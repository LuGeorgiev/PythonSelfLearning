def find_result(num_str):
    sum_odd = 0
    sum_even = 0
    for char in num_str:
        if char == '-':
            continue
        number = int(char)
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number

    return sum_odd * sum_even


if __name__ == "__main__":
    string_num = input()
    result = find_result(string_num)
    print(result)
