# jsonabler

Python package for making your classes easy encodable to JSON string and vice-versa. 

[![Lint & Test](https://github.com/webfucktory/python-jsonabler/actions/workflows/lint-test.yml/badge.svg)](https://github.com/webfucktory/python-jsonabler/actions/workflows/lint-test.yml)
[![PyPI version](https://badge.fury.io/py/jsonabler.svg)](https://pypi.org/project/jsonabler)
[![Downloads count](https://img.shields.io/pypi/dm/jsonabler)](https://pypistats.org/packages/jsonabler)

## Getting started

### Requirements

- Python >= 3.8

### Installation

```bash
pip install jsonabler
```

## Usage

### Making a Jsonable 

Make your class extends the `Jsonable` interface and implements `get_jsonable_data` and `from_jsonable_data` methods with the encoding/decoding logic. 

```python
from jsonabler import Jsonable, jsonabled 

@jsonabled
class Foo(Jsonable):
    def __init__(self, bar: str):
        self.__bar = bar
    
    def get_jsonable_data(self) -> dict:
        return {
            'bar': self.__bar,
        }

    @classmethod
    def from_jsonable_data(cls, data: dict) -> Jsonable:
        return cls(data['bar'])
```

### Registering a Jsonable

For decoding your Jsonable classes, you need to register it.

#### Decorating your classes with the `@jsonabled` decorator

```python
from jsonabler import Jsonable, jsonabled 

@jsonabled
class Foo(Jsonable):
    ...
```    

#### Calling `register_jsonables` method passing class types

```python
from jsonabler import Jsonable, register_jsonables 

class Foo(Jsonable):
    ...

if __name__ == '__main__':
    register_jsonables({Foo})
```

### Encoding a Jsonable

Call `dumps` method passing a `Jsonable` object.

```python
from jsonabler import dumps

def upload_foo(foo: Foo) -> None:    
    json_string = dumps(foo)
    
    # transmit your JSON string
    ...
```

#### Encoded Foo
```json5
[
  'Foo',
  {
    'bar': "abc",
  }
]
```

### Decoding a Jsonable

Call `loads` method passing the JSON string.

```python
from jsonabler import loads, JsonableDecodeError, JsonableNotRegisteredError
from json import JSONDecodeError

def download_foo() -> Foo:    
    # receive JSON string encoded Foo object
    ...

    try:
        return loads(json_string)
    
    # not a valid encoded JSON string
    except JSONDecodeError:  
        ...
    
    # the Jsonable type of the encoded object was not registered
    except JsonableNotRegisteredError:  
        ...
    
    # something went wrong while decoding the object
    except JsonableDecodeError:  
        ...
```

## License

Distributed under the MIT License. See `LICENSE` file for more information.
