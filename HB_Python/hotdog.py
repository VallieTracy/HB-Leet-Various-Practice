# Import dependencies
import random
import time
from random import choice

def excitement(front_lapse, sent1, sent2, time_lapse, symbol, end_lapse):
    '''Adds time delay between sentences'''
    
    time.sleep(front_lapse)
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

    # Ask question in order to get input below, then a while loop
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

    # Time delay between print statement based on grocery store choice & are you ready 
    excitement(2, a + store, b, 1, space, 0)   

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
    excitement(2, c, d, 2, space, 2)
    
    # Asking user if they'd like to drive
    a2 = input(">> ")
    print()
    if a2.startswith('y'):
        time.sleep(1)
        print("Driving a bun-mobile is like riding a bike.  Once you learn, you never forget. But I don't have time to teach you today.")
    else:
        time.sleep(1)
        print("You're missing out--it's a stick shift!  There aren't enough of those these days...")
    return store

def driving():
    '''Make a list of miles traveled along the route'''    
    excitement(3, e, f, 2, space, 0)
    
    # Empty list to store user input for miles traveled
    miles = []
    
    # Get user input to append empty miles list
    a1 = int(input(">> "))
    miles.append(a1)
    print()
    print("And then how many blocks do we go straight for? ")
    a2 = int(input(">> "))
    miles.append(a2)
    print()
    
    # Variables to store values returned from 'travel_time' function
    total_miles = travel_time(miles)[0]
    total_time = travel_time(miles)[1]
    
    # Calling generic_error function in order to try to ask for user input
    generic_error(question1, float, r, s)
    print()
    print("Nope!")
    print("Fun fact, bun-mobiles can actually only travel 3 miles per hour.")
    print(f"And we traveled {total_miles} miles.")
    print(f"So it's gonna take {total_time} hours. We should have left earlier.")
    

def generic_error(question, dtype, y, z):
    '''Generic error function which takes in input prompt, data type, and items to be replaced'''

    print(question)
    while True:
        try:
            user_choice = dtype(input(">> ").replace(y, z))
            break
        except:
            print("Sorry, just enter a number")
            pass

def travel_time(distance):
    '''Returns calculations, takes list as argument'''
    total_distance = sum(distance)
    time_to_store = total_distance * 4
    return total_distance, time_to_store

def total_bill(some_dictionary):
    # Initial tab of 0
    tab = 0
        
    for value in some_dictionary.values():
        tab = tab + value
    
    return tab

def groceries_list():
    '''Asks for user input and builds a dictionary'''

    excitement(1, g, h, 1, space, 1)

    # Set initial values
    groceries = {}
    shopping = 'no'
    
    # While loop to generate grocery shopping
    while shopping == 'no':
        print("What should we add to our basket?")
        # Creates the groceries dictionary
        a1 = input(">> ")
        print()
        groceries[a1] = round(random.uniform(.5, 10.5), 2)

        # Call total_bill function and store in a variable
        total_tab = format(total_bill(groceries), '.2f')
                        
        # Determinant of loop closure
        shopping = input('Are we done shopping? ')
        if shopping == 'yes':
            print()
            print(f"Our TOTAL TAB:")
            print(f"${total_tab}")
            print()
            break

    print("Would you like to see a list of what we bought and the cost breakdown?")
    receipt = input(">> ").lower()
    if receipt.startswith('y'):
        print()
        for key in groceries:
            print(f"  {key.title()}: ${groceries[key]}")
    
    print("Alright, let's get outta here. Time to part-ay!") # add grocery store here!

def party_arrival():
    excitement(0, j, k, 5, '*', 2)


def hotdog():
    #conversation
    #driving_directions
    grocery_shopping
    arrival
    print("...THE END...")

# Variables to be used in 'excitement' function
opening = "Because it's 2020, guess what..."
closing = "YOU'RE A HOTDOG!"
period = '...'
#excitement(0, opening, closing, 5, period, 2)

# Immediately repeat 'excitement' function with new variables
next_line = "On the upside to 2020, you're actually a very charming hotdog."
last_line = "Which means you have lots of friends...\nAND A PARTY TO GO TO!\nYAY!!"
space = ''
#excitement(0, next_line, last_line, 4, space, 2)

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

# Sentences for 'excitement' function:
# ---------
# for being ready to leave
a = 'Alright, we gotta head over to '
b = 'Are you ready?'

# leaving for grocery store
c = "2020 isn't all bad...you get to ride in a bun-mobile today!" 
d = 'Do you want to drive?'

# navigation
e = "Because you're not driving and bun-mobiles don't yet come standard-equipped with GPS, I need you to navigate."
f = 'How many blocks until we turn left?'

# Storing information from 'convo' function into a variable
# Needs to come above where we declare 'g' variable
#conversation = convo()

# grocery shopping
g = f"Now that we're at the grocery store, it's time to shop!"
h = ''

# party arrival
j = ''
k = 'Do you see that hotdog over there?'

# Variables for generic_error function, guessing time to party
question1 = "Guess how many hours it'll take us to get to the party:"
r = ','
s = ''




#driving_directions = driving()
grocery_shopping = groceries_list()
arrival = party_arrival()

hotdog()



