nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    seen = {}
    for index, number in enumerate(nums):
        difference = target - number
        if number in seen:
            return index, seen[number]
        
        seen[difference] = index

print(twoSum(nums, target))