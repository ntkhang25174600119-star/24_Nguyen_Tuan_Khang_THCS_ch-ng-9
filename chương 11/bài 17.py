data = {'a': 10, 'b': 25, 'c': 7, 'd': 25}

max_key = None
max_value = None

for key in data:
    if max_value is None or data[key] > max_value:
        max_value = data[key]
        max_key = key

print("Key có giá trị lớn nhất:", max_key)
print("Giá trị:", max_value)
