n=int(input("Enter a number:"))
fact=1
if(n==0 or n==1):
    print("Factorial is: 1")
else:
    for i in range (1,n+1):
        fact=fact*i
    print("Factorial is:",fact)