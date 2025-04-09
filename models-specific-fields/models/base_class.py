import uuid
from typing import Any, Dict, List, Union, Callable
from enums.mapping_type import MappingType


class BaseClass:
    def __init__(self):
        self._id = str(uuid.uuid4())
        self._mapping: Dict[str, Dict[str, Any]] = {}

    @property
    def id(self) -> str:
        return self._id

    def _initialize_mappings(self) -> None:
        """Initialize all mappings for functions, properties and child objects.
        This method should be overridden by child classes."""
        pass

    def _register_function(self, name: str, func: Callable) -> None:
        """Register a function in the mapping."""
        self._mapping[name] = {
            "type": MappingType.FUNCTION,
            "value": func
        }

    def _register_property(self, name: str, prop: property) -> None:
        """Register a property in the mapping."""
        self._mapping[name] = {
            "type": MappingType.PROPERTY,
            "value": prop
        }

    def _register_properties(self, name: str, props: List[property]) -> None:
        """Register multiple property in the mapping."""
        for prop in props:
            self._register_property(name, prop)

    def _register_child(self, child: 'BaseClass') -> None:
        """Register a child object in the mapping."""
        if child is not None:
            self._mapping[child.id] = {
                "type": MappingType.CHILD,
                "value": child
            }

    def _register_children(self, children: List['BaseClass']) -> None:
        """Register multiple child objects in the mapping."""
        for child in children:
            self._register_child(child)

    def _process_function_mapping(self, value: Callable) -> Any:
        """Process a function mapping by executing the function."""
        return value()

    def _process_property_mapping(self, value: Any, instance: 'BaseClass') -> Any:
        """Process a property mapping by getting its value."""
        if isinstance(value, property):
            return value.fget(instance)
        return value

    def _process_child_mapping(self, child: 'BaseClass') -> Dict[str, Any]:
        """Process a child object's mappings recursively."""
        child_result = {}
        for name, mapping in child._mapping.items():
            mapping_type = mapping["type"]
            value = mapping["value"]

            if mapping_type == MappingType.FUNCTION:
                child_result[name] = self._process_function_mapping(value)
            elif mapping_type == MappingType.PROPERTY:
                child_result[name] = self._process_property_mapping(
                    value, child)
            else:  # CHILD type
                child_result[name] = value.get_value([])
        return child_result

    def _process_mapping(self, mapping_type: MappingType, value: Any, instance: 'BaseClass') -> Any:
        """Process a single mapping based on its type."""
        if mapping_type == MappingType.FUNCTION:
            return self._process_function_mapping(value)
        elif mapping_type == MappingType.PROPERTY:
            return self._process_property_mapping(value, instance)
        else:  # CHILD type
            return self._process_child_mapping(value)

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
        current = self._mapping

        # If no keys provided, process all mappings
        if not keys:
            result = {}
            for name, mapping in current.items():
                result[name] = self._process_mapping(
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
                return self._process_mapping(mapping_type, value, self)
            else:  # CHILD type
                if i == len(keys) - 1:  # If this is the last key
                    return value.get_value([])
                else:  # If there are more keys to process
                    current = value._mapping

        return current
