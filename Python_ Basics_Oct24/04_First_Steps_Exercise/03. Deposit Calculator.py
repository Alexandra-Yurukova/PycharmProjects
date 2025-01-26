deposit = float(input())
period = int(input())
interest = float(input())
interest_percent = interest / 100
amount = deposit + period * ((deposit * (interest_percent)) / 12)
print(amount)
