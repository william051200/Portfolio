from typing import List

class FieldLine:
    def __init__(self, path: List[str], prefix: str, suffix: str):
        self._path = path
        self._prefix = prefix
        self._suffix = suffix

    @property
    def path(self) -> List[str]:
        return self._path

    @path.setter
    def path(self, value: List[str]) -> None:
        self._path = value

    @property
    def prefix(self) -> str:
        return self._prefix

    @prefix.setter
    def prefix(self, value: str) -> None:
        self._prefix = value

    @property
    def suffix(self) -> str:
        return self._suffix

    @suffix.setter
    def suffix(self, value: str) -> None:
        self._suffix = value