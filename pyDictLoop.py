thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1945
}

#Print all key names in the dictionry, one by one
print("key names:")
for x in thisdict:
    print(x)

print()
# use the key() method
for x in thisdict.keys():
    print(x)
# Print all values in the dictionary, one by one
print()
print()
print("All Values:")
for x in thisdict:
    print(thisdict[x])

print()
# use the values() method
for x in thisdict.values():
    print(x)

print()
# Loop through both keys and values, by using the items() method

for x, y in thisdict.items():
    print(x,y) 