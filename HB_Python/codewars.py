# password = "lakshdf  a;lsk a;oi q2390847..??/1"

# def maskify(str):
#     lst = list(str)
#     if len(lst) > 4:
#         last_four = lst[len(lst)-4:]
#         for i in range(0, len(lst)-4):
#             lst[i] = "#"
#         output = ''.join(lst) 
#         return output
#     else:
#         return str       


# print(maskify(password))

def get_count(input_str):
    num_vowels = 0
    vowels = 'aeiou'
    for i in range(len(input_str)):
        if input_str[i] in vowels:
            num_vowels += 1
    
    return num_vowels

print(get_count("hi vallie ee"))