type_flowers = input()
number_of_flowers = int(input())
budget = int(input())

sub_total = 0.00

if type_flowers == "Roses":
    if number_of_flowers > 80:
        sub_total = (number_of_flowers * 5.00) * 0.9
    else:
        sub_total = number_of_flowers * 5.00
elif type_flowers == "Dahlias":
    if number_of_flowers > 90:
        sub_total = (number_of_flowers * 3.80) * 0.85
    else:
        sub_total = number_of_flowers * 3.80
elif type_flowers == "Tulips":
    if number_of_flowers > 80:
        sub_total = (number_of_flowers * 2.80) * 0.85
    else:
        sub_total = number_of_flowers * 2.80
elif type_flowers == "Narcissus":
    if number_of_flowers < 120:
        sub_total = (number_of_flowers * 3) * 1.15
    else:
        sub_total = number_of_flowers * 3
elif type_flowers == "Gladiolus":
    if number_of_flowers < 80:
        sub_total = (number_of_flowers * 2.50) * 1.2
    else:
        sub_total = number_of_flowers * 2.50
if budget >= sub_total:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flowers} and {budget - sub_total:.2f} leva left.")
else:
    print(f"Not enough money, you need {sub_total - budget:.2f} leva more.")