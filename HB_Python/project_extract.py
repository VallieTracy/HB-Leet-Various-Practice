# Import dependencies
import random
import time
from random import choice
import string

# Variables to store lists of various grocery stores
stores_list1 = ['Cub Foods', 'Hyvee', "Costco"]
stores_list2 = ["Jerry's", "Lunds & Byerly's", "Kowalski's"]

first_store = choice(stores_list1)
second_store = choice(stores_list2)

jerry = stores_list2[0].lower()
print(jerry.title())

