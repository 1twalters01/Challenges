def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1+nums2)
    if len(nums)%2 == 1:
        index = (len(nums)+1)//2
        value = nums[index-1]
        return value
    else:
        index = float(len(nums)+1)/2
        value = (nums[int(index-0.5)-1]+nums[int(index+0.5)-1])/2
        return value


nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))