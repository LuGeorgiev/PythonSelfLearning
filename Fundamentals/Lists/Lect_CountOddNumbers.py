nums = list(map(int, input().split(' ')))

odd_num_list = [num for num in nums if num % 2 == 1]
print(len(odd_num_list))
