length = int(input())
width = int(input())
height = int(input())
not_empty_percent = float(input())

total_volume = length * width * height
total_volume_in_liters = total_volume / 1000

total_liters_needed = total_volume_in_liters * (1 - not_empty_percent / 100)

print(total_liters_needed)