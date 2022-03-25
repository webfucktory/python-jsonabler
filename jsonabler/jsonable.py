from __future__ import annotations

from abc import ABC, abstractmethod


class Jsonable(ABC):
    @abstractmethod
    def get_jsonable_data(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_jsonable_data(cls, data: dict) -> Jsonable:
        pass
