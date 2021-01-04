# my_str = 'moOse'

# def is_isogram(string):
#     string = string.lower()
#     for letter in string:
#         if string.count(letter) > 1:
#             return False
#     return True

# result = is_isogram(my_str)
# print(result)

# my_str = 'kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'

# def printer_error(s):
#     ok = 'abcdefghijklm'
#     count = 0
#     for i in range(len(s)):
#         if s[i] in ok:
#             count +=1
#     d = len(s)
#     errors = d - count
#     return f"{errors}/{d}"

# print(printer_error(my_str))

# my_string = 'xdvFFgoo'

# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')

# print(xo(my_string))

# def quarter_of(month):
#     q1 = range(1, 4)
#     q2 = range(4, 7)
#     q3 = range(7, 10)
#     q4 = range(10, 13)
#     if month in q1:
#         return 1
#     if month in q2:
#         return 2
#     if month in q3:
#         return 3
#     if month in q4:
#         return 4
 
# print(quarter_of(13))

def count_sheep(n):
    repeat = " sheep..."
    return f"{n}{repeat}{n-1}{repeat}{n-2}{repeat}"

print(count_sheep(5))
















