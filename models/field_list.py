class FieldList:
    def __init__(self, fields):
        self._fields = fields

    @property
    def fields(self):
        return self._fields

    @property
    def count(self):
        return len(self._fields)

    def get_field(self, index):
        return self._fields[f"field{index + 1}"]