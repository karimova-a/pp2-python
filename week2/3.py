print("--1--lists")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


print("--2--access list items")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


print("--3--change items")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


print("--4--add items")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
thislist.insert(1, "orange")
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


print("--5--remove items")
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


print("--6--loop lists")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


print("--7--list comperhension")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


print("--8--sort lists")
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


print("--9--copy lists")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
#mylist = list(thislist)
#mylist = thislist[:]
print(mylist)


print("--10--join lists")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
#for x in list2:
#  list1.append(x)
#list1.extend(list2)
print(list3)


print("--11--methods")
'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''


