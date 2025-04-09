import uuid
from typing import Any, Dict, List, Union, Callable
from enums.mapping_type import MappingType
from models.mapping_manager import MappingManager
from models.value_processor import ValueProcessor
from models.delimiter_config import DelimiterConfig


class BaseClass:
    def __init__(self):
        self._id = str(uuid.uuid4())
        self._mapping_manager = MappingManager()

    @property
    def id(self) -> str:
        return self._id

    def _initialize_mappings(self) -> None:
        """Initialize all mappings for functions, properties and child objects.
        This method should be overridden by child classes."""
        pass

    def _register_function(self, name: str, func: Callable) -> None:
        """Register a function in the mapping."""
        self._mapping_manager.register_function(name, func)

    def _register_property(self, name: str, prop: property) -> None:
        """Register a property in the mapping."""
        self._mapping_manager.register_property(name, prop)

    def _register_properties(self, name: str, props: List[property]) -> None:
        """Register multiple property in the mapping."""
        self._mapping_manager.register_properties(name, props)

    def _register_child(self, child: 'BaseClass') -> None:
        """Register a child object in the mapping."""
        self._mapping_manager.register_child(child)

    def _register_children(self, children: List['BaseClass']) -> None:
        """Register multiple child objects in the mapping."""
        self._mapping_manager.register_children(children)

    def get_value(self, keys: List[str]) -> Any:
        """Get value by traversing through mapping hierarchy using a list of keys.

        Args:
            keys: List of keys to traverse the mapping hierarchy.
                 If empty, processes all mappings.

        Returns:
            The value(s) found at the specified key path.

        Raises:
            KeyError: If a key in the path is not found.
        """
        current = self._mapping_manager.get_mapping()

        # If no keys provided, process all mappings
        if not keys:
            result = {}
            for name, mapping in current.items():
                result[name] = ValueProcessor.get_instance().process_mapping(
                    mapping["type"],
                    mapping["value"],
                    self
                )
            return result

        # Process specific keys
        for i, key in enumerate(keys):
            if key not in current:
                raise KeyError(f"Key '{key}' not found")

            mapping = current[key]
            mapping_type = mapping["type"]
            value = mapping["value"]

            if mapping_type in (MappingType.FUNCTION, MappingType.PROPERTY):
                return ValueProcessor.get_instance().process_mapping(mapping_type, value, self)
            else:  # CHILD type
                if i == len(keys) - 1:  # If this is the last key
                    return value.get_value([])
                else:  # If there are more keys to process
                    current = value._mapping_manager.get_mapping()

        return current

    def to_string(self, value: Any = None) -> str:
        """Convert a value to string using the configured delimiters.

        Args:
            value: The value to convert. If None, uses the result of get_value([]).

        Returns:
            str: The formatted string representation of the value.

        Raises:
            ValueError: If no delimiter configuration was provided.
        """
        value_processor = ValueProcessor.get_instance()

        if value is None:
            value = self.get_value([])

        return value_processor.to_string(value)
