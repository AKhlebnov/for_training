def revers(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    return nums


print(revers(nums=[81, 9, 4, 4, 0]))
