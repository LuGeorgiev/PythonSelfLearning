def multiply(el, p):
    return el * p


if __name__ == "__main__":
    data_list = list(map(int, input().split(' ')))
    multiplyer = int(input())
    a = [multiply(el, multiplyer) for el in data_list]
    print(a)
    print(*a)
    print(' '.join(map(str, a)))

