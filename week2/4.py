print("--1--tuples")
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
#thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


print("--2--access tuples")
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


print("--3--update")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y.append("orange")
#y = ("orange",)
#thistuple += y
x = tuple(y)
print(x)


print("--4--unpack")
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green) #apple
print(tropic) #['mango', 'papaya', pineapple']
print(red)#cherry


print("--5--loop")
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

'''
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1'''


print("--6--join")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
#mytuple = tuple1 * 2

print(tuple3)


#print("--7--methods")
'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''

