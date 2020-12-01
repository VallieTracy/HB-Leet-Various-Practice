# my_list = [1, 2, 4, 6]

# def evens(some_param):
#     count = 0
#     for param in some_param:
#         if param % 2 == 0:
#             count += 1
#     return count

# out = evens(my_list)
# print(f"'my_list' contains {out} even numbers.")

# my_list = []

# def big_diff(some_param):
#     if len(some_param) >= 1:
#         lg = max(some_param)
#         sm = min(some_param)
#         return lg - sm
#     else:
#         print("empty list")

# print(big_diff(my_list))

my_list = [1, 2, 4, 5, 5, 6]
# others = []
# sm = min(my_list)
# lg = max(my_list)
# for i in range(len(my_list)):
#     if my_list[i] != lg and my_list[i] != sm:
#         others.append(my_list[i])

# print(others)

def centered_average(param):
    others = []
    sm = min(param)
    lg = max(param)

    for i in range(len(param)):
        if param[i] != sm and param[i] != lg and not param[i] in others:
            others.append(param[i])
   
    for j in range(len(others)):
        average = sum(others) / len(others)

    return average

print(centered_average(my_list))



