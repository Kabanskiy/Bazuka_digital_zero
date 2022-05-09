a = {1, 2, 'bazuka', 'zdarova'}

a.add('terminator')
print(a)
a.remove('zdarova')
print(a)

# print(a.clear())

b = {7, 9, 4, 5, 8}
c = {6, 3, 1, 2}
print(a.isdisjoint(b))
print(c.union(b))
print(a|c)
print(a&c)
print(c-a)

r = frozenset([1, 2, 4, 'sdf'])
print(type(r))