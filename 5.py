myRait = list(map(int, input('Enter the initial value of the rating: ').split()))
print(' '.join(map(str, myRait)))

myRait.sort(reverse=True)
print(' '.join(map(str, myRait)))

number = int(input('Enter the new value of the rating: '))

while number <= 0:
    number = int(input('Enter a natural number: '))

for el in range(len(myRait)):
        if number == myRait[el] or number > myRait[el]:
            myRait.insert(el, number)
            break
else:
    myRait.append(number)

print("New rating is: ")
print(' '.join(map(str, myRait)))

# решение из разбора дз
myRait = list(map(int, input('Enter the initial value of the rating: ').split()))
print(' '.join(map(str, myRait)))

myRait.sort(reverse=True)
print(' '.join(map(str, myRait)))

number = int(input('Enter the new value of the rating: '))
i = 0

for n in myRait:
    if number <= n:
        i += 1
myRait.insert(i, float(number))
print(' '.join(map(str, myRait)))
