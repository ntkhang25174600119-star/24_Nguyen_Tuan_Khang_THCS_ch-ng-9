data = {'a': 30, 'b': 60, 'c': 80, 'd': 45}

result = {}

for key in data:
    if data[key] > 50:
        result[key] = data[key]

print(result)
