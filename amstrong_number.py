try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer")
    raise SystemExit(1)

total = 0
num = abs(n)
nod = len(str(num))

while num > 0:
    digit = num % 10
    total += digit ** nod
    num //= 10

if total == abs(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
