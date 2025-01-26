budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards_price = video_cards_count * 250

processors_price = video_cards_price * 0.35
ram_price = video_cards_price * 0.10

total_cost = video_cards_price + processors_count * processors_price + ram_count * ram_price

if video_cards_count > processors_count:
    total_cost *= 0.85

if budget >= total_cost:
    money_left = budget - total_cost
    print(f'You have {money_left :.2f} leva left!')
else:
    money_needed = total_cost - budget
    print(f'Not enough money! You need {money_needed :.2f} leva more!')