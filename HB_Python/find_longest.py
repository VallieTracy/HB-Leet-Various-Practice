words = ['coffee', 'mug', 'ceramic', 'bean']

def longest_testing(some_param):
    for param in some_param:
        print(param + " " + str(len(param)) + " letter length")

# longest_testing(words)

def longest(some_param):
    
    lengths_list = []
    
    for param in some_param:
        
        lengths_list.append(len(param))

    print(lengths_list)
    print(max(lengths_list))

longest(words)

# making progress here, but not done.  It is printing the length of the longest word, but need to print the word itself!

# sorted_words = sorted(words, key = len)
# print(sorted_words)
# print(f"The longest word is {sorted_words[-1]}")

def find_longest(some_param):
    sorted_words = sorted(some_param, key = len)
    print(f"The longest word is {sorted_words[-1]}")

find_longest(words)
