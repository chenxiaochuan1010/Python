class User():
    """A model for users information"""

    def __init__(self, first_name, last_name, user_name):
        """Initialize first name, last name, user name and password"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.login_attempts = 0

    def describe_user(self):
        """print out all attributes of a user"""
        print("\nFollowing are the information of user: ")
        print("First Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        print("User Name: " + self.user_name.title())

    def greet_user(self):
        """Personalized greeting to the user"""
        print("Welcome login, %s!" % self.user_name.title())

    def increment_login_attempts(self):
        """Add login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Set login attempts back to 0."""
        self.login_attempts = 0

# user_1 = User('xiaochuan', 'chen', 'cxc1010')
# user_2 = User('min', 'jia', 'lily')
# user_3 = User('yanxi', 'chen', 'cyx2016')

# user_1.describe_user()
# user_1.greet_user()

# user_2.describe_user()
# user_2.greet_user()

# user_3.describe_user()
# user_3.greet_user()

user = User('xiaochuan', 'chen', 'cxc1010')
user.increment_login_attempts()
print("Login attempts = %i" % user.login_attempts)
user.increment_login_attempts()
print("Login attempts = %i" % user.login_attempts)
user.reset_login_attempts()
print("Login attempts = %i" % user.login_attempts)
