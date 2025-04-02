class DelimiterConfig:
    def __init__(
        self,
        array_start="[",
        array_end="]",
        array_separator=", ",
        object_start="{",
        object_end="}",
        object_separator=", ",
        key_value_separator=": ",
    ):
        self._array_start = array_start
        self._array_end = array_end
        self._array_separator = array_separator
        self._object_start = object_start
        self._object_end = object_end
        self._object_separator = object_separator
        self._key_value_separator = key_value_separator

    @property
    def array_start(self):
        return self._array_start

    @array_start.setter
    def array_start(self, value):
        self._array_start = value

    @property
    def array_end(self):
        return self._array_end

    @array_end.setter
    def array_end(self, value):
        self._array_end = value

    @property
    def array_separator(self):
        return self._array_separator

    @array_separator.setter
    def array_separator(self, value):
        self._array_separator = value

    @property
    def object_start(self):
        return self._object_start

    @object_start.setter
    def object_start(self, value):
        self._object_start = value

    @property
    def object_end(self):
        return self._object_end

    @object_end.setter
    def object_end(self, value):
        self._object_end = value

    @property
    def object_separator(self):
        return self._object_separator

    @object_separator.setter
    def object_separator(self, value):
        self._object_separator = value

    @property
    def key_value_separator(self):
        return self._key_value_separator

    @key_value_separator.setter
    def key_value_separator(self, value):
        self._key_value_separator = value
