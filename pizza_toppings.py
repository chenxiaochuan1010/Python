prompt = "\nPlease enter what  pizza toppings you need."
prompt += "\nUse 'quit' to exit the program / 'done' to show your order: "

pizza_toppings = []

active = True
while active:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        active = False
    elif pizza_topping == 'done':
        print("\nYou've ordered:")
        print(pizza_toppings)
    else:
        print("%s will be added to your pizza." % pizza_topping)
        pizza_toppings.append(pizza_topping)
