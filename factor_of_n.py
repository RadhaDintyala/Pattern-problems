n=int(input("enter the number: "))
print("Factors are:\n")
for i in range(1,n):
    if n%i ==0:
        print(i , end = " ")
