data = [7, 6, 9, 8, 5, 10, 3]

for i in range(0, len(data) - 1):
    index = i
    for j in range(i + 1, len(data)):
        if data[j] < data[index]:
            index = j
        data[index], data[i] = data[i], data[index]
print(data)
