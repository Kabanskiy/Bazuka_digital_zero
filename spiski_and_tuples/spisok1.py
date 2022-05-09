a = [100, 500, 'vasya', 'wowa']

b = [0.22, 0.77, '_26515_sfd']

d = a.copy()

a.append('bazuka')
a.insert(1, 250)
a[0] = 99    #zamena stroki
b.extend(a)
# a.remove(500)
# a.pop()
d = a.copy()
d.append(3)
a.append(2)
a.clear()
print(a)
# print(b)
print(a.count('vasya'))
print(d)



f = [100, 22, 39, 14, 500]
f.reverse()
f.sort(reverse = True)
print(f)