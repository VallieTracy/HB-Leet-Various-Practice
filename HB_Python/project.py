# Import dependencies
import random
import time
from random import choice
import string

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
    
    groc_letters = (some_letters + more_letters).lower()
    
    if user_choice in groc_letters:
        print(f"I think you meant either {some_letters} or {more_letters}.\nPlease verify by typing it again below.")
    else:
      print("That grocery store isn't in the list.  Try again...")

def convo(choice_1, choice_2):
    '''A function that talks with the user based on user input'''

    # Ask question in order to get input below, then a while loop
    print(f"We need to go to the grocery store before we head over to the party.  Do you prefer {string.capwords(s1)} or {string.capwords(s2)}?")

    # While loop
    while True:
        store = input(">> ").lower()
        print()
            
        if store.startswith(choice_1.lower()):
            # Reset variable in case user inputs correct first letter but then misspells
            store = s1
            print(f"I shop at {store.upper()} too!\nYou'd be surprised at the number of hotdogs that shop there.")
            break
        elif store.startswith(choice_2.lower()):
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
    excitement(2, a, b, 1, space, 0)   

    # User input on if they're ready to leave or not
    while True:   
        a1 = input(">> ").lower()
        print()
    
        if a1.startswith('y'):
            print("Cool, let's go.")
            break
        elif a1.startswith('n'):
            print("No?")
            time.sleep(1)
            print("Too bad, you're a hotdog.  We're leaving.")
            break
        else:
            print("Your response isn't a variation of yes or no that I understand.\nPlease try again:")
            print()
   

    # Time delay between 'leaving' statement and 'excitement' function about driving
    excitement(1, c, d, 2, space, 0)
    
    # Asking user if they'd like to drive
    while True:
        a2 = input(">> ").lower()
        print()
        
        if a2.startswith('y'):
            time.sleep(1)
            print("Driving a bun-mobile is like riding a bike.\nOnce you learn, you never forget.\nBut I don't have time to teach you today.")
            break
        elif a2.startswith('n'):
            time.sleep(1)
            print("Good.  I wasn't going to let you drive anyway.")
            break
        else:
            print("I didn't catch that. Did you want to drive?:")
    
    return store

def driving(an_array):
    '''Make a list of miles traveled along the route'''    
    
    # Empty list to store user input for miles traveled
    miles = []

    # Get user input to append empty miles list
    for i in range(len(an_array)):
        print(an_array[i])
        print()
        while True:
            try:
                answer = int(input(">> ").replace(',', ''))
                miles.append(answer)
                break
            except:
                print("Please try again.  I only understand integers.")
                print()
            pass
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
    return total_time, total_miles


def generic_error(question, dtype, y, z):
    '''Generic error function which takes in input prompt, data type, and items to be replaced'''

    print(question)
    while True:
        try:
            user_choice = dtype(input(">> ").replace(y, z))
            break
        except:
            print("Sorry, just enter a number")
            print()
            pass

def travel_time(distance):
    '''Returns calculations, takes list as argument'''
    total_distance = sum(distance)
    time_to_store = total_distance * 4
    return total_distance, time_to_store

def total_bill(some_dictionary):
    '''Adds values of key:value pair in a dictionary and returns the total'''
    # Initial tab of 0
    tab = 0
    for value in some_dictionary.values():
        tab = tab + value
    return tab

def groceries_list(arr):
    '''Asks for user input and builds a dictionary'''
    '''Also takes an array as an argument; in this case it prints 7 questions with timesleep between each one'''

    for i in range(len(arr)):
        print(arr[i])
        time.sleep(1)
    print()
    time.sleep(6)

    # Set initial values
    groceries = {}
    done = 'no'
    
    # While loop to generate grocery shopping until user input says to stop
    while done == 'no':
        print("What should we add to our basket?")
        # Creates the groceries dictionary
        a1 = input(">> ")
        print()
        
        while True:
            print(f"Confirm that you meant {a1} by typing yes or no:")
            a2 = input(">> ").lower()
            print()
            if a2.startswith('y'):
                groceries[a1] = round(random.uniform(.5, 10.5), 2)
                break
            elif a2.startswith('n'):
                print("Got it.  Item won't be added!")
                break
            else:
                print("Your response isn't a variation of yes or no that I understand.\nPlease try again:")
                print()
        
        # Call total_bill function and store in a variable
        total_tab = format(total_bill(groceries), '.2f')
                        
        # Determinant of loop closure
        print("Are we done shopping?")
        
        while True:
            done = input(">> ").lower()
            print()
            if done.startswith('y'):
                done = 'yes'
                time.sleep(1)
                print(f"Our TOTAL TAB comes to:")
                print(f"${total_tab}")
                time.sleep(1)
                print()
                break
            elif done.startswith('n'):
                done = 'no'
                break
            else:
                print("I didn't understand your answer.\nAre we done shopping?")

    print("Would you like to see a list of what we bought and the cost breakdown?\nPlease only enter yes or no.")
    receipt = input(">> ").lower()
    print()
    if receipt.startswith('y'):
        time.sleep(1)
        print("Our Shopping Receipt")
        print("____________________")
        print()
        for key in groceries:
            print(f"{key.title()}: ${groceries[key]}")
        time.sleep(3)
            
    print()
    print("Alright, let's get outta here. Time to part-ay!") 
    print()
    print()

