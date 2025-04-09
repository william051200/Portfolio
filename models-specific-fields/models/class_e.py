from models.base_class import BaseClass


class Class_E(BaseClass):
    def __init__(self):
        super().__init__()

    def get_E(self):
        return "E"

    def initialize_mappings(self):
        self._register_function("get_E", self.get_E)
