class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print out descriptive information of a restaurant."""
        msg = self.restaurant_name.title() + " serves delicious "
        msg += self.cuisine_type + '!'
        print("\n" + msg)

    def open_restaurant(self):
        """Show a message of restaurant opening"""
        print("Restaurant %s is now open." % self.restaurant_name)\

    def set_number_served(self, number):
        """Set number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, increment_num):
        """Allow user to increment the number of customers served."""
        if increment_num >= 0:
            self.number_served += increment_num
        else:
            print("Increment number can't be negative!")
