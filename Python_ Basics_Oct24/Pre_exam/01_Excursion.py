price_per_night = 20
transportation_card = 1.60
museum_ticket = 6

num_people_group = int(input())
num_nights = int(input())
num_cards = int(input())
num_tickets = int(input())

total_price_hotel = num_nights * price_per_night
total_price_cards = num_cards * transportation_card
total_price_tickets = num_tickets * museum_ticket

price_per_person = (total_price_hotel + total_price_cards + total_price_tickets)
total_price_group = price_per_person * num_people_group
final_cost = total_price_group * 1.25

print(f"{final_cost :.2f}")
