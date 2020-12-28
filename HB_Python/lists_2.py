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

my_nums = [1, 2, 13, 4, 6, 6, 13, 13]

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

def sum13(nums):
    count = 0
    i = 0
    while i <= len(nums):
        if nums[i] in nums[-2:]:
            count = count + nums[i]
            i = i + 1
            print(f"COUNT: {count}")
            print(f"i = i + 1: {i}")
            print("-----------------")
        

print(sum13(my_nums))



