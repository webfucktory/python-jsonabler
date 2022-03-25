from __future__ import annotations

from abc import ABC, abstractmethod


class Jsonable(ABC):
    @classmethod
    @abstractmethod
    def get_jsonable_data(cls) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_jsonable_data(cls, data: dict) -> Jsonable:
        pass
