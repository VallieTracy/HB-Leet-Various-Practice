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
    



