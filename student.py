from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,module):
        self.modules.append(module)
        self.grades[module] = module.get_grade()

    def get_list_modules(self):
        for mod in self.modules:
            print("Modules of Student: %s" % self.name, "\n", (mod))

    def get_grades(self):
        for mod in self.grades:
            print("Modules of Student: %s" % self.name, "\n", mod, self.grades[mod])


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
