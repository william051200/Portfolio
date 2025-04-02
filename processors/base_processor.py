from abc import ABC, abstractmethod
from utils.file_reader import JsonReader


class BaseProcessor(ABC):
    def __init__(self, config_file):
        self.configs = JsonReader.read_json(config_file)
        self.root_class = None

    @abstractmethod
    def process_combo(self, combo_name):
        pass

    def process_all_combos(self):
        return {name: self.process_combo(name) for name in self.configs}
