prompt = "\nHow old are you?"
prompt += "\nUse 'quit' to exit. "

while True:
    age = input(prompt)
    age = int(age)

    if age < 0:
        print("Wrong input. Please input your age again.")
        continue
    elif age <= 3 and age >= 0:
        print("Ticket cost: $0.")
    elif age <= 12:
        print("Ticket cost: $10.")
    elif age > 12:
        print("Ticket cost: $15.")
        

