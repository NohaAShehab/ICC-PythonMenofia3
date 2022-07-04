# class Test(object):
#     pass
#
#
# t = Test()
#
# ## classes in python ===> inherits from object

l = [5, 6, 6, 5]
print(len(l))


# magic methods
class Employee:
    def __init__(self, name, salary):
        self.name = name  #
        # self.__salary = salary  # object property
        self.salary = salary

    ## override magic method
    def __str__(self):  # must return string
        return self.name

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary})"

    def __len__(self):  ## must return with integer
        return len(self.__dict__)

    def __call__(self, *args, **kwargs):
        print("object called ")


e = Employee("noha", 1000)
print(e)
## debug code
print(e.__dict__)
print(e.__repr__())
print(len(e))
print(e.__len__())
# ##########3
e(4, 5, name="ahmed")  # calling the object
