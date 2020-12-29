# my_nums = [1, 2, 2]

# def count_evens(nums):
#     evens = 0
#     for num in nums:
#         if num %  2 == 0:
#             evens += 1
#     return evens

# print(count_evens(my_nums))

# my_nums = [10]

# def big_diff(nums):
#     big = max(nums)
#     small = min(nums)
#     return big - small

# print(big_diff(my_nums))

#my_nums = [1, 2, 10, 4, 10, -1, -1]
# lrg = max(my_nums)
# sml = min(my_nums)
# print(my_nums)
# my_nums.remove(lrg, sml)
# print(my_nums)

# def centered_average(nums):
#     lrg = max(nums)
#     nums.remove(lrg)
#     sml = min(nums)
#     nums.remove(sml)
#     total = sum(nums)
#     ca = int(total / (len(nums)))
#     return ca

# print(centered_average(my_nums))



# def sum13(nums):
#     count = 0
#     i = 0
#     while i <= len(nums):
#         if nums[i] != 13:
#             print(f"i: {i}")
#             count = count + nums[i]
#             i = i + 1
#             print(f"COUNT: {count}")
#             print(f"i = i + 1: {i}")
#             print("-----------------")
#         elif nums[i] in nums[-2:] and nums[i] == 13:
#             print("clueless")
#             break
#         elif nums[i] == 13:
#             print(f"i: {i}")
#             i = i + 2
#             print(f"COUNT: {count}")
#             print(f"i = i+2: {i}")
#             print("--------------")

            
        

    # return count

# my_nums = [1, 2, 13, 4, 13, 2, 3] #length = 5, i in 0, 4

# def sum13(nums):
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] != 13:
#             count += nums[i] 
#         elif i < len(nums) - 1:
#             if nums[i+1] != 13:
#                 count -= nums[i+1]

#     return count     

# print(sum13(my_nums))

# my_nums = [1, 6, 7, 1, 6, 7, 2, 6, 1, 3, 5, 7, 14]
 
# def sum67(arr):
#     while 6 in arr: 
#         idx6 = arr.index(6)
#         idx7 = arr.index(7)
#         print(f"idx7: {idx7}")
#         del arr[idx6:idx7+1] 
    
#     return sum(arr)
        

# print(sum67(my_nums))

my_nums = [1, 2, 2, 4]

def has22(nums):
    while 2 in nums:
        for i in range(len(nums)-1):
            if nums[i] == 2:
                if nums[i+1] == 2:
                    return True
    else:
        return False

print(has22(my_nums))


        





