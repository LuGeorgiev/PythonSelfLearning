input_list = list(input().split(' '))
last_element = input_list.pop()
input_list.insert(0, last_element)
print(*input_list)

#print(input_list[-1], end=' ')
#print(*input_list[:-1])
