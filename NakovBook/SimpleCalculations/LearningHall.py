hall_length = float(input())
hall_width = float(input())

rows = hall_length//1.2
cols = (hall_width-1)//0.7

print(int(rows*cols-3))
