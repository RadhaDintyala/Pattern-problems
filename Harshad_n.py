n=int(input("Enter a number:"))
temp=n
d_sum=0

while(temp>0):
    d_sum += temp%10
    temp /= 10
if n % d_sum == 0:
    print("Harshad")
else:
    print("Not a Harshad number")
