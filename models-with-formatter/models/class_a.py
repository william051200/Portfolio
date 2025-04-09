from models.base_class import BaseClass


class Class_A(BaseClass):
    def __init__(self):
        super().__init__()
        self._class_b = None

    @property
    def class_b(self):
        return self._class_b

    @property
    def get_result(self):
        return "result"

    def get_count(self):
        return "count"

    def initialize_mappings(self):
        self._register_function("get_count", self.get_count)
        self._register_property("get_result", self.get_result)
        # self._register_property("class_b", self.class_b)
        self._register_child(self.class_b)
