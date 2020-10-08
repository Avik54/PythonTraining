# keys
keys = ['a', 'b', 'c', 'd', 'e']
# values
values = [1, 2, 3, 4, 5]

# creating a dict from the above lists
dictValue = {key: value for (key, value) in zip(keys, values)}

# printing the dictionary
print(dictValue)