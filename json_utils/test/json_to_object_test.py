from json_utils.json_to_object import json_to_obj

data = '{"password": "123456", "id": 1, "name": "abhimanyu"}'
data_2 = '{"password": "123456", "id": 1, "name": "abhimanyu", "school" : "SOHS"}'


class Student:
    school = None

    def __init__(self):
        self.id = None
        self.name = None
        self.password = None


o = json_to_obj(data, Student)
print(o.__dict__)

p = json_to_obj(data_2, Student)
print(p.__dict__)
