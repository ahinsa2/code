# Function to check if a year is leap
def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Main program
month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

# Days in each month (default for non-leap years)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# If February and leap year, adjust days to 29
if month == 2 and is_leap_year(year):
    print("Number of days: 29")
elif 1 <= month <= 12:
    print("Number of days:", days_in_month[month - 1])
else:
    print("Invalid month number!")
