# Json_Object_Conv

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
