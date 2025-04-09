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

    @property
    def get_xyz(self):
        return 'xyz'

    def get_number(self):
        return "number"
