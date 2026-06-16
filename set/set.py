s1 = {"wjegdyf", 1, 2, 3}
print(s1)
s1.add("gerdws")
print(s1)
s2 = {4, 5, 6, 7}
s1.update(s2)
print(s1)
s1.remove(1)
print(s1)
#.remove() raises an error if item does not belong to set
try:
    s1.remove(1)
except:
    print("Already removed")
#discard does not
s1.discard(1)
#.pop() removes arbitrary element and returns it
x = s1.pop()
print(x)
#.pop() throws error if we try to remove element from an empty set
empty_set = set(())
try:
    y = empty_set.pop()
except:
    print("Already empty")
#.clear() removes all elements
s1.clear()
print(s1)
#set operations
a = {1,2,3}
b = {3,4,5}
#union
print(a.union(b))
print(a | b)
#intersection
print(a.intersection(b))
print(a & b)
#defference
print(a.difference(b))
print(a - b)
#symmetric difference
print(a.symmetric_difference(b))
print(a ^ b)
#if we add _update to method name other than union it modifies a instead of creating new set
#we can also use assignment operators &=, -=, and ^=
x = {1,2,3}
print(x)
x.difference_update({1,2})
print(x)
#for union to work in place we replace it with update, not union_update
#we can also use assignment operator |=
x.update({1,2})
print(x)
#we can copy set with .copy()
#we can compare set with .issubset() (or <=), .issuperset() (or >=), (< and > for being a proper (sub/super)-set)
#if we don't want to allow adding and removing elements we can use frozenset instead of set
#it supports all set methods that do not modify it

