num = int(input("Enter number of elements in series:"))
f1, f2 = 0, 1
print("Series:", f1, f2, end=" ")
for i in range(2, num):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=" ")


