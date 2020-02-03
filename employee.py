class Employee():
    """A model to collect employee information"""

    def __init__(self, first, last, salary):
        """Store first, last, salary as attributes"""
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary

    def give_raise(self, amount=5000):
        """Add the given amount to annual salary."""
        self.annual_salary += amount

        
