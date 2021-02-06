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
