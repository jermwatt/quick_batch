import functools
import traceback
import sys


class LogExceptions:
    def __init__(self):
        # self.file_path = file_path
        pass

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                # with open(self.file_path, 'a') as file:
                #     file.write(f"FAILURE: {func_name} failed: {e}\n")
                #     traceback.print_exc(file=file)
                print(f"FAILURE: {func_name} failed: {e}")
            else:
                # with open(self.file_path, 'a') as file:
                #     file.write(f"SUCCESS: {func_name} succeeded\n")
                print(f"SUCCESS: {func_name} succeeded")
                return result
        return wrapper


def decorate_methods(decorator):
    def decorate(obj):
        if isinstance(obj, type):
            # Decorate class methods
            for name, method in vars(obj).items():
                if callable(method):
                    setattr(obj, name, decorator(method))
            return obj
        else:
            # Decorate standalone functions
            return decorator(obj)
    return decorate



class Logger(object):
    def __init__(self, log_file):
        self.terminal = sys.stdout
        self.log_file = log_file
        self.log = None

    def open_log(self):
        self.log = open(self.log_file, "a")

    def write(self, message):
        self.terminal.write(message)
        self.terminal.flush()  # Flush the terminal output
        self.log.write(message)
        self.log.flush()  # Flush the log file output

    def flush(self):
        pass

    def close_log(self):
        self.log.close()



# class Logger(object):
#     def __init__(self, log_file):
#         self.terminal = sys.stdout
#         self.log_file = log_file
#         self.log = None

#     def open_log(self):
#         self.log = open(self.log_file, "a")

#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)

#     def flush(self):
#         pass

#     def close_log(self):
#         self.log.close()

