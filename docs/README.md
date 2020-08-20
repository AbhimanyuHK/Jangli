
### Scope

* Data Definition
* Data mapping  

### Convert json to python object

Convert json or dict to model object.

#### Supports 
* dict
* json
* json dumps

```
from jangli.json_to_object import json_to_obj

data = '{"password": "123456", "id": 1, "name": "john"}'



class Student:
    def __init__(self):
        self.id = None
        self.name = None
        self.password = None


s = json_to_obj(data, Student)
print(s.name)
```


### Convert json to python object with static variable

Convert json or dict to model object. Class containing static variables

#### Supports 
* dict
* json
* json dumps

```
from jangli.json_to_object import json_to_obj

data_2 = '{"password": "123456", "id": 1, "name": "john", "school" : "SOHS"}'


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
Create list of similar object. Pass a model which you want create a list.
It only allows model objects which model passed whle creating list of objects.
  
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

Converter snack case to camel case. 

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

Change string of None to None,

EX : 

String of None is : x = 'None'

After change : x = None


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

### Re-Try Function

If a function failed one or many times, you can retry N no. of times just by passing retry_value = ?. 

#### If retry_value = 1 

A function will execute ones, mean while any error any occurring function will through exception.

```
@Retry(retry_value=1)
def x_fun():
    print("Function is executing ones")

```

#### If retry_value = 2

A function will execute twice if first execution fails else only ones.

```
@Retry(retry_value=2)
def x_fun():
    print("raise exception")
    raise Exception("Try twice")

```

#### If retry_value = 0

A function is disabled and could not execute the function.

```
@Retry(retry_value=0)
def x_fun():
    print("Function is disabled")

```

#### If delay of 10 seconds

A function will execute with delay of 10 seconds.

```
@Retry(delay=10)
def x_fun():
    print("Function with delay of 10 seconds.")

```


#### If need to pass raising exception

A function will execute with 3 times retry and no need to raise final failed exception.

 ```
@Retry(retry_value=3, is_raisable=False)
def x_fun():
    raise Exception("Pass exception")

```
