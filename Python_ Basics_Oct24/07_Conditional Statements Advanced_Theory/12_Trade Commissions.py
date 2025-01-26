city = input()
volume = float(input())
commission = 0.00
is_error = False

if city == "Sofia":
    if 0 <= volume <= 500:
        commission = 0.05
    elif 500 < volume <= 1000:
        commission = 0.07
    elif 1000 < volume <= 10000:
        commission = 0.08
    elif volume > 10000:
        commission = 0.12
    else:
        is_error = True
elif city == "Varna":
    if 0 <= volume <= 500:
        commission = 0.045
    elif 500 < volume <= 1000:
        commission = 0.075
    elif 1000 < volume <= 10000:
        commission = 0.10
    elif volume > 10000:
        commission = 0.13
    else:
        is_error = True
elif city == "Plovdiv":
    if 0 <= volume <= 500:
        commission = 0.055
    elif 500 < volume <= 1000:
        commission = 0.08
    elif 1000 < volume <= 10000:
        commission = 0.12
    elif volume > 10000:
        commission = 0.145
    else:
        is_error = True
else:
    is_error = True

total_amount = volume * commission

if is_error:
    print("error")
else:
    print(f"{total_amount :.2f}")
