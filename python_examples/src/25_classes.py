# =============================================================
# MODULE 3.1a: Classes, Objects and __init__
# =============================================================
# OOP in Python vs Java:
#   - __init__ replaces the constructor
#   - 'self' replaces 'this'
#   - No type declarations on attributes
#   - Class variables replace 'static' fields

print("=" * 55)
print("MODULE 3.1a: Classes, Objects and __init__")
print("=" * 55)


class Employee:
    """Represents an employee in a company."""

    # Class variable — shared by ALL instances (like static in Java)
    company_name = "TechCorp"
    headcount = 0

    # the following is the constructor
    # (optional if you are not expecting instantiation params)
    def __init__(self, emp_id, name, department, salary):
        """
        Instance initializer — called when you create an object.
        'self' refers to the current instance (like 'this' in Java).
        Instance variables — unique to each object.
        """
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        Employee.headcount += 1  # update class variable

    # public method - normally accessible upon creating an instance
    def get_info(self):
        """Instance method — needs 'self' as first parameter."""
        return f"[{self.emp_id}] {self.name} | {self.department} | ₹{self.salary:,}"

    # public method receiving a param
    def give_raise(self, percent):
        """Update salary by a percentage."""
        increase = self.salary * (percent / 100)
        self.salary += increase
        print(f"{self.name}'s salary raised by {percent}% → ₹{self.salary:,.2f}")

    @classmethod  # will be available without creating instance - directly on the class
    def get_headcount(self):
        """Class method — operates on the class, not an instance."""
        return f"{self.company_name} has {self.headcount} employee(s)"

    @staticmethod
    def validate_salary(salary):
        """Static method — no access to instance or class. Pure utility."""
        return salary >= 15000


# Creating objects
emp1 = Employee("E001", "Alice", "Engineering", 70000)
emp2 = Employee("E002", "Bob", "Marketing", 55000)

print(emp1.get_info())
print(emp2.get_info())


print(Employee.get_headcount())

emp1.give_raise(10)

print(f"\nValid salary ₹15000? {Employee.validate_salary(15000)}")
print(f"Valid salary ₹5000?  {Employee.validate_salary(5000)}")

# # Class variable accessible from both instance and class
print(f"\nCompany (via instance): {emp1.company_name}")
print(f"Company (via class):    {Employee.company_name}")
