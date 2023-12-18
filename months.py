# Programmer: Noah
# Description: Months

#Get a list of months
months = [
    "January", 
    "February", 
    "March", 
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


month = input ("enter a month ")


while month not in months:
    print ("Invalid month! Try again.")
    month = input ("enter a month ")

if month == "February":
    print (f" {month} has 28 or 29 days")
elif month in ["November", "April", "June", "September"]:
    print (f" {month} has 30 days")
else:
    print (f" {month} has 31 days")
    

