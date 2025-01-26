pocket_money = float(input())
earned_money = float(input())
expenses = float(input())
gift_price = float(input())

saved_pocket_money = 5 * pocket_money
total_earned_money = 5 * earned_money

total_income = (saved_pocket_money + total_earned_money) - expenses

if total_income >= gift_price:
    print(f'Profit: {total_income :.2f} BGN, the gift has been purchased.')
else:
    money_needed = gift_price - total_income
    print(f'Insufficient money: {money_needed :.2f} BGN.')