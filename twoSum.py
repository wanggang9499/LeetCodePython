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

# ---------------------------------------------------------

def twoSum1(array_list,T):
 	if len(array_list) < 2:
 		return False

 	counted = set()
 	output_set = set()

 	for num in array_list:
 		the_num_you_want_to_find = T - num

 		if the_num_you_want_to_find not in counted:
 			counted.add(num)

 		else:
 			output_set.add((min(num,the_num_you_want_to_find),max(num,the_num_you_want_to_find)))

 	print('\n'.join(map(str,list(output_set))))
twoSum1([2,7,11,3,6,15],9)