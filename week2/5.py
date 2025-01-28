print("--1--sets")
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(len(thisset))
print(type(thisset))
#thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


print("--2--access set items")
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
print("banana" in thisset)


print("--3--add items")
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
#thisset = {"apple", "banana", "cherry"}
#mylist = ["kiwi", "orange"]
#thisset.update(mylist)

print(thisset)


print("--4--remove items")
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
#thisset.discard("banana")
#x = thisset.pop()
#thisset.clear()
#del thisset
print(thisset)


print("--5--loop sets")
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


print("--6--join sets")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # // set3 = set1 | set2
#set1.update(set2)
#set3 = set1.intersection(set2) // set3 = set1 & set2
#set1.intersection_update(set2)
#set3 = set1.difference(set2) // set3 = set1 - set2
#set1.difference_update(set2)
#set3 = set1.symmetric_difference(set2) // set3 = set1 ^ set2
#set1.symmetric_difference_update(set2)
print(set3)


#print("--7--methods")
'''
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
'''