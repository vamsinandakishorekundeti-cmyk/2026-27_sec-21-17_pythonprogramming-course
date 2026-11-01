# Example solution: voting eligibility using if-else
age_in_years = int(input("Enter age in years: "))

if age_in_years >= 18:
    print(f"Age {age_in_years} years: Eligible to vote")
else:
    print(f"Age {age_in_years} years: Not eligible to vote")