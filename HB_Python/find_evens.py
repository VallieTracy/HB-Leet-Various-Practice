my_list = [1, 3, 5]

def evens(some_param):
    evens_list = []

    for i in range(len(some_param)):
        if ((some_param[i])%2 == 0):
            evens_list.append(i)

    return(evens_list)

print(evens(my_list))