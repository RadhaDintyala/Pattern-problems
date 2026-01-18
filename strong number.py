n=int(input("Enter a Number: "))
temp=n
sum=0
while (temp>0):
    a=temp%10
    fact=1
    for i in range(1, a+1):
        fact = fact*i
    sum=sum+fact
    temp=temp//10
if sum==n:
    print("strong number")
else:
    print("not a strong number")
