from typing import List
from .field_line import FieldLine

class FieldData:
    def __init__(self, id: int, name: str, field_lines: List[FieldLine]):
        self._id = id
        self._name = name
        self._field_lines = field_lines

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def field_lines(self) -> List[FieldLine]:
        return self._field_lines

    @field_lines.setter
    def field_lines(self, value: List[FieldLine]) -> None:
        self._field_lines = value