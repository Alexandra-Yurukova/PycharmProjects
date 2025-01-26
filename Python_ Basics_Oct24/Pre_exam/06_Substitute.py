K = int(input())
L = int(input())
M = int(input())
N = int(input())

valid_changes = 0

for first1 in range(K, 9):
    for second1 in range(9, L - 1, -1):
        for first2 in range(M, 9):
            for second2 in range(9, N - 1, -1):

                if first1 % 2 == 0 and second1 % 2 != 0 and first2 % 2 == 0 and second2 % 2 != 0:

                    num1 = f"{first1}{second1}"
                    num2 = f"{first2}{second2}"

                    if num1 != num2:
                        print(f"{num1} - {num2}")
                        valid_changes += 1
                    else:
                        print("Cannot change the same player.")

                    if valid_changes == 6:
                        break
            if valid_changes == 6:
                break
        if valid_changes == 6:
            break
    if valid_changes == 6:
        break
