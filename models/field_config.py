class FieldConfig:
    def __init__(self, path, prefix=None, suffix=None, simplified=False):
        self._path = path
        self._prefix = prefix or ""
        self._suffix = suffix or ""
        self._simplified = simplified

    @property
    def path(self):
        return self._path

    @property
    def prefix(self):
        return self._prefix

    @property
    def suffix(self):
        return self._suffix

    @property
    def simplified(self):
        return self._simplified
