nums = [0,1,1,2,4,6]

def remove_dups(numbers):
    singles = []
    
    for i in range(len(numbers) - 1):
        if numbers[i+1] != numbers[i]:
            singles.append(numbers[i+1])
        
    return singles

print(remove_dups(nums))

#not working!