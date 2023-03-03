def firstMissingPositive(nums):
    nums = sorted(set(nums))
    count = 1
    while count:
        if count in nums:
            count +=1
        else:
            return count

print(firstMissingPositive(nums))