# Example solution: smallest of three numbers using nested if
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x <= y:
    if x <= z:
        smallest = x
    else:
        smallest = z
else:
    if y <= z:
        smallest = y
    else:
        smallest = z

print(f"Smallest = {smallest} (among {x}, {y}, {z})")
