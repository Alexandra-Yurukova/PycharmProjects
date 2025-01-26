starting_points = int(input())

bonus_points = 0
if starting_points <= 100:
    bonus_points = 5
elif 100 < starting_points <= 1000:
    bonus_points = starting_points * 0.20
else:
    bonus_points = starting_points * 0.10

additional_bonus_points = 0
if starting_points % 2 == 0:
    additional_bonus_points = 1
if starting_points % 10 == 5:
    additional_bonus_points = 2

total_bonus = bonus_points + additional_bonus_points

print(total_bonus)
print(starting_points + total_bonus)