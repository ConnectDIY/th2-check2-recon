# Copyright 2020-2020 Exactpro (Exactpro Systems Limited)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import queue
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread

from grpc_common import common_pb2

from th2_check2_recon import store

logger = logging.getLogger()


class QueueListener:

    def __init__(self, routing_key: str, cache_size: int, channel, timeout, index: int) -> None:
        self.queue = channel.queue_declare(queue='',
                                           exclusive=True)
        self.queue_name = self.queue.method.queue
        self.routing_key = routing_key
        self.buffer = queue.Queue(cache_size)
        self.timeout = timeout
        self.index = index


def log_table_messages(messages, col_size):
    result = ''
    field_names = []
    for message in messages:
        for field_name in message.fields.keys():
            field_names.append(field_name)

    result += '\n|' + 'message_type'.ljust(col_size, ' ') + '|'
    for message in messages:
        result += message.metadata.message_type.ljust(col_size, ' ') + '|'

    result += '\n|' + 'id'.ljust(col_size, ' ') + '|'
    for message in messages:
        result += str(message.metadata.id.sequence).ljust(col_size, ' ') + '|'

    result += '\n|' + 'timestamp'.ljust(col_size, ' ') + '|'
    for message in messages:
        result += str(message.metadata.timestamp.seconds).ljust(col_size, ' ') + '|'

    result += '\n' + '-' * ((len(messages) + 1) * col_size + len(messages) + 2)
    for field_name in field_names:
        result += '\n|' + field_name.ljust(col_size, ' ') + '|'
        for message in messages:
            value: common_pb2.Value = message.fields[field_name]
            if len(value.simple_value) > 0:
                field_value = value.simple_value
            else:
                if len(value.list_value.values) > 0:
                    field_value = 'NOT_EMPTY_LIST'  # TODO fix
                else:
                    if len(value.message_value.fields) > 0:
                        field_value = 'SUB_MESSAGE'  # TODO fix
                    else:
                        field_value = 'EMPTY'
            result += field_value.ljust(col_size, ' ') + '|'
    return result


def log_result(indices, cache, queue_listeners):
    col_size = 30
    result = ''
    for elem_idx in range(len(indices)):

        result += '\n\n' + '*' * ((len(queue_listeners.values()) + 1) * col_size + len(queue_listeners.values()) + 2)
        result += '\n|' + 'Field'.ljust(col_size, ' ') + '|'
        for i in range(len(queue_listeners.values())):
            key = ""
            for queue_listener in queue_listeners.values():
                if i == queue_listener.index:
                    key = queue_listener.routing_key
                    break
            result += key.ljust(col_size, ' ') + '|'
        result += '\n' + '*' * ((len(queue_listeners.values()) + 1) * col_size + len(queue_listeners.values()) + 2)

        messages = []
        for seq_idx in range(len(indices[elem_idx])):
            messages.append(cache[seq_idx][indices[elem_idx][seq_idx]])
        result += log_table_messages(messages, col_size)
    logging.info(result)


def get_timestamp(message: common_pb2.Message):
    return message.metadata.timestamp.seconds * 1_000_000_000 + message.metadata.timestamp.nanos


class Cache:

    def __init__(self, cache_size: int, time_interval: int, routing_keys: list, event_store: store.Store,
                 rule_event_id: common_pb2.EventID) -> None:
        self.cache_size = cache_size
        self.time_interval = time_interval * 1_000_000_000
        self.min_time = 0
        self.event_store = event_store
        self.rule_event_id = rule_event_id
        self.data = {key: dict() for key in routing_keys}
        self.min_by_key = {key: set() for key in routing_keys}  # TODO fix search fast usable set for find minimum
        self.hash_by_timestamp = {key: {} for key in routing_keys}  # TODO fix search fast usable set for find minimum

    def contains(self, hash_of_message: str, routing_key: str) -> bool:
        return self.data[routing_key].__contains__(hash_of_message)

    def get(self, routing_key: str, hash_of_message: str) -> common_pb2.Message:
        return self.data[routing_key][hash_of_message]

    def remove_matched(self, hash_of_message: str, messages_by_routing_key: dict):
        for key in messages_by_routing_key.keys():
            self.remove(key, hash_of_message)

    def put(self, routing_key: str, hash_of_message: str, message: common_pb2.Message, event_name_suffix: str):
        if len(self.data[routing_key]) < self.cache_size:
            if self.contains(hash_of_message, routing_key):
                event_message = 'The message was deleted because a new message was received with the same hash.'
                self.remove(routing_key, hash_of_message, event_message, event_name_suffix)
                self.put(routing_key, hash_of_message, message, event_name_suffix)
            else:
                self.data[routing_key][hash_of_message] = message
                self.min_by_key[routing_key].add(get_timestamp(message))
                self.hash_by_timestamp[routing_key][get_timestamp(message)] = hash_of_message
                self.min_time = max(self.min_time, get_timestamp(message) - self.time_interval)
        else:
            event_message = 'The message was deleted because there was no free space in the cache.'
            hash_for_del = self.hash_by_timestamp[routing_key][min(self.min_by_key[routing_key])]
            self.remove(routing_key, hash_for_del, event_message, event_name_suffix)
            self.put(routing_key, hash_of_message, message, event_name_suffix)

    def remove(self, routing_key: str, hash_of_message: str, event_message="", event_name_suffix=""):
        message = self.data[routing_key][hash_of_message]
        timestamp = get_timestamp(message)
        if event_message != '':
            event_name = f"Removed '{routing_key}': '{message.metadata.message_type}'"
            event_name += event_name_suffix
            self.event_store.store_no_match(self.rule_event_id, message, event_name, event_message)

        self.hash_by_timestamp[routing_key].pop(timestamp)
        self.min_by_key[routing_key].remove(timestamp)
        self.data[routing_key].pop(hash_of_message)

    def clear(self):
        event_message = 'The message was deleted because the Recon stopped.'
        for routing_key in self.data.keys():
            while len(self.data[routing_key]) > 0:  # TODO fix it
                for hash_of_message in self.data[routing_key].keys():
                    self.remove(routing_key, hash_of_message, event_message)
                    break


class Recon:

    def __init__(self, rules: list, queue_listeners: dict) -> None:
        self.is_stopped = True
        self.rules = rules
        self.queue_listeners = queue_listeners

    def start(self):
        self.is_stopped = False
        Thread(target=self.run, args=()).start()

    def stop(self):
        self.is_stopped = True

    def run(self):
        with ThreadPoolExecutor(20) as executor:
            try:
                while not self.is_stopped:
                    some_not_empty = False
                    for queue_listener in self.queue_listeners.values():
                        if not queue_listener.buffer.empty():
                            some_not_empty = True
                            break
                    for queue_listener in self.queue_listeners.values():
                        if self.is_stopped:
                            break
                        timeout = 0 if some_not_empty else queue_listener.timeout
                        try:
                            message = queue_listener.buffer.get(block=not some_not_empty,
                                                                timeout=timeout)
                            for rule in self.rules:
                                rule.process(message, queue_listener.routing_key, executor)
                        except queue.Empty:
                            if not some_not_empty:
                                logger.debug(
                                    f'{queue_listener.routing_key}: no messages '
                                    f'from buffer within {queue_listener.timeout} sec')
                        except Exception as e:
                            logger.error(e)

                for rule in self.rules:
                    rule.cache.clear()
            except Exception as e:
                logger.error('service.run(): ', e)
