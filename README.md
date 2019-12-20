# `Jangli`

### Scope

* Data Definition
* Data mapping  

### Convert json to python object.

```
from jangli.json_utils.json_to_object import json_to_obj

data = '{"password": "123456", "id": 1, "name": "abhimanyu"}'



class Student:
    def __init__(self):
        self.id = None
        self.name = None
        self.password = None


s = json_to_obj(data, Student)
print(s.name)
```


### Convert json to python object.

```
from jangli.json_utils.json_to_object import json_to_obj

data_2 = '{"password": "123456", "id": 1, "name": "abhimanyu", "school" : "SOHS"}'


class Student:
    school = None

    def __init__(self):
        self.id = None
        self.name = None
        self.password = None


s2 = json_to_obj(data_2, Student)
print(s2.school)

```

### Custom object list
```
from jangli.list_of_object import ListObject


class A:
    def __init__(self, b):
        self.b = b


lt = ListObject(A)
lt.append(A(7))
lt.insert(1, A(8))

print(lt)

Output : [<__main__.A object at 0x00CA3730>, <__main__.A object at 0x00CC6E10>]
```

### Case Change to CamelCase

```
from jangli.case_type import CamelCase


@CamelCase
class NewClass:

    def __init__(self):
        self.a = 7
        self.b = "hi"
        self.c = True
        self._from = None


new = NewClass()

print(new.__dict__)

```

### String of None to None

```
from jangli.checker.none_checker import NoneChecker

@NoneChecker
class A:

    def __init__(self):
        self.b = 8
        self.c = "None"
        self.d = True


print(A().__dict__)
>>> {'b': 8, 'c': None, 'd': True}

```