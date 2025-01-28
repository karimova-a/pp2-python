print("--1--dictionary")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["brand"])
print(len(thisdict))
#thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


print("--2--access items")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#x = thisdict.get("model")
#x = thisdict.keys()
#x = thisdict.values()
#x = thisdict.items()
print(x)


print("--3--change items")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#thisdict.update({"year": 2020})
print(thisdict)


print("--4--add items")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
#thisdict.update({"color": "red"})
print(thisdict)


print("--5--remove items")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
#thisdict.popitem() #last item
#del thisdict["model"]
#thisdict.clear() = del thisdict
print(thisdict)


print("--6--loop dictionary")
for x in thisdict:
  print(x) 
#for x in thisdict.keys():
#  print(x)
for x in thisdict:
  print(thisdict[x])
#for x in thisdict.values():
#  print(x)
for x, y in thisdict.items():
  print(x, y)


print("--7--copy")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
#mydict = dict(thisdict)
print(mydict)


print("--8--nested dicyionaries")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


#print("--9--methods")
'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''