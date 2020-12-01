print("Let's begin...")

def add_numbers(numbers):
    total = 0
    for number in numbers:
        total += number

    return total

print(add_numbers([1, 3, 10]))

def double_it(number):
    return number * 2

print(double_it(70))

def equation(number):
    return (4*number) - 1
print(equation(4))

def plus_one(number):
    return number + 1
print(plus_one(7))

# def average(numbers):
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         total += number
#     return total / length


# Test your function with the following:
#print(average([1, 5, 9]))
#print(average(range(11)))


