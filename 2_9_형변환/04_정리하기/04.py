a = ('Seoul', 'Paris', 'Paris', 'US')
a = list(a)
a[3: 4] = []
a = tuple(a)
print(a, type(a))
