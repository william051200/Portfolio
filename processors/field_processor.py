from models.class_a import Class_A


class FieldProcessor:
    def __init__(self, formatter):
        self._formatter = formatter
        self._root_class = Class_A()

    @property
    def formatter(self):
        return self._formatter

    @formatter.setter
    def formatter(self, value):
        self._formatter = value

    @property
    def root_class(self):
        return self._root_class

    @root_class.setter
    def root_class(self, value):
        self._root_class = value

    def _process_list_attribute(self, obj_list, attribute):
        """Process attribute for each item in a list"""
        return [getattr(item, attribute) for item in obj_list]

    def _process_single_attribute(self, obj, attribute):
        """Process attribute for a single object"""
        return getattr(obj, attribute)

    def _process_path_step(self, obj, step):
        """Process a single step in the path"""
        if isinstance(obj, list):
            return self._process_list_attribute(obj, step)
        return self._process_single_attribute(obj, step)

    def _process_value(self, obj):
        """Process final value based on its type"""
        if isinstance(obj, list):
            return [self._process_value(item) for item in obj]
        if hasattr(obj, "get_all"):
            return obj.get_all()
        if callable(obj):
            return obj()
        return obj

    def process_field_by_index(self, index):
        """Process a field by its index"""
        if index < 0 or index >= self.formatter.count:
            raise ValueError(
                f"Field index {index} out of range (0-{self.formatter.count-1})"
            )

        field = self.formatter.get_field(index)
        result = self.root_class

        # Process each step in the path
        for step in field.path:
            result = self._process_path_step(result, step)

        return self._process_value(result)

    def process_all_fields(self):
        """Process all fields in the list"""
        return [self.process_field_by_index(i) for i in range(self.formatter.count)]
