from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Union

JSONDataType = Optional[Union[dict, list, tuple, str, int, float, bool]]


class Jsonable(ABC):
    @abstractmethod
    def get_jsonable_data(self) -> JSONDataType:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_jsonable_data(cls, data: JSONDataType) -> Jsonable:
        raise NotImplementedError
