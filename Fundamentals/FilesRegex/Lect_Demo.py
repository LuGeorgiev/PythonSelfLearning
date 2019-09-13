#r - read, w - write
with open('my-file.txt', 'a') as file:
    file.write('added data')
    line_data = file.readline()
    while line_data != '':
        print(line_data, end='')
        line_data = file.readline()

