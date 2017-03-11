sample = [1, ["another", "list"], ("a", "tuple")]
mylist = ["List item 1", 2, 3.14]
mylist[0] = "List item 1 again" # We're changing the item.
mylist[-1] = 3.21 # Here, we refer to the last item.
mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
mydict["pi"] = 3.15 # This is how you change dictionary values.
mytuple = (1, 2, 3)
myfunction = len
print(myfunction(mylist))

#####
myfile = open(r"C:\\text.txt", "w")
myfile.write("This is a sample string")
myfile.close()

myfile = open(r"C:\\text.txt")
print(myfile.read())
'This is a sample string'
myfile.close()

#####
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
print([x * y for x in lst1 for y in lst2])
#[3, 4, 5, 6, 8, 10, 9, 12, 15]
print([x for x in lst1 if 4 > x > 1])
#[2, 3]
# Check if a condition is true for any items.
# "any" returns true if any item in the list is true.
any([i % 3 for i in [3, 3, 4, 4, 3]])
#True
# This is because 4 % 3 = 1, and 1 is true, so any()
# returns True.

# Check for how many items a condition is true.
sum(1 for i in [3, 3, 4, 4, 3] if i == 4)
#2
del lst1[0]
print(lst1)
#[2, 3]
del lst1

#####
number = 5

def myfunc():
    # This will print 5.
    print(number)

def anotherfunc():
    # This raises an exception because the variable has not
    # been bound before printing. Python knows that it an
    # object will be bound to it later and creates a new, local
    # object instead of accessing the global one.
    print(number)
    number = 3

def yetanotherfunc():
    global number
    # This will correctly change the global.
    number = 3

#####
class MyClass(object):
    common = 10
    def __init__(self):
        self.myvariable = 3
    def myfunction(self, arg1, arg2):
        return self.myvariable

    # This is the class instantiation
classinstance = MyClass()
classinstance.myfunction(1, 2)

# This class inherits from MyClass. The example
# class above inherits from "object", which makes
# it what's called a "new-style class".
# Multiple inheritance is declared as:
# class OtherClass(MyClass1, MyClass2, MyClassN)
class OtherClass(MyClass):
    # The "self" argument is passed automatically
    # and refers to the class instance, so you can set
    # instance variables as above, but from inside the class.
    def __init__(self, arg1):
        self.myvariable = 3
        print(arg1)

classinstance = OtherClass("hello")
#hello