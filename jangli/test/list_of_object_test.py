from jangli.list_of_object import ListObject


class A:
    def __init__(self, b):
        self.b = b


def append_test():
    lt = ListObject(A)
    lt.append(A(7))
    print(lt)


def insert_test():
    lt = ListObject(A)
    lt.insert(1, A(8))
    print(lt)
