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
