thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1943,
    "year": 2021,
    "electric": False,
    "color": ["red", "White", "blue"]
}

# print(thisdict)
# print(thisdict["brand"])
# print(len(thisdict))
# print(type(thisdict))

# Get the value of the "model" key:
x = thisdict.get("model")
print(x)

#Get a list of the keys:
keys = thisdict.keys()
print(keys) #befor the change

# Add a new item to the original dictionary, and see that the value list gets updated as well:
thisdict["name"] = "Abu Daud"
print(keys)

# Get a list of the values:
val = thisdict.values()
print(val)

# Add a new item to the original dictionary, and see that the keys list gets updated as well
thisdict['name'] = "Abu Daud Hossain Sumon"
print(val)

# use items method
val = thisdict.items()
print(val)

if "model" in thisdict:
    print("Yes, 'model' is onr of the key in the thisdict dictionry")

if "price" in thisdict:
    print("Yes, 'price' is one of the key in the thisdict dictionry")

else:
    print("No, 'Price' is not the key in the thisdict dictionry")

# Removing Items
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item
thisdict.popitem()
print(val)

# The del keyword removes the item with the specified key name
del thisdict["color"]
print(val)
print("delete color key")
# The del keyword can also delete the dictionary completely
# del thisdict

# The clear() method empties the dictionary
thisdict.clear()
print(thisdict)