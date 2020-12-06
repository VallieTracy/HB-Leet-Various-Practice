# Import dependencies
import random
import time
from random import choice

# Introducing the user to their life as a hotdog
# def excitement(sent1, sent2, time_lapse):
#   attempts = 0
#   print(sent1)
#   while attempts < 1:
#     timer = time_lapse
#     while timer > 0:
#       print('')
#       time.sleep(1)
#       timer = timer - 1
#     attempts = attempts + 1
#   print(sent2)
#   print()

# opening = "Because it's 2020, guess what..."
# closing = "YOU'RE A HOTDOG!"
# excitement(opening, closing, 3)

# time.sleep(2)

# next_line = "On the upside to 2020, you're actually a very charming hotdog."
# last_line = "Which means you have lots of friends...\nAND A PARTY TO GO TO!\nYAY!!"
# excitement(next_line, last_line, 1)



def choose_2_stores(list1, list2):
    first_store = choice(list1)
    second_store = choice(list2)
    return first_store, second_store, first_store[0], second_store[0]

stores_list1 = ['Cub Foods', 'ALDI', 'HyVee']
stores_list2 = ['Whole Foods', "Lunds & Byerly's", 'Kowalskis']




# def wrong_input(user_choice): WORKS
#     groc_letters = 'ubundsyer'
#     portions_list = []
#     for i in range(len(groc_letters)-1):
#         portion = groc_letters[i] + groc_letters[i+1]
#         portions_list.append(portion)
  
#     if user_choice in portions_list:
#         print(f"I think you meant either {s1} or {s2}.\nPlease verify by typing it again below.")
#     else:
#       print("That grocery store isn't in the list.  Try again...")

# def wrong_input(user_choice, some_words, more_words): WORKS
#     groc_letters = some_words + more_words
#     groc_letters = groc_letters.replace(' ','').replace('&','').replace("'", '').lower()
#     if user_choice in groc_letters:
#         print(f"I think you meant either {some_words} or {more_words}.\nPlease verify by typing it again below.")
#     else:
#       print("That grocery store isn't in the list.  Try again...")

def wrong_input(user_choice, some_letters, more_letters): 
    groc_letters = some_letters + more_letters
    groc_letters = groc_letters.replace('&','').replace("'", '').lower()
    if user_choice in groc_letters:
        print(f"I think you meant either {some_letters} or {more_letters}.\nPlease verify by typing it again below.")
    else:
      print("That grocery store isn't in the list.  Try again...")
                
   
# Initial conversation
def convo():

    print(f"We need to go to the grocery store.  Do you prefer {s1.upper()} or {s2.upper()}?")

    # While loop
    while True:
      store = input("> ").lower()
      
    
      if store.startswith(s1l1.lower()):
        print(f"I shop at {store.title()} too!\nOk, off to {store.title()} we go!")
        
        break
      elif store.startswith(s2l1.lower()):
        print(f"You chose {store.title()}.  You're bougie, I like it.")
        
        break
      else:
        wrong_input(store, s1, s2)
        
        
    
    
    print("Are you ready to go?")
    a1 = input(">> ")
    if a1.startswith('y'):
        print("You're ready to go.")
    else:
        print("You're not ready to go.  Too bad, you're a hotdog.  We're leaving.")

    print("Do you want to drive?")
    a2 = input(">> ")
    if a2.startswith('y'):
        print("Too bad, I'm driving.")
    else:
        print("Good, I wasn't going to let you drive anyway!")

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


caboodle = choose_2_stores(stores_list1, stores_list2)
s1 = caboodle[0]
s2 = caboodle[1]
s1l1 = caboodle[2]
s2l1 = caboodle[3]

conversation = convo()
driving_directions = driving()
grocery_shopping = groceries_list()
hotdog()

