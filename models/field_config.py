class FieldConfig:
    def __init__(self, name, path, prefix=None, suffix=None):
        self._name = name
        self._path = path
        self._prefix = prefix or ""
        self._suffix = suffix or ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        self._prefix = value or ""

    @property
    def suffix(self):
        return self._suffix

    @suffix.setter
    def suffix(self, value):
        self._suffix = value or ""
