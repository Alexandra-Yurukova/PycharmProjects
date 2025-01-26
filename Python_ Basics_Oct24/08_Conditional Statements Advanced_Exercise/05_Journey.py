budget = float(input())
season = input()

destination = ""
vacation_type = ""
vacation_cost = 0.0

if season == "summer":
    vacation_type = "Camp"
elif season == "winter":
    vacation_type = "Hotel"

if budget > 1000:
    vacation_type = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_cost = budget * 0.30
    elif season == "winter":
        vacation_cost = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_cost = budget * 0.40
    elif season == "winter":
        vacation_cost = budget * 0.80
else:
    destination = "Europe"
    vacation_cost = budget * 0.90

print(f'Somewhere in {destination}')
print(f"{vacation_type} - {vacation_cost :.2f}")