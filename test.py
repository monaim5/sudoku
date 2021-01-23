a = (1, 2, 3)
b = (1, 2, 3)
c = (1, 2, 3)
d = (4, 2, 3)

print(a is b)
print(id(a))
print(id(b))

a = None
b = None
a = 6
print(a is b)
print(id(a))
print(id(b))

print(a)
print(b)