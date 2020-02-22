def max_subarray(array_list):
 	if len(array_list) == 0:
 		return False

 	max_sum_of_subarray = current_sum_of_subarray = array_list[0]

 	for num in array_list[1:]:
 		current_sum_of_subarray = max(current_sum_of_subarray + num, num)
 		max_sum_of_subarray = max(current_sum_of_subarray,max_sum_of_subarray)
 	print(max_sum_of_subarray)


max_subarray([-2,1,-3,4,-1,2,1,-5,4])

