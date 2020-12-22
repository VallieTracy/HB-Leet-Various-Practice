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

# def get_count(input_str):
#     num_vowels = 0
#     vowels = 'aeiou'
#     for i in range(len(input_str)):
#         if input_str[i] in vowels:
#             num_vowels += 1
    
#     return num_vowels

# print(get_count("hi vallie ee"))

# nums = [1,2,6,7,3,6,8,7,1]

# def sum67(numbers):
#     while 6 in numbers:
#         idx6 = numbers.index(6)
#         idx7 = numbers.index(7)
#         del(numbers[idx6:idx7+1])
#     return sum(numbers)

# total = sum67(nums)
# print(f"TOTAL SUM: {total}")

my_list = [1, 3, 2, 2]

def has22(arr):
    for i in range(len(arr)-1):
        while True:
            if arr[i] == 2 and arr[i+1] == 2:
                return True
                break
            else:
                return False
                break

print(has22(my_list))





