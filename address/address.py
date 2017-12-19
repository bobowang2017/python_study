data = [1, 2, 3, 4, 9]
print(id(data))
print(id(data[0]))
print(id(data[1]))
print(id(data[2]))

data[0], data[1] = data[1], data[0]
print(id(data))
print(id(data[0]))
print(id(data[1]))
print(id(data[2]))

print(data)
