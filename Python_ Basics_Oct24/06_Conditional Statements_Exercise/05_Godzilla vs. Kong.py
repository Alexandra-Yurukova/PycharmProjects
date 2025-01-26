
budget = float(input())
crew_count = int(input())
clothes_price = float(input())

decor = budget * 0.10
total_clothes_price = crew_count * clothes_price

total_budget_spent = total_clothes_price + decor
if crew_count > 150:
    price = total_clothes_price * 0.1
    total_budget_spent: float = total_budget_spent - price

if total_budget_spent > budget:
    print('Not enough money!')
    print(f'Wingard needs {total_budget_spent-budget :.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget - total_budget_spent :.2f} leva left.')

# budget = float(input())
# crew_count = int(input())
# clothes_price = float(input())
#
# decor = budget * 0.10
# total_clothes_price = crew_count * clothes_price
#
# if crew_count > 150:
#     total_clothes_price *= 0.90
#
# total_cost = total_clothes_price + decor
#
# if budget >= total_cost:
#     money_left = budget - total_cost
#     print('Action!')
#     print(f'Wingard starts filming with {money_left :.2f} leva left.')
#
# else:
#     money_needed = total_cost - budget
#     print('Not enough money!')
#     print(f'Wingard needs {money_needed :.2f} leva more.')