num = int(input("Enter a number: "))

if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else: 
    print("Negative")

a = 3.1

for i in range(5):
    if  i == 3:
        a += i
        break
    print(i)
print(a)

n = 1

while n <= 20:
    if n % 2 == 0:
        print(n)
    n += 1