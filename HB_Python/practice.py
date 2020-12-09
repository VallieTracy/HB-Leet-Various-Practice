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
# print("Are you ready to go?")
# while True:   
#     a1 = input(">> ").lower()
#     print("*")

#     if a1.startswith('y'):
#         print("Cool, let's go.")
#         break
#     elif a1.startswith('n'):
#         print("No?")
#         time.sleep(1)
#         print("Too bad, you're a hotdog.  We're leaving.")
#         break
#     else:
#         print("I didn't understand your response.  Please type yes or no.")
#         try:
#             a1 = input(">> ").lower()
#             break
#         except:
#             want = 'yn'
#             if a1 in want:
#                 print("1 of 2 test print statements")
#             else:
#                 print("Nope, Try again...")

# drive_questions = ['How many blocks until we turn left?',
#                    'And then how many blocks do we go straight for?']
# miles = []
# for i in range(2):
#     print(drive_questions[i])
#     while True:
#         try:
            
#             answer = int(input(">> "))
#             miles.append(answer) 
#             break
#         except:
#             print("Enter a number please")
#             pass              

# def total_bill(some_dictionary):
#     '''Adds values of key:value pair in a dictionary and returns the total'''
#     # Initial tab of 0
#     tab = 0
#     for value in some_dictionary.values():
#         tab = tab + value
#     return tab
  
# # Set initial values
# groceries = {}
# done = 'no'
# print("Before we delve too deep into the shopping and because you're new to the life of a hotdog...")
# print("We're in a bit of a pickle you see.")
# print("Because we're hotdogs, we don't have ears.")
# print("This doesn't mean we can't hear.  It just means we can't hear well.")
# print("So as we shop, I'm going to ask you to confirm every item.")
# print("One of the drawbacks of being a hotdog.")
# print("No big deal though.  You'll just confirm with a simple yes or no!")
# print()
# time.sleep(0)

#**********************WORKS*****************
# While loop to generate grocery shopping
# while done == 'no':
#     print("What should we add to our basket?")
#     # Creates the groceries dictionary
#     a1 = input(">> ")
#     print()
    
#     while True:
#         print(f"Confirm that you meant to tell me {a1} by typing yes or no:")
#         a2 = input(">> ").lower()
#         print()
#         if a2.startswith('y'):
#             print("Adding item to groceries dictionary...")
#             groceries[a1] = round(random.uniform(.5, 10.5), 2)
#             break
#         elif a2.startswith('n'):
#             print("Got it.  Item won't be added!")
#             break
#         else:
#             print("Your response isn't a variation of yes or no that I understand.\nPlease try again:")
            

#     # Call total_bill function and store in a variable
#     total_tab = format(total_bill(groceries), '.2f')
                    
#     # Determinant of loop closure
#     print("Are we done shopping?")
#     done = input(">> ").lower()
#     print()
#     if done.startswith('y'):
#         done = 'yes'
#         time.sleep(1)
#         print(f"Our TOTAL TAB comes to:")
#         print(f"${total_tab}")
#         time.sleep(1)
#         print()
#         break
# print("Would you like to see a list of what we bought and the cost breakdown?")
# receipt = input(">> ").lower()
# if receipt.startswith('y'):
#     print()
#     for key in groceries:
#         print(f"  {key.title()}: ${groceries[key]}")

# descriptions = ['with red hair', 'standing by the pool', 'taking a selfie']
# # Prompting the user for input
# print("Don't look now, but do you see that hotdog over there?")
# # Starting at 0, give user 3 tries to answer 'yes'
# i = 0
# while True:
#     while i < 4:
#         ability = input(">> ").lower()
#         if ability.startswith('n'):
#             if i == 3:
#                 print("Well whatever...all you need to know is that")
#                 break
#             print(f"She's the one {descriptions[i]}.")
#             print("Do you see her now?")
            
#             i = i + 1
            
#         elif ability.startswith('y'):
#             break
#         else:
#             print("I didn't hear you. Say that again?")
#     break

def error_loop(question, ltr_a, print_a, ltr_b, print_b1, print_b2, print_c):
    print(question)
    while True:
        a1 = input(">> ").lower()
        print()

        if a1.startswith(ltr_a.lower()):
            print(print_a)
            break
        elif a1.startswith(ltr_b.lower()):
            print(print_b1)
            time.sleep(1)
            print(print_b2)
            break
        else:
            print(print_c)
 
        
q = 'Do you want to drive?'
a = 'y'
sent_a = 'I do not have time to teach you.  Sorry.'
b = 'n'
sent_b1 = ''
sent_b2 = 'I was not going to let you drive anayway.'
sent_c = 'I do not understand.  Try again.'

error_loop(q,a,sent_a,b, sent_b1,sent_b2,sent_c)
