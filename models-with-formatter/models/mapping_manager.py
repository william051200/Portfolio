from typing import Any, Dict, List, Callable
from enums.mapping_type import MappingType


class MappingManager:
    def __init__(self):
        self._mapping: Dict[str, Dict[str, Any]] = {}

    def register_function(self, name: str, func: Callable) -> None:
        """Register a function in the mapping."""
        self._mapping[name] = {
            "type": MappingType.FUNCTION,
            "value": func
        }

    def register_property(self, name: str, prop: property) -> None:
        """Register a property in the mapping."""
        self._mapping[name] = {
            "type": MappingType.PROPERTY,
            "value": prop
        }

    def register_properties(self, name: str, props: List[property]) -> None:
        """Register multiple property in the mapping."""
        for prop in props:
            self.register_property(name, prop)

    def register_child(self, child) -> None:
        """Register a child object in the mapping."""
        if child is not None:
            self._mapping[child.id] = {
                "type": MappingType.CHILD,
                "value": child
            }

    def register_children(self, children) -> None:
        """Register multiple child objects in the mapping."""
        for child in children:
            self.register_child(child)

    def get_mapping(self) -> Dict[str, Dict[str, Any]]:
        """Get the internal mapping dictionary."""
        return self._mapping
