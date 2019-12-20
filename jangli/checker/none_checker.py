class NoneChecker:
    def __init__(self, function):
        self.function = function
        self.obj = None

    def __call__(self, *args, **kwargs):
        try:
            self.obj = self.function(*args, **kwargs)
            func_dict = self.obj.__dict__
            [self.obj.__setattr__(_var, None) for _var in func_dict
             if func_dict[_var] == "None"]
            return self.obj
        except Exception as e:
            print(e)
            raise e

    def __instancecheck__(self, dec_class):
        return self.obj
