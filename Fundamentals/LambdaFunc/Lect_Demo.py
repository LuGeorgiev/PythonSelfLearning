students_grades = {
    'ivan': [3, 4],
    'petar': [5, 3, 5],
    'maria': [6, 6, 6, 5],
    'gosho': [3, 5]
}

sorted_grades = sorted(students_grades, key=lambda kvp: (len(kvp[1]), kvp[0]))
print(sorted_grades)


# Reverse positive numbers
positive_nums_list = list(filter(lambda x: x >= 0, map(int, input().split())))
print(*positive_nums_list[::-1])
