# Import dependencies
import random
import time
from random import choice

def excitement(sent1, sent2, time_lapse, symbol, end_lapse):
    '''Adds time delay between sentences'''
    
    attempts = 0
    print()
    print(sent1)
    while attempts < 1:
        timer = time_lapse
        while timer > 0:
            print(symbol)
            time.sleep(1)
            timer = timer - 1
            attempts = attempts + 1
    print(sent2)
    print()
    time.sleep(end_lapse)

def choose_2_stores(list1, list2):
    '''Function that will randomly choose two items from two different lists'''
    '''In addition to returning the two chosen stores, also returns the first letter of each'''
    
    first_store = choice(list1)
    second_store = choice(list2)
    return first_store, second_store, first_store[0], second_store[0]

def wrong_input(user_choice, some_letters, more_letters): 
    '''Combine two strings, check to see if 'user_choice' is in that combination, and then print based on if/else'''
    groc_letters = some_letters + more_letters
    groc_letters = groc_letters.replace('&','').replace("'", '').lower()
    if user_choice in groc_letters:
        print(f"I think you meant either {some_letters} or {more_letters}.\nPlease verify by typing it again below.")
    else:
      print("That grocery store isn't in the list.  Try again...")
                
def convo():
    '''A function that talks with the user based on user input'''

    # Ask question in order to get input below, which is inside a while loop
    print(f"We need to go to the grocery store before we head over to the party.  Do you prefer {s1.title()} or {s2.title()}?")

    # While loop
    while True:
        store = input(">> ").lower()
        print()
            
        if store.startswith(s1l1.lower()):
            # Reset variable in case user inputs correct first letter but then misspells
            store = s1
            print(f"I shop at {store.upper()} too!\nYou'd be surprised at the number of hotdogs that shop there.")
            break
        elif store.startswith(s2l1.lower()):
            # Reset variable in case user inputs correct first letter but then misspells
            store = s2
            print(f"{store.upper()}, huh?  You're bougie, I like it.")
            break
        # if user enters a string not starting with the first letter of either store
        else:
            # call 'wrong_input' function based on 'store' variable created above,
            # and s1 and s2, variables created from 'choose_2_stores' function and stored in 'caboodle' variable
            wrong_input(store, s1, s2)

    # Time delay between print statement based on grocery store choice & 'excitement' function
    time.sleep(2)
    excitement(a + store, b, 1, space, 0)   

    # User input on if they're ready to leave or not    
    a1 = input(">> ")
    print()
    
    if a1.startswith('y'):
        print("Cool, let's go.")
    else:
        print("No?")
        time.sleep(1)
        print("Too bad, you're a hotdog.  We're leaving.")

    # Time delay between 'leaving' statement and 'excitement' function about driving
    time.sleep(2)
    excitement(c, d, 2, space, 0)
    
    a2 = input(">> ")
    print()
    if a2.startswith('y'):
        print("Driving a bun-mobile is like riding a bike.  Once you learn, you never forget. But I don't have time to teach you today.")
    else:
        print("It's super fun, it's a stick shift!  There aren't enough of those these days...")
    

def driving():
    miles = []
    print("Apple sucks, my iPhone died, and bun-mobiles aren't yet standard-equipped with GPS systems. I need you to navigate.")
    print("How many blocks until we turn left?")
    a1 = int(input(">> "))
    miles.append(a1)
    print("And then how many blocks do we go straight for? ")
    a2 = int(input(">> "))
    miles.append(a2)
    print(travel_time(miles))



def travel_time(distance):
    total_distance = sum(distance)
    time_to_store = total_distance * 4
    return f"We're going a total of {total_distance} miles, which will take us {time_to_store} hours!"



def total_bill(some_dictionary):
    # Initial tab of 0
    tab = 0
    
    print("TOTAL TAB:")
    
    for value in some_dictionary.values():
        tab = tab + value
    
    return tab


def groceries_list():
    # Set initial values
    groceries = {}
    shopping = 'no'
    
    # While loop to generate grocery shopping
    while shopping == 'no':
        print("What should we add to our basket? ")

        # Creates the groceries dictionary
        a1 = input(">> ")
        groceries[a1] = round(random.uniform(.5, 10.5), 2)

        # Call total_bill function and store in a variable
        total_tab = total_bill(groceries)
        print(f"${total_tab}")
                
        # Determinant of loop closure
        shopping = input('Are we done shopping? ')
        if shopping == 'yes':
            print("Here's what we're bringing to the party and the cost breakdown:")
            for key in groceries:
                print(f"{key}: ${groceries[key]}")
            print('Done shopping!')
            break

def hotdog():
    conversation
    driving_directions
    grocery_shopping
    print("...THE END...")

# # Variables to be used in 'excitement' function
opening = "Because it's 2020, guess what..."
closing = "YOU'RE A HOTDOG!"
period = '...'
excitement(opening, closing, 5, period, 2)

# # Immediately repeat 'excitement' function with new variables
next_line = "On the upside to 2020, you're actually a very charming hotdog."
last_line = "Which means you have lots of friends...\nAND A PARTY TO GO TO!\nYAY!!"
space = ''
excitement(next_line, last_line, 4, space, 2)

# Variables to store lists of various grocery stores
stores_list1 = ['Cub Foods', 'ALDI', 'HyVee']
stores_list2 = ['Whole Foods', 'Lunds & Byerlys', 'Kowalskis']

# Variables to store what was returned in the 'choose_2_stores' function

# Returns a 4-item tuple: random first store, random second store, first letter of first store, first letter of second store
caboodle = choose_2_stores(stores_list1, stores_list2)
# Rewriting the four items from the above tuple
s1 = caboodle[0]
s2 = caboodle[1]
s1l1 = caboodle[2]
s2l1 = caboodle[3]

# Sentences for 'excitement' function for being ready to leave
a = 'Alright, we gotta head over to '
b = 'Are you ready?'

# Sentences for 'excitement' function for leaving for grocery store
c = "2020 isn't all bad...you get to ride in a bun-mobile today!" 
d = 'Do you want to drive?'

conversation = convo()
driving_directions = driving()
grocery_shopping = groceries_list()
hotdog()



