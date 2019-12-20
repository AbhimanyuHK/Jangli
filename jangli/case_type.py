class BaseClass:

    def __init__(self, function):
        self.function = function
        self.obj = None

    def __instancecheck__(self, dec_class):
        return self.obj


class CamelCase(BaseClass):

    def __call__(self, *args, **kwargs):
        try:
            self.obj = self.function(*args, **kwargs)
            func_dict = self.obj.__dict__
            class_var_value = {var: func_dict[var] for var in func_dict}
            for _var in class_var_value:
                r_var = self.camel_type(_var)
                self.obj.__setattr__(r_var, class_var_value[_var])
                if r_var != _var:
                    self.obj.__delattr__(_var)

            return self.obj

        except Exception as e:
            print("Error while converting to camel case : {}".format(e))
            raise e

    @staticmethod
    def camel_type(snake_str):
        try:
            snake_str_list = snake_str.split("_")
            if len(snake_str_list) > 1:
                return str(snake_str_list[0]) + str("".join(x.title() for x in snake_str_list[1:]))
            else:
                return snake_str_list[0]
        except Exception as e:
            print("Error While converting to camel case : {}".format(e))
            raise e


class PascalCase(BaseClass):

    def __call__(self, *args, **kwargs):
        try:
            self.obj = self.function(*args, **kwargs)
            func_dict = self.obj.__dict__
            class_var_value = {var: func_dict[var] for var in func_dict}
            for _var in class_var_value:
                r_var = self.pascal_type(_var)
                self.obj.__setattr__(r_var, class_var_value[_var])
                if r_var != _var:
                    self.obj.__delattr__(_var)

            return self.obj

        except Exception as e:
            print("Error while converting to pascal case : {}".format(e))
            raise e

    @staticmethod
    def pascal_type(snake_str):
        try:
            snake_str_list = snake_str.split("_")
            return "".join(x.title() for x in snake_str_list)
        except Exception as e:
            print("Error While converting to pascal case : {}".format(e))
            raise e
