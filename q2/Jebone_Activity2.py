#Single Inheritance
class Parent:
    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message

    def func1(self):
        print("Parent message:", self.message)


class Child(Parent):
    def func2(self):
        print("This function is in the child class.")
        print("Message received:", self.message)


obj1 = Child("Hello, World!")
obj2 = Child("Welcome to Python!")

obj1.func1()
obj1.func2()

print()

obj2.func1()
obj2.func2()

obj1.set_message("Inheritance is easy!")

print("\nAfter changing the message:")
print("Updated message:", obj1.get_message())
obj1.func2()

#Multilevel Inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    def get_grandfathername(self):
        return self.grandfathername

    def set_grandfathername(self, name):
        self.grandfathername = name


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self.fathername = fathername

    def get_fathername(self):
        return self.fathername

    def set_fathername(self, name):
        self.fathername = name


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        super().__init__(fathername, grandfathername)
        self.sonname = sonname

    def get_sonname(self):
        return self.sonname

    def set_sonname(self, name):
        self.sonname = name

    def print_name(self):
        print("Family Information")
        print("Grandfather name:", self.grandfathername)
        print("Father name:", self.fathername)
        print("Son name:", self.sonname)


s1 = Son("Prince", "Rampal", "Lal Mani")
s2 = Son("Rahul", "Raj", "Mohan")

s1.print_name()

print()

s2.print_name()

s1.set_sonname("Arjun")
s1.set_fathername("Ramesh")
s1.set_grandfathername("Krishna")

print("\nUpdated Family Information")
s1.print_name()

print("\nGetter Methods")
print("Son name:", s1.get_sonname())
print("Father name:", s1.get_fathername())
print("Grandfather name:", s1.get_grandfathername())

#Hierarchical Inheritance
class Parent:
    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message

    def func1(self):
        print("Parent says:", self.message)


class Child1(Parent):
    def func2(self):
        print("Child 1 is learning Python.")


class Child2(Parent):
    def func3(self):
        print("Child 2 is practicing inheritance.")


# Create objects
object1 = Child1("Welcome, students!")
object2 = Child2("Welcome, students!")
object3 = Child1("Keep learning!")

object1.func1()
object1.func2()

print()

object2.func1()
object2.func3()

print()

object3.func1()
object3.func2()

object1.set_message("Inheritance saves time!")

print("\nAfter changing the message:")
print("Updated message:", object1.get_message())
object1.func1()

print("\nSecond object's message:")
object2.func1()


