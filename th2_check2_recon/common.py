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
import uuid
from datetime import datetime
from json import JSONEncoder

from google.protobuf.timestamp_pb2 import Timestamp
from th2_grpc_common.common_pb2 import Event, Message
from th2_grpc_common.common_pb2 import EventStatus, EventID, MessageID, FilterOperation, Direction
from th2_grpc_util.util_pb2 import ComparisonEntryStatus, ComparisonEntry, ComparisonEntryType

logger = logging.getLogger()


class EventUtils:
    class __ComponentEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

    @staticmethod
    def create_event_body(component) -> bytes:
        return EventUtils.component_encoder().encode(component).encode()

    @staticmethod
    def component_encoder() -> __ComponentEncoder:
        return EventUtils.__ComponentEncoder()

    @staticmethod
    def new_event_id():
        return EventID(id=str(uuid.uuid1()))

    @staticmethod
    def create_event(name: str, id: EventID = None, parent_id: EventID = None,
                     status: EventStatus = EventStatus.SUCCESS, body: bytes = None,
                     attached_message_ids: [MessageID] = None) -> Event:
        if id is None:
            id = EventUtils.new_event_id()
        if attached_message_ids is None:
            attached_message_ids = []
        start_time = datetime.now()
        seconds = int(start_time.timestamp())
        nanos = int(start_time.microsecond * 1000)
        return Event(id=id,
                     parent_id=parent_id,
                     start_timestamp=Timestamp(seconds=seconds, nanos=nanos),
                     end_timestamp=Timestamp(seconds=seconds, nanos=nanos),
                     status=status,
                     name=name,
                     body=body,
                     attached_message_ids=attached_message_ids)


class MessageUtils:

    @staticmethod
    def get_timestamp_ns(message: Message) -> int:
        return message.metadata.timestamp.ToNanoseconds()

    @staticmethod
    def str_message_id(message: Message) -> str:
        res = str(message.metadata.id.connection_id.session_alias) + ':'
        res += str(Direction.Name(message.metadata.id.direction)) + ':'
        res += str(message.metadata.id.sequence)
        return res


class ComparatorUtils:

    @staticmethod
    def __get_result_count(comparison_result, status) -> int:
        count = 0
        if status == comparison_result.status:
            count += 1

        for sub_result in comparison_result.fields.values():
            count += ComparatorUtils.__get_result_count(sub_result, status)

        return count

    @staticmethod
    def __get_status_type_by_val(failed, passed) -> ComparisonEntryStatus:
        if failed != 0:
            return ComparisonEntryStatus.FAILED
        else:
            if passed != 0:
                return ComparisonEntryStatus.PASSED
        return ComparisonEntryStatus.NA

    @staticmethod
    def get_status_type(comparison_result: ComparisonEntry) -> ComparisonEntryStatus:
        failed = ComparatorUtils.__get_result_count(comparison_result, ComparisonEntryStatus.FAILED)
        passed = ComparatorUtils.__get_result_count(comparison_result, ComparisonEntryStatus.PASSED)
        return ComparatorUtils.__get_status_type_by_val(failed, passed)


class MessageComponent:

    def __init__(self, message: str) -> None:
        self.type = 'message'
        self.data = message


class TableComponent:

    def __init__(self, column_names: list) -> None:
        self.type = 'table'
        self.rows = []
        self.__column_names = column_names

    def add_row(self, *values):
        row = {self.__column_names[i]: values[i] for i in range(len(values))}
        self.rows.append(row)


class VerificationComponent:

    def __init__(self, comparison_entry: ComparisonEntry) -> None:
        self.type = 'verification'
        self.fields = {field_name: VerificationComponent.VerificationEntry(comparison_entry.fields[field_name])
                       for field_name in comparison_entry.fields.keys()}
        self.status = EventStatus.FAILED if ComparatorUtils.get_status_type(
            comparison_entry) == ComparisonEntryStatus.FAILED else EventStatus.SUCCESS

    class VerificationEntry:

        def __init__(self, comparison_entry: ComparisonEntry) -> None:
            self.type = ComparisonEntryType.Name(comparison_entry.type).lower()
            self.status = ComparisonEntryStatus.Name(comparison_entry.status)
            self.expected = comparison_entry.first
            self.actual = comparison_entry.second
            self.key = comparison_entry.is_key
            self.operation = FilterOperation.Name(comparison_entry.operation)
            self.fields = dict()

            if comparison_entry.type == ComparisonEntryType.COLLECTION:
                for field_name in comparison_entry.fields.keys():
                    self.fields[field_name] = \
                        VerificationComponent.VerificationEntry(comparison_entry.fields[field_name])
