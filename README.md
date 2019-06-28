# `Jangli`

### Scope

* Data Definition
* Data mapping  

### [1] Convert json to python object.

```
from json_utils.json_to_object import json_to_obj

data = '{"password": "123456", "id": 1, "name": "abhimanyu"}'



class Student:
    def __init__(self):
        self.id = None
        self.name = None
        self.password = None


s = json_to_obj(data, Student)
print(s.name)
```


### [2] Convert json to python object.

```
from json_utils.json_to_object import json_to_obj

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

### [3] Custom object list
```
class A:
    def __init__(self, b):
        self.b = b


lt = ListObject(A)
lt.append(A(7))
lt.insert(1, A(8))

print(lt)

Output : [<__main__.A object at 0x00CA3730>, <__main__.A object at 0x00CC6E10>]
```