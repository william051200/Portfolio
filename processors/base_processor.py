from abc import ABC, abstractmethod
from utils.file_reader import JsonReader


class BaseProcessor(ABC):
    def __init__(self, field_list):
        self.field_list = field_list

    @property
    def field_count(self):
        return self.field_list.count

    @abstractmethod
    def process_field_by_index(self, index):
        pass

    def process_all_fields(self):
        return [self.process_field_by_index(i) for i in range(self.field_count)]
