N = int(input())

total_liters = 0
total_degrees = 0

for day in range(1, N + 1):
    quantity = float(input())
    degrees = float(input())

    total_liters += quantity
    total_degrees += quantity * degrees

average_degrees = total_degrees / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
