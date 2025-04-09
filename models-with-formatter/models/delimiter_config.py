class DelimiterConfig:
    def __init__(self):
        self._array_start = ""
        self._array_end = ""
        self._array_separator = ""
        self._object_start = ""
        self._object_end = ""
        self._object_separator = ""
        self._key_value_separator = ""
        self._result_separator = ""

    # Getter and setter for array_start
    @property
    def array_start(self):
        return self._array_start

    @array_start.setter
    def array_start(self, value):
        self._array_start = value

    # Getter and setter for array_end
    @property
    def array_end(self):
        return self._array_end

    @array_end.setter
    def array_end(self, value):
        self._array_end = value

    # Getter and setter for array_separator
    @property
    def array_separator(self):
        return self._array_separator

    @array_separator.setter
    def array_separator(self, value):
        self._array_separator = value

    # Getter and setter for object_start
    @property
    def object_start(self):
        return self._object_start

    @object_start.setter
    def object_start(self, value):
        self._object_start = value

    # Getter and setter for object_end
    @property
    def object_end(self):
        return self._object_end

    @object_end.setter
    def object_end(self, value):
        self._object_end = value

    # Getter and setter for object_separator
    @property
    def object_separator(self):
        return self._object_separator

    @object_separator.setter
    def object_separator(self, value):
        self._object_separator = value

    # Getter and setter for key_value_separator
    @property
    def key_value_separator(self):
        return self._key_value_separator

    @key_value_separator.setter
    def key_value_separator(self, value):
        self._key_value_separator = value

    # Getter and setter for result_separator
    @property
    def result_separator(self):
        return self._result_separator

    @result_separator.setter
    def result_separator(self, value):
        self._result_separator = value
