import math

a = float(input())
b = float(input())
c = float(input())

volume_truck = a * b * c
n = float(input())
count_b = 0

for barrel in range(n):
    r = float(input())
    h = float(input())
    volume_b = math.pi * r**2 * h
    if volume_truck >= volume_b:
        volume_truck -= volume_b
        count_b += 1
    else:
        print(f'Truck is full. {count_b} on board')
        exit(0)

if count_b == n:
    print(f'All barrels on board. Capacity left - {volume_truck:.2f}')

