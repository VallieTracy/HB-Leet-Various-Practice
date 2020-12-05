# Import dependencies
import random
import time

# Introducing the user to their life as a hotdog
def excitement(sent1, sent2, time_lapse):
  attempts = 0
  print(sent1)
  while attempts < 1:
    timer = time_lapse
    while timer > 0:
      print('')
      time.sleep(1)
      timer = timer - 1
    attempts = attempts + 1
  print(sent2)
  print()

opening = "Because it's 2020, guess what..."
closing = "YOU'RE A HOTDOG!"
excitement(opening, closing, 5)

time.sleep(2)

next_line = "On the upside to 2020, you're actually a very charming hotdog."
last_line = "Which means you have lots of friends...\nAND A PARTY TO GO TO!\nYAY!!"
excitement(next_line, last_line, 1)

# Initial conversation
def convo():
    print("We need to go to the grocery store.  Do you prefer CUB or Lunds & Byerly's?")
    store = input("> ")
    print(f"You chose {store}")
    
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

conversation = convo()
driving_directions = driving()
grocery_shopping = groceries_list()
hotdog()

