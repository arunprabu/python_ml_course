# =============================================================
# MODULE 3.1b: Inheritance (Single)
# =============================================================
# Java:   class Manager extends Employee { }
# Python: class Manager(Employee): ...
#
# super() works the same way as in Java.
# Method overriding works the same way too.

print("=" * 55)
print("MODULE 3.1b: Single Inheritance")
print("=" * 55)


class Employee:
    """Base class."""

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def get_info(self):
        return f"[{self.emp_id}] {self.name} | {self.department} | ₹{self.salary:,}"

    def give_raise(self, percent):
        increase = self.salary * (percent / 100)
        self.salary += increase
        print(f"{self.name}'s salary raised by {percent}% → ₹{self.salary:,.2f}")


class Manager(Employee):
    """Manager IS-A Employee with extra responsibilities."""

    def __init__(self, emp_id, name, department, salary, team_size):
        # Call parent __init__ using super()
        super().__init__(emp_id, name, department, salary)
        self.team_size = team_size  # extra attribute specific to Manager

    def get_info(self):
        """Override parent method — extend with team_size info."""
        base = super().get_info()  # reuse parent's output
        return f"{base} | Team: {self.team_size} people"

    def approve_leave(self, employee_name, days):
        """New method — only Managers have this."""
        print(f"{self.name} approved {days}-day leave for {employee_name}")


class SeniorManager(Manager):
    """Multi-level inheritance: SeniorManager → Manager → Employee."""

    def __init__(self, emp_id, name, department, salary, team_size, budget):
        super().__init__(emp_id, name, department, salary, team_size)
        self.budget = budget

    def get_info(self):
        base = super().get_info()
        return f"{base} | Budget: ₹{self.budget:,}"


# --- Demo ---
emp = Employee("E001", "Alice", "Engineering", 70000)
mgr = Manager("M001", "Charlie", "Engineering", 120000, 9)
smgr = SeniorManager("SM001", "Diana", "Technology", 200000, 30, 2000000)

print("Employee:")
print(f"  {emp.get_info()}")

print("\nManager (inherits give_raise from Employee):")
print(f"  {mgr.get_info()}")
mgr.give_raise(15)  # inherited from Employee
mgr.approve_leave("Alice", 3)

print("\nSeniorManager (inherits from Manager → Employee):")
print(f"  {smgr.get_info()}")

# # isinstance() confirms the inheritance chain
print(f"\nisinstance checks:")
print(f"  mgr is Employee?      {isinstance(mgr, Employee)}")  # True
print(f"  mgr is Manager?       {isinstance(mgr, Manager)}")  # True
print(f"  emp is Manager?       {isinstance(emp, Manager)}")  # False
print(f"  smgr is Employee?     {isinstance(smgr, Employee)}")  # True
