data = {'a': 1, 'b': 2, 'c': 3}

reversed_dict = {}

for key in data:
    value = data[key]
    reversed_dict[value] = key

print(reversed_dict)
