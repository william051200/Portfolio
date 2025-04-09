from models.base_class import BaseClass


class Class_D(BaseClass):
    def __init__(self):
        super().__init__()
        self._class_e = []

    @property
    def class_e(self):
        return self._class_e

    def get_array(self):
        return "array"
