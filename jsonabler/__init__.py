# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Generic release markers:
#   X.Y.0   # For first release after an increment in Y
#   X.Y.Z   # For bugfix releases
__version__ = '0.1.5'

import json as json
from typing import Set as Set, Tuple as Tuple, Type as Type

from .jsonable import Jsonable

_jsonables: Set[Type[Jsonable]] = set()


class JsonableNotRegisteredError(ValueError):
    pass


class JsonableDecodeError(ValueError):
    pass


class JsonableEncodeError(ValueError):
    pass


def __get_type(s: str) -> Type[Jsonable]:
    for j in _jsonables:
        if j.__name__ == s:
            return j

    raise JsonableNotRegisteredError(s)


def jsonabled(cls: Type[Jsonable]):
    register_jsonables({cls})

    return cls


def register_jsonables(josanable_types: Set[Type[Jsonable]]) -> None:
    """
    Registers Jsonable types for being loaded from JSON encoded strings.
    It is necessary to register your Jsonable types before loading them.

    :param josanable_types: Jsonable types to register.
    :return: None.
    """

    assert type(josanable_types), Set[Type[Jsonable]]

    _jsonables.update(josanable_types)


def loads(s: str) -> Jsonable:
    """
    Decodes a JSON encoded string and return a Jsonable type object.
    The jsonable type must be registered first using the `register_jsonables` method.

    :param s: JSON encoded string.
    :return: Jsonable type object decoded from input string.
    :raises TypeError: if input is not a string.
    :raises JSONDecodeError: if input string is not a valid JSON encoded string.
    :raises JsonableDecodeError: if input string is a valid JSON encoded string, but it is not a valid Jsonable type
        encoded object.
    :raises JsonableNotRegisteredError: if input string is a valid JSON encoded string and a valid Jsonable type
        encoded object, but the encoded Jsonable object type has not been registered.
    """

    t: Tuple[str, dict] = tuple(json.loads(s))

    if len(t) < 2:
        raise JsonableDecodeError("Input string is not a valid Jsonable encoded object")

    j: Type[Jsonable] = __get_type(t[0])

    try:
        return j.from_jsonable_data(t[1])

    except Exception:
        raise JsonableDecodeError("An error occured while decoding the Jsonable object, check the from_jsonable_data "
                                  "method")


def dumps(jsonable_object: Jsonable) -> str:
    """
    Encodes a Jsonable type object and return the JSON encoded string.

    :param jsonable_object: Jsonable type object to encode.
    :return: JSON encoded string.
    :raises JsonableEncodeError: if an exception was risen during get_jsonable_data() method execution of the passed
        object
    """

    try:
        return json.dumps((type(jsonable_object).__name__, jsonable_object.get_jsonable_data()))

    except Exception:
        raise JsonableEncodeError("An error occured while encoding the Jsonable object, check the get_jsonable_data "
                                  "method")
