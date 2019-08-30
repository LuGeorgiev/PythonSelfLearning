area_side = int(input())
tile_width = float(input())
tile_height = float(input())
bench_width = int(input())
bench_length = int(input())
area_to_cover = area_side*area_side - bench_length*bench_width
tile_area = tile_height*tile_width
tiles_needed = area_to_cover/tile_area
time = tiles_needed*0.2

print(round(tiles_needed, 2))
print(round(time, 2))