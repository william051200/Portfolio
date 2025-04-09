from models.base_class import BaseClass


class Class_B(BaseClass):
    def __init__(self):
        super().__init__()
        self._class_c = None
        self._class_d = []

    @property
    def class_c(self):
        return self._class_c

    @property
    def class_d(self):
        return self._class_d

    def get_number(self):
        return "number"

    def initialize_mappings(self):
        self._register_function("get_number", self.get_number)
        # self._register_property("class_c", self.class_c)
        # self._register_properties("class_d", self.class_d)
        self._register_child(self.class_c)
        self._register_children(self.class_d)
