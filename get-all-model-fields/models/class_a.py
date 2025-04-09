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

    @property
    def get_tail(self):
        return "tail"

    def get_count(self):
        return "count"

    def get_abc(self):
        return "abc"
