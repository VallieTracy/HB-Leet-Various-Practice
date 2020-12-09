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
    groc_letters = groc_letters.replace("&",'').replace("'", '').lower()
    if user_choice in groc_letters:
        print(f"I think you meant either {some_letters} or {more_letters}.\nPlease verify by typing it again below.")
    else:
      print("That grocery store isn't in the list.  Try again...")

def convo(choice_1, choice_2):
    '''A function that talks with the user based on user input'''

    # Ask question in order to get input below, then a while loop
    print(f"We need to go to the grocery store before we head over to the party.  Do you prefer {s1.title()} or {s2.title()}?")

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
            print("Driving a bun-mobile is like riding a bike.  Once you learn, you never forget. But I don't have time to teach you today.")
            break
        elif a2.startswith('n'):
            time.sleep(1)
            print("You're missing out--it's a stick shift!  There aren't enough of those these days...")
            break
        else:
            print("Your response isn't a variation of yes or no that I understand.\nPlease try again:")
    
    return store

def driving():
    '''Make a list of miles traveled along the route'''    
    
    
    # Empty list to store user input for miles traveled
    miles = []

    # List of driving directions questions to get input from user
    drive_questions = ['How many blocks until we turn left?',
                       'And then how many blocks do we go straight for?']
    
    # Get user input to append empty miles list
    for i in range(len(drive_questions)):
        print(drive_questions[i])
        print()
        while True:
            try:
                answer = int(input(">> "))
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


def hotdog():
    excitement(0, opening, closing, 5, period, 2)
    excitement(0, next_line, last_line, 4, space, 2)
    convo(s1l1, s2l1)
    excitement(3, e, f, 2, space, 2)
    driving()

# Initial variables to be used in excitement function, welcoming the user
opening = "Because it's 2020, guess what..."
closing = "YOU'RE A HOTDOG!"
period = '...'
next_line = "On the upside to 2020, you're actually a very charming hotdog."
last_line = "Which means you have lots of friends...\nAND A PARTY TO GO TO!\nYAY!!"
space = ''

# Variables to store lists of various grocery stores
stores_list1 = ['Cub Foods', 'Walmart', "Costco"]
stores_list2 = ['Whole Foods', "Lunds & Byerlys", 'Kowalskis']

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

hotdog()

