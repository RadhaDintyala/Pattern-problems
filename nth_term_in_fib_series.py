num = int(input("Enter number of elements in series:"))
f1, f2 = 0, 1
print("Series:", f1, f2, end=" ")
for i in range(2, num):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=" ")
print("\n")
t=int(input("Enter the term number in the series:"))
if t==1:
    print("\nTerm number",t,"is:",f1)
elif t==2:
    print("\nTerm number",t,"is:",f2)
else:
    for i in range(2,t):
        f3=f1+f2
        f1=f2
        f2=f3
        print("\nTerm number",t,"is:",f3)


