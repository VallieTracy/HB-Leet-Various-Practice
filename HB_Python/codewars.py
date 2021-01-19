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

# def count_sheep(n):
#     repeat = " sheep..."
#     sheep_list = "" 
#     return f"{n}{repeat}{n-1}{repeat}{n-2}{repeat}"

# print(count_sheep(5))

# def sheep_test(n):
#     sleep = ""
#     sheep_list = []
#     for i in range(1, n+1):
#         sheep_list.append(f"{i} sheep...")
#     return sleep.join(sheep_list)

# print(sheep_test(3))


# param = input("What is your profession? ")

# def get_drink_by_profession(param):
#     param = param.lower()
#     if param == 'jabroni':
#         return "Patron Tequila"
#     elif param == 'school counselor':
#         return "Anything with Alcohol"
#     elif param == 'programmer':
#         return "Hipster Craft Beer"
#     elif param == "bike gang member":
#         return "Moonshine"
#     elif param == 'politician':
#         return "Your tax dollars"
#     elif param == 'rapper':
#         return "Cristal"
#     else:
#         return "Beer"

# print(get_drink_by_profession(param))

# def cube_sum(n, m):
#     init = min(n, m)
#     end = max(n, m)
#     num_list = list(range(init+1, end+1))
#     sum = 0
#     for number in num_list:
#         cube = number**3
#         sum = sum + cube
#     return sum

# print(cube_sum(1, 2))

# def digital_root(n):
#     #digits = [int(x) for x in str(n)]
#     digits = [int(digit) for digit in str(n)]
#     return digits

    

# print(digital_root(123))

# def is_square(n):
#     if n < 0:
#         return False 
    
#     i = 0
#     while i <= n:
#         if i**2 == n:
#             return True
#             break
#         else:
#             if i == n-1:
#                 if i**2 != n:
#                     return False
#             i += 1

# def is_square(n):
#     if n >= 0:
#         return n**.5 == int(n**.5)
#     else:
#         return False

# print(is_square(-10))

# my_nums = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"


# def high_and_low(numbers):
#     num_array = numbers.split()
#     str_int = [int(i) for i in num_array]
#     sml = min(str_int)
#     bg = max(str_int)
#     return f'"{bg} {sml}"'
    

# print(high_and_low(my_nums))

my_names = [ {'name': 'Bart'}, {'name': 'Lisa'} ]#, {'name': 'Maggie'} ]
print(len(my_names))

# def namelist(names):
#     names_list = []
#     names_string = ""

#     for name_dict in my_names:
#         for name in name_dict:
#             names_list.append(f"{name_dict[name]}, ")
#     return names_string.join(names_list)

# print(namelist(my_names))

def nameslist(names):
    for key, value in names:
        print(f"KEY: {key}, VALUE: {value}")

nameslist(my_names)












