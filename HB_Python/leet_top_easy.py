my_list = [1, 1, 3, 4]

def no_doubles(numbers):
    new_list = []
    for i in range(len(numbers) - 1):
        if numbers[i+1] != numbers[i]:
            new_list.append(numbers[i+1])
    return new_list

print(no_doubles(my_list))



