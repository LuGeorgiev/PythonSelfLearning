students_grades = {
    'ivan': [3, 4],
    'petar': [5, 3, 5],
    'maria': [6, 6, 6, 5],
    'gosho000000': [3, 5]
}

sorted_grades = sorted(students_grades, key=lambda kvp: (kvp[0], len(kvp[1])))
print(sorted_grades[::-1])


# Reverse positive numbers

nums = (2, 3, 34, -56, -2, 34, -23)
positive_nums_list = list(filter(lambda x: x >= 0, map(int, nums)))
print(*positive_nums_list[::-1])
