count=0
n=int(input("Enter a number:"))
while n>0:
    b=n%10
    n=n//10
    count+=1
print("Total digits:",count)