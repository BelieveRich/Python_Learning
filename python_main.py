# First hello_world python project
# Author: Richard

# Note: yes, no need semi-colon needed!
# Note: increment(++, --) does not work
# Note: Indentation replaces the brackets
print("Hello_World!")

# see if \n still works as LF, Note: yes still works :)
print("What is your name\n?")

# std::cin() is input() in python
name = input()

print("Nice to meet ya, ", name)

# Python has 3 common data-types: Int, Float, String  (No double/long etc)
# Note: no need to put explicit data type as C/C++, just declare variable name = value, then python will auto map it!
int_val1   = 99
float_val1 = 3939889.5
string_val1 = "A_day_after_Christmas"
string_val2 = "This is a multiple   \
                Line string with a  \
                lot of newline.     \
                \\ works well"
print("int_val1 = ", int_val1, "\nfloat_val1 = ", float_val1, "\nstring_val1 = ", string_val1)
print("type = ", type(int_val1))     # type =  <class 'int'>
print("type = ", type(float_val1))   # type =  <class 'float'>
print("type = ", type(string_val1))  # type =  <class 'str'>

#########################
#  String manipulation  #
#########################
print("string_val2 = ", string_val2)
string_val3 = "I love " + "Christmas eve"
string_val4 = " and new year as well"
string_val5 = string_val3 + string_val4
print("string_val5 = ", string_val5)
print("string_val3 + string_val4 = ", string_val3 + string_val4)
# Len() function will show the lenth of a string/array/sequence
print("Len(string_val3 + string_val4) = ", len(string_val3 + string_val4))

# below will throw an error: TypeError: can only concatenate str (not "int") to str
# print("string_val3 + int_val1 = ", string_val3 + int_val1)

# string replication: using "*" to output same string multiple times
print("I love steak * 5\n" * 5)

