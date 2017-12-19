a = [0, 1, 2, 3, 4, 5, 6]
i = -len(a)
while i < len(a):
    print('a[' + str(i) + ']=%s' % a[i])
    i += 1

print(a[::-1])
print(a[1:-1])
print(a.count(2))
b = [11, 22, 33]
print(a.extend(b))
print(a)
print(a[::-1])
