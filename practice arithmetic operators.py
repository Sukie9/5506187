def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Reading the year from STDIN
year = int(input())

# Checking if it is a leap year and printing the result
result = is_leap(year)
print(result)