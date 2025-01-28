new_input = input()
total_sum = 0

while new_input != "NoMoreMoney":
    number_input = float (new_input)
    if number_input < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {number_input:.2f}")
    total_sum += number_input
    new_input = input()

print(f"Total: {total_sum:.2f}")