import time


class Retry:
    """
    class Retry : This will retry the function by 1 time.
    """

    def __init__(self, except_function=None, retry_value=1, is_raisable=True, error_log_info="", delay=0):
        """
        Retry class : Default retry value is 1

        :param except_function:
        :type except_function:
        :param retry_value:
        :type retry_value:
        :param is_raisable:
        :type is_raisable:
        :param error_log_info:
        :type error_log_info:
        :param delay:
        :type delay:
        """
        self.except_function = except_function
        self.retry_value = retry_value
        self.is_raisable = is_raisable
        self.error_log_info = error_log_info
        self.delay = delay

    def __call__(self, function):
        """
        Calling function with arguments.
        Default retry is 1.
        Maximum 1 failure is ignored.

        :param function: Foo
        :param args: Foo args
        :param kwargs: Foo kwargs

        :return:
        """

        def inner_func(*args, **kwargs):
            """
            Inner function which executes the actual function and Except function.

            :param args:
            :param kwargs:
            :return:
            """
            if self.retry_value == 0:
                return
            for i in range(0, self.retry_value + 1):
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    if i == self.retry_value and self.is_raisable:
                        raise e
                    if self.except_function:
                        self.except_function(*args, **kwargs)
                    print("Try #{} {} failed with Exception: {}".format(i + 1, self.error_log_info, e))
                    if self.delay:
                        time.sleep(self.delay)
                    continue

        return inner_func
