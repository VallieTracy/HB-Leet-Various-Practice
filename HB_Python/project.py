initial_choice = input("Would you rather be a rain drop or a hotdog? ").lower()
print()
print(f">You want to be a {initial_choice.upper()}!  That's awesome, I'm a {initial_choice} too!!")
print()



if initial_choice.startswith('r'):
    print("As " + initial_choice + "s, we just fell out of a cloud in Burnsville.")
    print()
    a_1 = input("Are you scared, yes or no? ").lower()
    if a_1.startswith('y'):
        print(">I'm actually kind of scared too, I don't like the suburbs!")
    else:
        print(">That's fantastic, you're very brave!")
    print()
    print("...I should tell you...I'm pretty chatty...")
    print()
    try:
        a_2 = int((input("If you had to guess in seconds, how long do you think until we hit the ground? ")).replace(',', ''))
        #print(a_2)
    except:
        print(">I'm sorry, I need you to just enter a number.")
        print()
        a_2 = int((input("If you had to guess in seconds, how long do you think until we hit the ground? ")).replace(',', ''))
        #print(a_2)
        pass

    if a_2 > 600:
        print()
        print(f"You guessed {a_2} seconds.")
        print(">Did you know:")
        print("     The average speed for a raindrop is 14mph and average cloud height is 2500 feet.")
        print("     So maybe if our cloud was extra high it would take us that long!")
    elif a_2 > 300 and a_2 <= 600:
        print()
        print(">Very small raindrops can take up to 7 minutes to hit the ground.")
        print(f">So it might take us the {a_2} seconds that you guessed!")
    else:
        print()
        print(">The average raindrop takes 2 minutes to hit the ground.  You're so smart!")





    
    
    





