#lists are basically dynamic arrays under the hood
#list is created by using []
lst1 = [1,2,3,4]
print(lst1)
#we can store various data types in one list
lst2 = [1,2,3,"kjqwfhjhweg"]
print(lst2)
#list is ordered, we can acces element by its index
lst3 = [0,1,2,3,4]
print(lst3[3])
#if we have an iterable object we can create a list out of it using list() constructor
#for example if we want to create list out of tuple
lst4 = list((0,1,2,3,4,5,6,7,8,9))
print(lst4)
#we can check if an object is in a list using in keyword
lst5 = [0,1,2,3]
print(2 in lst5)
#we can insert new item at a specified index with .insert
#all items already in a list with >= indices would move right
lst6 = [0,1,2,3,4,5,6]
print(lst6)
lst6.insert(3, 44)
print(lst6)
#if we want to add an item to the end we can use .append
#if we want to add another list (or other iterable object) to the end we can use .extend
lst7 = [8,9]
lst6.append(7)
print(lst6)
lst6.extend(lst7)
print(lst6)
#extending list with tuple
lst6.extend((10,11,12))
print(lst6)
#we can remove first occurence of a given value with .remove()
lst8 = [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
print(lst8)
lst8.remove(1)
print(lst8)
#if we want to remove specific index we can use .pop()
lst8.pop(3)
print(lst8)
#.pop() without argument removes last element
#.clear() removes all elements
lst8.clear()
print(lst8)
#we can loop through all elements in a list using in keyword
lst9 = [0,1,2,3,4,5,6]
for x in lst9:
    print(x)
#it is shorter than the following
for i in range(len(lst9)):
    print(lst9[i])
#to be even shorter we can use list comprahension
[print(x) for x in lst9]
#but it will create new list, so it it is useless for printing (or maybe interpreter is smart enough to not create if when it is never assigned???),
#but good for exmaple for filtering
lst10 = [x for x in lst9 if x % 2 == 1] #creates new lst10 out of odd elements of lst9
print(lst10)
#we can make a copy of a list with .copy(), list() constructor, or slice [:]
lst11 = [0,1,2,3]
lst12 = lst11.copy()
lst13 = list(lst11)
lst14 = lst11[:]
print(lst11 is not lst12)
print(lst11 is not lst13)
print(lst11 is not lst14)
print(lst12 is not lst13)
print(lst12 is not lst14)
print(lst13 is not lst14)

