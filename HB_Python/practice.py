# my_list = [1, 4, 3, 1]

# def sum(numbers):
#     total = 0

#     for i in range(len(numbers)):
#         total = total + numbers[i]
#     return total

# final = sum(my_list)
# print(final)

# my_list = ['elephant', 'coffee', 'bug', 'emu']

# def vowel_words(words):
#     vowels = 'aeiou'
#     vowels_list = []
#     for word in words:
#         if word[0] in vowels:
#             vowels_list.append(word)
#     return vowels_list

# new_words = vowel_words(my_list)
# print(f"All the words that start with vowels: {new_words}")

# my_list = []

# def evens(numbers):
#     new_list = []
#     for i in range(len(numbers)):
#         if numbers[i] % 2 == 0:
#             new_list.append(i)

#     return new_list

# print(evens(my_list))

#Write a function that takes a list of letters as an arg
#The function should return a list, with the same items in the same order
#but with any vowels appearing as stars *

# ['h', 'e', 'l', 'l', 'o']
#-> ['h', '*', 'l', 'l', '*']

# vowels = 'aeiou'
# my_list = ['h', 'e', 'l', 'l', 'o']

# def remove_vowels(letters):
#     for i in range(len(letters)):
#         if letters[i] in vowels:
#             letters[i] = '*'
#     return letters
        
# print(remove_vowels(my_list))

from random import choice

# groc1 = 'Cub Foods'
# groc2 = "Lunds & Byerly's"
# groc3 = 'Kowalskis'
# groc4 = 'Whole Foods'
# groc5 = 'ALDI'
# groc6 = 'HyVee'

# new_list = (groc1 + groc2).replace(' ','').replace('&','').replace("'", '').lower()
# print(new_list)
# user_input = "unds and Byerly's" 
# print(user_input)
# user_input = user_input.replace(' ','').replace('&','').replace("'", '').lower()
# if user_input in new_list:
#     print(f"new_list: {new_list}")
#     print(f"user_input: {user_input}")
#     print(True)

# grocery_stores1 = ['Whole Foods', "Lunds & Byerly's", 'Kowalskis']
# grocery_stores2 = ['Cub Foods', 'ALDI', 'HyVee']

# def choose_2_stores(list1, list2):
#     first_store = choice(list1)
#     second_store = choice(list2)
#     return first_store, second_store, first_store[0], second_store[0]

# # testing_stores = choose_2_stores(grocery_stores1, grocery_stores2)
# # print(testing_stores[0])
# caboodle = choose_2_stores(grocery_stores1, grocery_stores2)
# print(f"CABOODLE: {caboodle}")
# s1 = caboodle[0]
# s1l1 = s1[0]
# print(f"S1L1: {s1l1}")
# s2 = caboodle[1]
# s2l1 = s2[0]
# print(f"S2L1: {s2l1}")

some_letters = 'lunds & byerlys'
more_letters = 'aldi'
user_choice = 'unds and byerlys'

groc_letters = some_letters + more_letters
groc_letters = groc_letters.replace('&','').replace("'", '').lower()
if user_choice in groc_letters:
    print(f"I think you meant either {some_letters} or {more_letters}.\nPlease verify by typing it again below.")
else:
    print("That grocery store isn't in the list.  Try again...")




