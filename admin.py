"""A collection of classes for modeling an admin user account."""

from user import User

class Admin(User):
    """A model for administrator."""

    def __init__(self, first_name, last_name, user_name):
        """Initialize the administrator."""
        super().__init__(first_name, last_name, user_name)
        self.privileges = Privileges() 

class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nThe administrator has following privileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")
