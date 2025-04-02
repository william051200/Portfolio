from models.class_c import Class_C
from models.class_d import Class_D

class Class_B:
    def __init__(self):
        self._class_c = Class_C()
        self._class_d = [Class_D(), Class_D()]

    @property
    def class_c(self):
        return self._class_c

    @property
    def class_d(self):
        return self._class_d

    def get_number(self):
        return "number"

    def get_formatter_mapping(self):
        return {
            "get_number": self.get_number,
            "class_c": self.class_c.get_formatter_mapping(),
            "class_d": [d.get_formatter_mapping() for d in self.class_d],
        }

    def get_all(self):
        return {
            "get_number": self.get_number(),
            "class_c": self.class_c.get_all(),
            "class_d": [d.get_all() for d in self.class_d],
        }