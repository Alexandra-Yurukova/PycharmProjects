n = int(input())
next_number = 1

while True:
    if next_number > n:
        break
    print(next_number)
    next_number = (next_number * 2) + 1