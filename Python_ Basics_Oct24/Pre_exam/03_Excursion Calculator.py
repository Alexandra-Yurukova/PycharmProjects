number_people = int(input())
season = input()
price_per_person = 0.00
is_error = False

if season == "spring":
    if 0 <= number_people <= 5:
        price_per_person = number_people * 50
    elif number_people > 5:
        price_per_person = number_people * 48
    else:
        is_error = True
elif season == "summer":
    if 0 <= number_people <= 5:
        price_per_person = (number_people * 48.50) * 0.85
    elif number_people > 5:
        price_per_person = (number_people * 45) * 0.85
    else:
        is_error = True
elif season == "autumn":
    if 0 <= number_people <= 5:
        price_per_person = number_people * 60
    elif number_people > 5:
        price_per_person = number_people * 49.50
    else:
        is_error = True
elif season == "winter":
    if 0 <= number_people <= 5:
        price_per_person = (number_people * 86) * 1.08
    elif number_people > 5:
        price_per_person = (number_people * 85) * 1.08
    else:
        is_error = True
else:
    is_error = True


if is_error:
    print("error")
else:
    print(f"{price_per_person :.2f} leva.")
