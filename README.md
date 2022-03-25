# jsonabler

A simple Python object to JSON string encoder/decoder. 

## Making a Jsonable 

Make your class extends `Jsonable` and implements `get_jsonable_data` and `from_jsonable_data` methods with the encoding/decoding logic.

```python
from jsonabler import Jsonable 

class Foo(Jsonable):
    def __init__(self, bar: str):
        self.__bar = bar
        
    # ...
    
    def get_jsonable_data(self) -> dict:
        return {
            'bar': self.__bar,
        }

    @classmethod
    def from_jsonable_data(cls, data: dict) -> Jsonable:
        return cls(data['bar'])
```

## Encoding a Jsonable

Call `dumps` method passing a Jsonable object.

```python
from jsonabler import dumps

def upload_foo(foo: Foo) -> None:    
    json_string = dumps(foo)
    
    # transmit your JSON string
    ...
```

### Encoded Foo
```json5
[
  'Foo',
  {
    'bar': "abc",
  }
]
```

## Decoding a Jsonable

1. Call `register_jsonable` method for registering the Jsonables types;
2. Call `loads` method passing the JSON string.

```python
from jsonabler import register_jsonables, loads, JsonableDecodeError, JsonableNotRegisteredError
from json import JSONDecodeError

def download_foo() -> Foo:
    # register Jsonable types for decoding
    register_jsonables({Foo})
    
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
