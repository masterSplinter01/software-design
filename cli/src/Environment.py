import os

class Environment:
    def __init__(self):
        self.variables_dict = dict()
        self.directory = os.getcwd()

    def find_var(self, key):
        return self.variables_dict.get(key)

    def push_var(self, key, value):
        self.variables_dict[key] = value

    def get_cwd(self):
        return str(self.directory)

    def set_cwd(self):
        self.directory = os.getcwd()