#########################
#     Math Operators    #
#########################
# + - * /, %, 
# Note: Different ones from C/C++ are: **(Exponetial power), // integer division
print("5 ** 2 = ", 5 ** 2, " 6 ** 2 = ", 6 ** 2 )
print("37 // 5 = ", 37 // 5, "\n99 // 2 = ", 99 // 2)
print("37 % 5 = ", 37 % 5)

#########################
#        Strings        #
#########################
# my_string[3]
# my_string[4:9]
# my_string.upper()
# my_string.lower()
# my_string.count()
# my_string.replace()  
# my_string.strip()    - strip white space

# 3 common containers are: list, dictionaries, tuples

#########################
#         List          #
#########################
# [Lists] specify an ordered sequence of elements. Data are mutable(String is not as they are being copied when modified), 
# each element is called an Item and placed between square brackets
# new_list = []
# index(), count(), append(), remove(), del(), reverse(), extend(), pop(), insert(), sort()
my_list = [1,2,3]
my_list2 = ["a", "b", "c"]
my_list3 = ['x', 'y', 'z']
my_list4 = ["hello", "2day", "is", 12, 24, 2020, "Christmas eve"]
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# Append(), can only take 1 argument
my_list2.append("d")
# ['a', 'b', 'c', 'd']
print(my_list2)
my_list2a = ["e", "f", "g"]
my_list2.append(my_list2a)
# ['a', 'b', 'c', 'd', ['e', 'f', 'g']], this a nested list
print(my_list2)

# += also can append
my_list2 += [0000, 1111]
print("my_list2 += [0000, 1111] = ", my_list2)

# Insert(), put object at arg1 - 1 location. arg1: index, arg2: object
my_list3.insert(0, ["u", "v", "w"])
print(my_list3)
my_list3.insert(len(my_list3), ["1", "2", "3"])
print(my_list3)

# remove(), pop(), del()
my_list3.remove("x");
print("remove(x) = ", my_list3)
my_list3.pop()   # Pop_back last value
print("pop() = ", my_list3)
my_list3.pop(0)  # pop first value
print("pop(0) = ", my_list3)
del my_list3     # remove whole list and object gone
my_list3 = ["u", "v", "w"]   # revive list3

# combine two lists
print("\n\nmy_list = ", my_list)
print("my_list2 = ", my_list2)
print("my_list3 = ", my_list3)
print("my_list4 = ", my_list4)
my_list2 = my_list2 + my_list
print("my_list2 + my_list =", my_list2)

# nest list
my_list5 = [my_list, my_list]
print("Nested list [my_list, my_list] = ", my_list5)

# clear, my_list5 = []
my_list5.clear()
print("m_list5.clear() = ", my_list5)

# sort()
my_list_int = [20, 30, 4, 99, 8, 70, 10, 3]
print("my_list_int pre sort() = ", my_list_int)
my_list_int.sort()
print("my_list_int.sort() = ", my_list_int)

# slice a list, show a partial list
# [3, 4, 8, 10]
# my_list[1:3]   - Select items 1 ~ 2
# my_list[-3]    - Select items 3rd from last
# my_list[1:]    - Select items from index 1 to last
# my_list[:3]    - Select items from 0 to 2
# my_list[:]     - select whole list
# my_list[1][:2]  - select sub list 1 item 0 & 1
print("my_list_int[0:4]", my_list_int[0:4])

# loop thru list
for x in range(1,4):
    my_list_int[x] = ["fruit"] # replace [1] - [3] = "fruit"
    print(my_list_int)

# list copy
my_list_int2 = my_list_int
print("Copied my_list_int2 = ", my_list_int2)

# List comprehension
# list_variable = [x for x in iterable]


#########################
#         Tuples        #
#########################
# Tuples are similar to lists, they can display an ordered sequence of elements
# - Immutable(Can't change the values)
# - Faster access
# new_tuple = ()

my_tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

print("my_tuples1 = ", my_tuple1)

# slide tuples
print("my_tuples[1:11:2]", my_tuple1[1:11:2]) # (1,3,5,7,9)
print("my_tuples[1:11:3]", my_tuple1[1:11:3]) # (1,4,7,10)

print("my_tuples[0:11:2]", my_tuple1[0:11:2]) # (0,2,4,6,8,10)
print("my_tuples[0:11:3]", my_tuple1[0:11:3]) # (0,3,6,9)

# to change tuple value, you will need to cast tuples to a list, then modify, and cast back to tuple
my_tuples_list = list(my_tuple1)
my_tuples_list[0] = 99
my_tuples_list[1] = 99
my_tuples_list[2] = 99
my_tuple1 = tuple(my_tuples_list)
print("modified tuples = ", my_tuple1)   #(99, 99, 99, 3, 4, 5, 6, 7, 8, 9, 10, 11)

#########################
#     Dictionaries      #
#########################
# Dictionary holds indexes with keys/values. The key-value pairs are mutable.
# new_dict = {}
# dict.keys(), values(), items() 

my_dict1 = {"username":"Richard", "online":"false", "friends":500}
new_dict = {}
other_dict = dict()

print("my_dict = ", my_dict1)
print("new_dict = ", new_dict)
print("other_dict = ", other_dict)

new_dict = {
    "field1": "This is a new dictionary!",
    "Name": "Johnny Walker",
    "Age":35
}

print("new_dict(modified) = ", new_dict)
print("new_dict[field1] = ", new_dict["field1"], "\nnew_dict[Name] = ", new_dict["Name"], \
      "\nnew_dict[Age] = ", new_dict["Age"])

print("dict.keys() = ", new_dict.keys())
print("dict.values() = ", new_dict.values())
print("dict.items() = ", new_dict.items())

# Modify values via keys
new_dict["Age"] = 35+1 # Increase age by 1
new_dict["Name"] = new_dict["Name"] + " Jr."  # Append name by Jr.

print("dict.items() new = \n", new_dict.items())

# Loop thru to print
# 1. Print all the keys
print("Print Keys:")
for x in new_dict:
    print(x)

# 2. Print all the values
print("\nPrint Values:")
for x in new_dict:
    print(new_dict[x])

# 3. Print both key & value pair
print("\nPrint Keys + Values:")
for x, y in new_dict.items():
    print(x," = ", y)


#############################
#   Conditional Statement   #
##############################
print("\n\nConditional statement:")
a = 45
b = 45
if b > a:
    print("b > a")
elif a ==b:
    print("a == b")
else:
    print("a > b")


# If-Not-Statement
new_list1 = [1, 2, 3, 4]
x = 10
if x not in new_list1:
    print("x is not in the new_list1")

# can use pass to statememt for empty if statement
a = 33
b = 200

if b > a:
    pass

#############################
#      Loops Statement      #
#############################
# can look thru LTDS(List\Tuples\Dictionary\String)
print("Loop string:")
for x in "Qualcomm":
    print(x)

print("\nLoop list:")
new_list2 = ["q", "u", "a", "l", "c", "o", "m", "m", "123"]
for x in new_list2:
    print(x)

print("\nLoop tuples:")
new_tuples2 = (new_list2, "q", "u", "a", "tuples", "456")
for x in new_tuples2:
    print(x)

print("\nLoop dictionaries:")
new_dict2 = {"slogan1":"YOLO!", "slogan2":"Viva la Via", "slogan3":3939889.456}
for x,y in new_dict2.items():
    print(x, " = ", y)

# while loops works too
i = 1
while i < 8:
    if i == 4:
        break  # Break early at 4
    print(i)
    i += 1

#############################
#      Class Statement      #
#############################
# Python is an OOP language and every element is an "object" with methods and properties
# Class is the blueprint to creating different objects.
class RCTestClass:
    birthday = "08/10/1985"

# Create an object
print("\n\n\nClass statement:")
rc1_object = RCTestClass()
print((rc1_object.birthday + "\n")* 3) 

# create class per template
class car(object):
    """
    docstring
    """
    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self):
        """
        Driving the car
        """
        return "Car Driving"

rc_car_object = car("yellow", "4 doors", "4 tires")
print("rc_car_object.brake() = ", rc_car_object.brake())
print("rc_car_object.drive() = ", rc_car_object.drive())

#############################
#      Error Statement      #
#############################
"""
1. AttributeError - when an attribute reference or assignment fails
2. IOError - when I/O operation(open() function) fails for an I/O related reason such as file not found or disk full
3. ImportError - comes up when an import statement cannot locate the module definition. Import can't find a name that must be imported
4. IndexError - When a sequence subscript is out of range
5. KeyError - when a dictionary key isn't found in the set
6. KeyboardInterrupt - when user hits the interrupt key(Ctrl+C) or delete
7. NameError - when a local or global name cannot be found
8. OSError - a System related error
9. SyntaxError - when a parser encounters a syntax error
10. TypeError - when an operation or function is applied to an object of inappropriate type
11. ValueError - when a built-in op/function gets an argument that has the right type but in-appropriate value
12. ZeroDivisionError - divide by zero 
"""

my_dict_error1 = {"a":1, "b":2, "c":3}
try:
    value = my_dict_error1["d"]
except KeyError:
    print("key D does not exist!Error!")
except:
    print("Error. Things break :(")
else:
    print("Wow! No error!")