numbers_list = list(map(int, input().split()))

data = input()
manipulated_num_list = []

while not data == "exhausted":
    data_list = input().split()
    command = data_list[0]

    if command == 'set':
        if len(set(numbers_list)) == len(numbers_list):
            print('It is a set')
        else:
            manipulated_num_list = list(sorted(set(numbers_list), key=numbers_list.index))
    elif command == 'filter':
        even_or_odd = data_list[1]
        if even_or_odd == 'even':
            manipulated_num_list = [num for num in numbers_list if num % 2 == 0]
        else:
            manipulated_num_list = [num for num in numbers_list if num % 2 == 1]
    elif command == 'multiply':
        number = input(data_list[1])
        manipulated_num_list = [num * number for num in numbers_list]
    elif command == 'divide':
        number = input(data_list[1])
        if number == 0:
            print('Zero division caught')
        else:
            manipulated_num_list = list(map(lambda x: x*number, numbers_list))
    elif command == 'slice':
        left = int(data_list[1])
        right = int(data_list[2])
        if 0 <= left < len(numbers_list) and 0 <= right < len(numbers_list):
            manipulated_num_list = numbers_list[left:right+1]
    elif command == 'sort':
        pass
    elif command == 'reverse':
        pass

    data= input()
