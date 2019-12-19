from jangli.case_type import CamelCase, PascalCase


@CamelCase
class NewClass:

    def __init__(self):
        self.a = 7
        self.b = "hi"
        self.c = True
        self._from = None


@PascalCase
class NewClass1:

    def __init__(self):
        self.a = 7
        self.b = "hi"
        self.c = True
        self._from = None


new = NewClass()

print(new.__dict__)

new = NewClass1()

print(new.__dict__)
