s1 = {"key1" : "value1", "key2" : "value2"}
print(s1)
#dictionaries are ordered in python 3.7+ and unordered in earlier python versions
#it is an dynamic array of objects (to preserve order) + hash map of indices to this array
#we can acces item by its key
print(s1["key1"])
print(s1.get("key1"))
#we can get keys with .keys()
s1_keys = s1.keys()
print(s1_keys)
#it is a view of dictionary keys, so if we modify dictionart, the list changes
s1["key3"] = "value3"
print(s1_keys)
#we can do the same with .values()
#or we can get tuples of key-value pairs with .items()
#we can check if key is in dict with in
if "key1" in s1:
    print(s1["key1"])
#we can add item with .update() or by its key
s1["key4"] = "value4"
s1.update({"key5":"value5"})
print(s1)
#we can remove item with .pop()
s1.pop("key5")
print(s1)
#.popitem() would remove last added item in 3.7+ and arbitrary item in earlier versions
s1.popitem()
print(s1)
#.clear() empties dictionary
s1.clear()
print(s1)
#loopint by keys
s2 = {1:-1, 2:-2, 3:-3}
for x in s2:
    print(x)
#or
for x in s2.keys():
    print(x)
#looping by values
for x in s2.values():
    print(x)
#or
for x in s2:
    y = s2[x]
    print(y)
#looping by items
for x, y in s2.items():
    print(x, ":", y)
#to copy a dictionary use .copy() or dict()
s3 = s2.copy()
s4 = dict(s2)
s5 = s2 #not a copy, it is a reference to the same dict as s2
print(s3 is s2)
print(s4 is s2)
print(s5 is s2)
#The famous question remains: "How to measure dict in bytes?".

