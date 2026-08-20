# =============================================================
# Scope — Local vs Global
# =============================================================
# Local variable: defined inside a function — invisible outside
# Global variable: defined outside — visible everywhere

company_name = "TechCorp"  # global variable


def show_company():
    dept = "Engineering"  # local variable
    print(f"Company: {company_name}, Dept: {dept}")  # can read global


def update_global():
    global company_name  # must declare 'global' to modify it
    company_name = "InnovateTech"


print(f"\nBefore: {company_name}")
show_company()


update_global()
print(f"After:  {company_name}")


# Local variable is NOT accessible outside the function
def create_temp():
    temp_data = "temporary"


create_temp()


try:
    print(temp_data)
except NameError as e:
    print(f"Cannot access local variable outside function: {e}")
