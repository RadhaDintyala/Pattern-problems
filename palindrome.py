n = int(input("Enter a number: "))
o = n  
rev= 0

while n > 0:
    digit = n % 10
    rev = (rev * 10) + digit
    n = n // 10

if o == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
