# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
    # pets.remove('cat')

# print(pets)

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a %s." % animal_type)
    print("My %s's name is %s." % (animal_type, pet_name.title()))

describe_pet('hamster', 'harry')
describe_pet(animal_type='cat', pet_name='willie')
