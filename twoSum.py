def twoSum(nums, target):
    lens = len(nums)
    j = -1
    for i in range(1,lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target-nums[i])
            break
    if j >= 0:
        return [j,i]

a=twoSum([2,7,11,15],9)
print(a)
