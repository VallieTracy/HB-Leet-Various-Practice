my_str = 'isIsogram'

def is_isogram(string):
    
    for i in range(len(string)):
        
        if string[i] in string[i:]:
            return False
        else:
            return True

print(is_isogram(my_str))




