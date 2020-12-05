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

my_list = []

def evens(numbers):
    new_list = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            new_list.append(i)

    return new_list

print(evens(my_list))

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

import time

attempts = 0

while attempts < 3:

    timer = 5

    while timer > 0:
        print(timer, "...")
        time.sleep(2)
        timer = timer - 1

    attempts = attempts + 1

print("*** LIFTOFF ***")
    



