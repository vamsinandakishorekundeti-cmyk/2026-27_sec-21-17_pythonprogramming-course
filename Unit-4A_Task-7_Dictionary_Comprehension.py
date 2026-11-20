# Example solution: dictionary comprehension
squares = {x: x * x for x in range(1, 6)}
print("Squares dict:", squares)

even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print("Even squares:", even_squares)