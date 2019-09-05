num_list = [1, 1, 2, 3, 3, 4]
index = 0
while index < len(num_list)-1:
    if num_list[index] == num_list[index+1]:
        cur_sum = num_list[index] + num_list[index+1]
        del num_list[index]
        num_list[index] = cur_sum
        index = -1
    index += 1

print(*num_list)
