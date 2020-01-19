class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nName of Restaurant: %s" % self.restaurant_name.title())
        print("Cuisine Type: %s" % self.cuisine_type.title())

    def open_restaurant(self):
        print("Restaurant %s is now open." % self.restaurant_name)

# my_restaurant = Restaurant("hujin restaurant", "chinese")

# print("Name of Restaurant: %s" % my_restaurant.restaurant_name.title())
# print("Cuisine Type: %s" % my_restaurant.cuisine_type.title())

# print("\n")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

restaurant_1 = Restaurant('hujin', 'hubei cuisine')
restaurant_2 = Restaurant('quan ju de', 'roast duck')
restaurant_3 = Restaurant('mcdonaut', 'fast food')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

