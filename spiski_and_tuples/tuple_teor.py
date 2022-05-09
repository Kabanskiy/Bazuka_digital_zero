# a = ()
# b = tuple([1, 2, 3, 4, 5])
# print(b)

a = ('terminator', 'bazuka', ['fox', 'pastagoy'])
b = (1, 2, 3, 4, 5)
a[2][0] = 'zhidkiy'
c = a + b
print(a)
print(b.count(2))
print(len(a))
print(min(b), max(b), sum(b))