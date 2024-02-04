# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime

# Read the date in MM DD YYYY format
date_string = input().strip()

# Convert the date string to a datetime object
date_object = datetime.strptime(date_string, '%m %d %Y')

# Get the day of the week as a string and capitalize it
day_of_week = date_object.strftime('%A').upper()

# Print the day of the week
print(day_of_week)