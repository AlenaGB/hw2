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
    print("month number {} is {}".format(month, mList[month]))

# задача на время года
seasons = {'winter': (1, 2, 12), 'spring': (3, 4, 5), 'summer' : (6, 7, 8),'autumn': (9, 10, 11)}
for key in seasons.keys():
    if month in seasons[key]:
        print(f"It is {key}")

# время года со списком из рабора дз
season = ['winter', 'spring', 'summer', 'autumn', 'winter']
print(f'It is {season[int(month) // 3]}')