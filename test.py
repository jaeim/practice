base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in base.lower():
    base.append(i)
for i in range(10):
    base.append(str(i))
base[62] = '+'
base[63] = '/'
print(base)