from models.class_b import Class_B

class Class_A:
    def __init__(self):
        self._class_b = Class_B()

    @property
    def class_b(self):
        return self._class_b

    @property
    def get_result(self):
        return "result"

    def get_count(self):
        return "count"

    def get_formatter_mapping(self):
        return {
            "get_result": self.get_result,
            "get_count": self.get_count,
            "class_b": self.class_b.get_formatter_mapping(),
        }

    def get_all(self):
        return {
            "get_result": self.get_result,
            "get_count": self.get_count(),
            "class_b": self.class_b.get_all(),
        }