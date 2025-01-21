print("variables")
x = 4       # x is of type int
x = "Sally" # x is now of type str
x1 = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x))
print(type(y))


print("variable names")
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)


print("multiple values")
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


print("output variables")
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
x1 = 5
y1 = "John"
print(x1, y1)

print("global variables")
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


