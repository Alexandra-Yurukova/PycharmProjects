from math import ceil

series_name = str(input())
movie_duration = int(input())
break_duration = int(input())


lunch_break = break_duration * 0.125
rest_break = break_duration * 0.25

total_brake_time = lunch_break + rest_break
break_time_left = break_duration - total_brake_time

if break_time_left >= movie_duration:
    time_left = break_time_left - movie_duration
    print(f'You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.')
else:
    time_needed = movie_duration - break_time_left
    print(f"You don't have enough time to watch {series_name}, you need {ceil(time_needed)} more minutes.")