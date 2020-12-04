# Import dependencies
import random

# def convo():
#     print("We need to go to the grocery store.  Do you prefer CUB or Lunds & Byerly's?")
#     store = input("> ")
#     print(f"You chose {store}")
    
#     print("Are you ready to go?")
#     a1 = input(">> ")
#     if a1.startswith('y'):
#         print("You're ready to go.")
#     else:
#         print("You're not ready to go.  Too bad, you're a hotdog.  We're leaving.")

#     print("Do you want to drive?")
#     a2 = input(">> ")
#     if a2.startswith('y'):
#         print("Too bad, I'm driving.")
#     else:
#         print("Good, I wasn't going to let you drive anyway!")

# def driving():
#     miles = []
#     print("Apple sucks, my iPhone died, and bun-mobiles aren't yet standard-equipped with GPS systems. I need you to navigate.")
#     print("How many blocks until we turn left?")
#     a1 = int(input(">> "))
#     miles.append(a1)
#     print("And then how many blocks do we go straight for? ")
#     a2 = int(input(">> "))
#     miles.append(a2)
#     return time(miles)

# def time(distance):
#     total_distance = sum(distance)
#     time_to_store = total_distance * 4
#     return f"We're going a total of {total_distance} miles, which will take us {time_to_store} hours!"


# def groceries_list():
#     groceries = {}
#     shopping = 'no'
#     tab = 0

#     while shopping == 'no':
#         print("What should we add to our basket? ")
#         a1 = input(">> ")
#         groceries[a1] = round(random.uniform(.5, 10.5), 2)
#         new_bill = groceries[a1]
#         tab = tab + new_bill
#         print(f"Tab Total: ${tab}")
#         print("OUR BASKET:")
#         for key in groceries:
#             print(f"{key}: ${groceries[key]}")
#         shopping = input('Are we done shopping? ')
#         if shopping == 'yes':
#             print('Done shopping!')
#             break

def total_bill(some_dictionary):
    tab = 0
    for value in some_dictionary.values():
        tab = tab + value
    return tab


def groceries_list():
    groceries = {}
    shopping = 'no'
    

    while shopping == 'no':
        print("What should we add to our basket? ")
        a1 = input(">> ")
        groceries[a1] = round(random.uniform(.5, 10.5), 2)
        print("TOTAL BILL")
        print(total_bill(groceries))
        
        
        print("OUR BASKET:")
        for key in groceries:
            print(f"{key}: ${groceries[key]}")
        shopping = input('Are we done shopping? ')
        if shopping == 'yes':
            print('Done shopping!')
            break



def total_bill(some_dictionary):
    tab = 0
    for value in some_dictionary.values():
        tab = tab + value
    return tab





    
 
groceries_list()    



 




# def hotdog():
#     conversation
#     print(driving_directions)

# conversation = convo()
# driving_directions = driving()
# hotdog()

# x = round(random.uniform(10.5, 100.5), 2)
# groceries = {}
# groceries['hotdog buns'] = x
# print(groceries)