# Example solution: list comprehension
numbers = range(1, 11)

squares = [x * x for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)