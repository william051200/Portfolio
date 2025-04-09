from models.base_class import BaseClass


class Class_C(BaseClass):
    def __init__(self):
        super().__init__()
        self._class_e = None

    @property
    def class_e(self):
        return self._class_e

    def get_number(self):
        return "2"

    def get_end(self):
        return "end"

    def initialize_mappings(self):
        self._register_function("get_number", self.get_number)
        self._register_function("get_end", self.get_end)
        # self._register_property("class_e", self.class_e)
        self._register_child(self.class_e)
