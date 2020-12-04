# word = 'blob'

# def multiply(param):
#     new_word = ''
#     for i in range(len(param)):
#         new_word = new_word + (param[i] * 2)
#     return new_word
    
# print(multiply(word))

# letters = 'hiphip'

# # for i in range(len(letters)-2):
# #     print(letters[i:i+2])

# def count_hi(some_param):
#     count = 0
#     for i in range(len(some_param)-2):
#         if 'hi' in some_param[i:i+2]:
#             count += 1
#     return count

# print(count_hi(letters))

# letters = 'catdogcatdogg'

# def counting_animals(string):
    
#     for i in range(len(string)-2):
#         animal = string[i:i+3]
#         cat_count = 0
#         dog_count = 0
#         if animal == 'cat':
#             cat_count += 1
#         if animal == 'dog':
#             dog_count += 1
#     if cat_count == dog_count:
#         return True
#     else:
#         return False

# print(counting_animals(letters))

# my_string = 'aaacodebbbcodecode'

# def codeword(letters):
#     code_count = 0
    
#     for i in range(len(letters)-3):
#         word = letters[i:i+4]
#         if word == 'code':
#             code_count += 1
#     return code_count

# code_total = codeword(my_string)
# print(f"Total number of times CODE appears: {code_total}!")

# string1 = 'hbdabc'
# string2 = 'abc'

# def ending(a, b):
#     if b.endswith(a) or a.endswith(b):
#         print(True)

# ending(string1, string2)

my_string = 'abxyzz'

def search_xyz(letters):

    if 'xyz' in letters:
        for i in range(len(letters)-2):
            print(letters[i:i+3])


search_xyz(my_string)
