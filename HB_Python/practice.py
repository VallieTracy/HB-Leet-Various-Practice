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

# # # testing_stores = choose_2_stores(grocery_stores1, grocery_stores2)
# # # print(testing_stores[0])
# caboodle = choose_2_stores(grocery_stores1, grocery_stores2)
# print(f"CABOODLE: {caboodle}")
# print(type(caboodle))
# s1 = caboodle[0]
# s1l1 = s1[0]
# print(f"S1L1: {s1l1}")
# s2 = caboodle[1]
# s2l1 = s2[0]
# print(f"S2L1: {s2l1}")

# some_letters = 'lunds & byerlys'
# more_letters = 'aldi'
# user_choice = 'unds and byerlys'

# groc_letters = some_letters + more_letters
# groc_letters = groc_letters.replace('&','').replace("'", '').lower()
# if user_choice in groc_letters:
#     print(f"I think you meant either {some_letters} or {more_letters}.\nPlease verify by typing it again below.")
# else:
#     print("That grocery store isn't in the list.  Try again...")

# def wrong_input(user_choice): WORKS
#     groc_letters = 'ubundsyer'
#     portions_list = []
#     for i in range(len(groc_letters)-1):
#         portion = groc_letters[i] + groc_letters[i+1]
#         portions_list.append(portion)
  
#     if user_choice in portions_list:
#         print(f"I think you meant either {s1} or {s2}.\nPlease verify by typing it again below.")
#     else:
#       print("That grocery store isn't in the list.  Try again...")

# def wrong_input(user_choice, some_words, more_words): WORKS
#     groc_letters = some_words + more_words
#     groc_letters = groc_letters.replace(' ','').replace('&','').replace("'", '').lower()
#     if user_choice in groc_letters:
#         print(f"I think you meant either {some_words} or {more_words}.\nPlease verify by typing it again below.")
#     else:
#       print("That grocery store isn't in the list.  Try again...")


# def generic_error(question, dtype, y, z):
#     print(question)
#     while True:
        
#         try:
#             user_choice = dtype(input(">> ").replace(y,z))
#             print(type(user_choice))
#             break
#         except:
#             print("Sorry, just enter a number")
#             pass

# question1 = 'QUESTION1'
# r = ''
# s = ''

# generic_error(question1, float, r, s)

import random
import time
from random import choice

# print("Here's what we're bringing to the party and the cost breakdown:")
# for key in groceries:
#     print(f"{key}: ${groceries[key]}")



# while i < 3:
#     while True:
#         try:
#             ability = input(">> ").lower()
#             if ability.startswith('n'):
#                 if i == 3:
#                     print("well whatever, all you need to know is...")
#                 print(f"She's the one with {desc[i]}")
#                 print("Do you see her now?")
#                 i = i + 1
            
#         except:
#             print("Her name is Shawniece and she's a reaaal bitch.")
#             break
#     break
print("Are you ready to go?")
while True:   
    a1 = input(">> ").lower()
    print("*")

    if a1.startswith('y'):
        print("Cool, let's go.")
        break
    elif a1.startswith('n'):
        print("No?")
        time.sleep(1)
        print("Too bad, you're a hotdog.  We're leaving.")
        break
    else:
        print("I didn't understand your response.  Please type yes or no.")
        try:
            a1 = input(">> ").lower()
            break
        except:
            want = 'yn'
            if a1 in want:
                print("1 of 2 test print statements")
            else:
                print("Nope, Try again...")

  