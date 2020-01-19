class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print out descriptive information of a restaurant."""
        print("\nName of Restaurant: %s" % self.restaurant_name.title())
        print("Cuisine Type: %s" % self.cuisine_type.title())

    def open_restaurant(self):
        """Show a message of restaurant opening"""
        print("Restaurant %s is now open." % self.restaurant_name)\

    def set_number_served(self, number):
        """Set number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, increment_num):
        if increment_num >= 0:
            self.number_served += increment_num
        else:
            print("Increment number can't be negative!")

# my_restaurant = Restaurant("hujin restaurant", "chinese")

# print("Name of Restaurant: %s" % my_restaurant.restaurant_name.title())
# print("Cuisine Type: %s" % my_restaurant.cuisine_type.title())

# print("\n")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# restaurant_1 = Restaurant('hujin', 'hubei cuisine')
# restaurant_2 = Restaurant('quan ju de', 'roast duck')
# restaurant_3 = Restaurant('mcdonaut', 'fast food')

# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()

restaurant = Restaurant('hujin', 'hubei cuisine')
restaurant.set_number_served(20)
print("The restaurant is now serving %i people." % restaurant.number_served)
restaurant.increment_number_served(10)
print("The restaurant is now serving %i people." % restaurant.number_served)
restaurant.increment_number_served(-10)
print("The restaurant is now serving %i people." % restaurant.number_served)



# restaurant.number_served = 10
# print("The restaurant is now serving %i people." % restaurant.number_served)


