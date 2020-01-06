responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    place = input("Where would you go for a vacation? ")
    responses[name] = place

    repeat = input("Another person to poll?(yes/no) ")
    if repeat == 'no':
        polling_active = False

# Show the result of poll
print("\n--- Poll Result ---")
for name, place in responses.items():
    print("%s would like to go to %s for a vacation." % (name.title(), place.title()))
