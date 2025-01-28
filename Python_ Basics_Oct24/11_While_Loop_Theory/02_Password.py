username = input()
password = input()
new_pass_input = input()

while True:
    if new_pass_input == password:
        print(f"Welcome {username}!")
        break

    new_pass_input = input()