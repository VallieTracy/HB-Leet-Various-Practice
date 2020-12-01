animals = ['elephant', 'ladybug', 'owl', 'cat', 'ant']

print(f"Animals! Yay! This is my list: {animals}")

print("------")

for animal in animals:
    print(animal)

print("-------")

print(animals[1])

print("-------")
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(5):
    print(f"animals[i]: {animals[i]}")

print("------")

print(animals[0][0])
print(animals[1][0])
print(animals[2][0])
print(animals[3][0])
print(animals[4][0])
print("------")

for i in range(5):
    print(animals[i][2])

print("-----")

for i in range(5):
    if animals[i] == 'owl':
        print(f"It's an owl! Whooooo!")
        print(animals[i])
        print(animals[i][0])

print("-----")

#doesn't work
# TIME TO LOOK AT THE SOLUTION!
for i in range(5):
    print(vowels[i])
    if animals[i][0] == vowels[i]:
        print(animal)

print("--------")
print("--------")

animals = ['ant', 'cat', 'elephant', 'giraffe', 'emu']
vowels = ['a', 'e', 'i', 'o', 'u']

def get_vowels(some_param):
    vowel_words = []

    for param in some_param:
        if param[0] in vowels:
            vowel_words.append(param)

    return vowel_words

print(get_vowels(animals))



