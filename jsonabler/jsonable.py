from __future__ import annotations

from abc import ABC, abstractmethod

from . import JSONDataType


class Jsonable(ABC):
    @abstractmethod
    def get_jsonable_data(self) -> JSONDataType:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_jsonable_data(cls, data: JSONDataType) -> Jsonable:
        raise NotImplementedError
