# list
mList = ['','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = int(input("Enter number of month: "))

while month <= 0 or month > 12:
     month = int(input(f"There is no month with number {month}. Try again: "))
else:
    print("month number {} is {}".format(month, mList[month]))

# dictionary
mDict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
month = int(input("Enter number of month: "))

while month <= 0 or month > 12:
    month = int(input(f"There is no month with number {month}. Try again: "))
else:
    print("month number {} is {}".format(month, mDict[month]))