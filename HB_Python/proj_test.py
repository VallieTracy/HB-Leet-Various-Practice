initial_choice = input("Would you rather be a rain drop or a hotdog? ").lower()
print()
print(f"You want to be a {initial_choice.upper()}!")



# Introductory message based on user choice
def introduction():
    if initial_choice.startswith('r'):
        intro = f"That's awesome, I'm a {initial_choice} too!!"
    if initial_choice.startswith('h'):
        intro = f"You chose to be an {initial_choice}.  That's kind of wierd!  But I like wierd."
    return intro


# Error handling
def error():
    while True:
        if first_letter == 'r':
            try:
                a_2 = int((input("If you had to guess in seconds, how long do you think until we hit the ground? ")).replace(',', ''))
                break
                
            except:
                print(">I'm sorry, I need you to just enter a number.")
                print()
                pass
        else:
            try:
                a_2 = int((input("If you had to guess in seconds? ")).replace(',', ''))
                break
                
            except:
                print(">I'm sorry...")
                print()
                pass

        
# Conversation with the user
def conversation(choice):
    if choice.startswith('r'):
        print("As " + choice + "s, we just fell out of a cloud in Burnsville.")
        a_1 = input("Are you scared, yes or no? ").lower()
        if a_1.startswith('y'):
            print(">I'm actually kind of scared too, I don't like the suburbs!")
        else:
            print(">That's fantastic, you're very brave!")
        print()
        print("...I should tell you...I'm pretty chatty...")
        return error()

    else:
        print("As " + choice + "s, we have a party to go to!")
        a_1 = input("Are you ready to go? ").lower()
        if a_1.startswith('y'):
            print("> Me too!  Alright, you're driving.")
        else:
            print(" What do you need to do in order to get ready?  Honestly, you're a hotdog. We're leaving.")
        print()
        print("Because it's 2020, we're driving in a bun-mobile.")
        

# Call the introduction function
welcome = introduction()
print(welcome)
        

conversation(initial_choice)
print()

# End.  Do you they want to go again or stop...
run = "yes"

while run == "yes":
    print("You've come to the end of your journey.")
    run = input("Do you want to keep going? Type 'yes' or 'no'. ")
    print("-------")
    if run == "yes":
        initial_choice = input("Would you rather be a rain drop or a hotdog? ").lower()
        print(introduction())
    else:
        print("Exiting")
        break
        



        

    