def party_arrival(desc_list):
    '''---------DESCRIPTION HERE----------------'''

    # Manhandled the function here instead of using the 'excitement' function in order to get it to look they way I want it
    print("-----")
    print("[Segue to party arrival and scanning the crowd]")
    print("-----")
    for i in range(10):
        print('*')
        time.sleep(1)
    
    # Prompting the user for input
    print("Don't look now, but do you see that hotdog over there?")
    # Starting at 0, give user 3 tries to answer 'yes'
    i = 0
    while True:
        while i < 4:
            ability = input(">> ").lower()
            print()
            if ability.startswith('n'):
                if i == 3:
                    print("No worries amigo...all you need to know...")
                    break
                print(f"She's the one {desc_list[i]}.")
                print("Do you see her now?")
                
                i = i + 1
                
            elif ability.startswith('y'):
                break
            else:
                print("I didn't hear you.  Say that again?")
        break

def hotdog():
    excitement(0, opening, closing, 5, period, 2)
    excitement(0, next_line, last_line, 4, space, 2)
    convo(s1l1, s2l1)
    excitement(3, e, f, 2, space, 2)
    driving(drive_questions)
    excitement(4, g, h, 1, space, 1)
    groceries_list(ears)
    party_arrival(descriptions)
    # Final four statements before program ends!
    excitement(2, j, k, 1, space, 2)
    excitement(1, l, m, 4, space, 4)
    excitement(1, n, o, 4, space, 0)

# Initial variables to be used in excitement function, welcoming the user
opening = "Because it's 2020, guess what..."
closing = "YOU'RE A HOTDOG!"
period = '...'
next_line = "On the upside to 2020, you're actually a very charming hotdog."
last_line = "Which means you have lots of friends...\nAND A PARTY TO GO TO!\nYAY!!"
space = ''

# Variables to store lists of various grocery stores
stores_list1 = ['Cub Foods', 'Hyvee', "Costco"]
stores_list2 = ["Jerry's", "Lunds & Byerly's", "Kowalski's"]

# Variables to store what was returned in the 'choose_2_stores' function
# Returns a 4-item tuple: random first store, random second store, first letter of first store, first letter of second store
caboodle = choose_2_stores(stores_list1, stores_list2)
s1 = caboodle[0]
s2 = caboodle[1]
s1l1 = caboodle[2]
s2l1 = caboodle[3]

# Sentences for 'excitement' function:
# ---------
# for being ready to leave
a = "Alright, let's get outta here."
b = 'Are you ready?'

# leaving for grocery store
c = "2020 isn't all bad...you get to ride in a bun-mobile today!" 
d = 'Do you want to drive?'

# navigation
e = "Because you're not driving and bun-mobiles don't yet come standard-equipped with GPS, I need you to navigate."
f = 'The map is in the glove box.'

# grocery shopping
g = "Now that we're at the grocery store, it's time to shop!"
h = ''

# list of statements for 'groceries_list' function to start
ears = ["Before we delve too deep into the shopping and because you're new to the life of a hotdog...",
        "We're in a bit of a pickle you see.",
        "Because we're hotdogs, we don't have ears.",
        "This doesn't mean we can't hear.  It just means we can't hear well.",
        "So as we shop, I'm going to ask you to confirm every item.",
        "One of the drawbacks of being a hotdog.",
        "No big deal though.  You'll just confirm with a simple yes or no!"]

# Variables for generic_error function, guessing time to party
question1 = "Guess how many hours it'll take us to get to the party:"
r = ','
s = ''

# List of driving directions questions to get input from user
drive_questions = ['How many blocks until we turn left?',
                    'And then how many blocks do we go straight for?']

descriptions = ['with red hair', 'standing by the pool', 'taking a selfie']

j = "Her name is Shawniece."
k = "And she's a total bitch."
l = "I'll tell you all about it on the ride home!"
m = "Alright, because we're good little hotdogs and listen to Governor Walz\nLet's put our masks on and party, social-distance style!"
n = "Time to mingle!!!!!"
o = "...THE END..."

hotdog()