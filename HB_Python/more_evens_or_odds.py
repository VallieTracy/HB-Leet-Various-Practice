num_list = [1, 2]
# odds_list = []
# evens_list = []

# for i in range(len(num_list)):
        
#     if num_list[i] % 2 == 0:
#         even = num_list[i]
#         evens_list.append(even)
#     else:
#         odd = num_list[i]
#         odds_list.append(odd)
        
# print(evens_list)
# print(odds_list)

# if len(odds_list) > len(evens_list):
#     print("There are more odd numbers.")
# elif len(odds_list) < len(evens_list):
#     print("There are more even numbers!")
# else:
#     print("It's a tie!!!")

def num_count(some_param):
    evens_list = []
    odds_list = []

    for param in some_param:
        if param % 2 == 0:
            evens_list.append(param)
        else:
            odds_list.append(param)

    if len(odds_list) > len(evens_list):
        print("There are more odds numbers.")
    elif len(odds_list) < len(evens_list):
        print("There are more evens!")
    else:
        print("It's a TIE!!!")

num_count(num_list)