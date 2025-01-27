tournaments_count = int(input())
starting_points = int(input())

points_gained = 0
tournaments_wins = 0

for t in range (tournaments_count):
    current_result = input()
    if current_result == "W":
        points_gained += 2000
        tournaments_wins += 1
    elif current_result == "F":
        points_gained += 1200
    elif current_result == "SF":
        points_gained += 720

final_score = starting_points + points_gained
average_points_gained = points_gained / tournaments_count
percent_win = tournaments_wins / tournaments_count * 100

print(f"Final points: {final_score}")
print(f"Average points: {int(average_points_gained)}")
print(f"{percent_win :.2f}%")