from functools import total_ordering

chicken_menu = 10.35
fish_menu = 12.40
veggie_menu = 8.15
delivery_fee = 2.50

total_chicken_menu = int(input())
total_fish_menu = int(input())
total_veggie_menu = int(input())

total_order = total_chicken_menu * chicken_menu + total_fish_menu * fish_menu + total_veggie_menu * veggie_menu

dessert = total_order * 0.20
order_cost = total_order + dessert + delivery_fee

print(order_cost)
