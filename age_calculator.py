from datetime import datetime

def calculate_age(birth_date, fixed_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    fixed_date = datetime.strptime(fixed_date, "%Y-%m-%d")

    # Calculate age in years
    age = fixed_date.year - birth_date.year - ((fixed_date.month, fixed_date.day) < (birth_date.month, birth_date.day))

    # Calculate months and days
    if fixed_date.month < birth_date.month or (fixed_date.month == birth_date.month and fixed_date.day < birth_date.day):
        months = (fixed_date.month + 12) - birth_date.month - 1
    else:
        months = fixed_date.month - birth_date.month

    if fixed_date.day < birth_date.day:
        fixed_date_month_adjusted = fixed_date.replace(month=fixed_date.month - 1 if fixed_date.month > 1 else 12,
                                                      year=fixed_date.year - 1 if fixed_date.month == 1 else fixed_date.year)
        days = (fixed_date - fixed_date_month_adjusted).days
    else:
        days = fixed_date.day - birth_date.day

    return age, months, days

# Input birth date
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")

# Input fixed date for calculation
fixed_date_input = input("Enter the fixed date for calculation (YYYY-MM-DD): ")

# Calculate age
age, months, days = calculate_age(birth_date_input, fixed_date_input)

# Output the calculated age
print(f"Your age is: {age} years, {months} months, and {days} days.")
