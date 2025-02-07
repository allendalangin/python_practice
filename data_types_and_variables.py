a = 3.10
b = 3.5
c = "Python"

print(type(a), type(b), type(c))
print(a, b)
a, b = b, a
print(a, b)
x = 10
y = "20"
print(x + int(y))
print(str(x) + y)

for i in range(5):
    if  i == 3:
        a += i
        break
print(a)
