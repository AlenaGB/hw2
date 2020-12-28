myRait = list(map(int,input('Enter the initial value of the rating: ').split()))
print(' '.join(map(str,myRait)))

sorRait = sorted(myRait)
print(' '.join(map(str,sorRait)))

number = int(input('Enter the new value of the rating: '))

while number <=0:
    number = int(input('Enter a natural number: '))

for el in range(len(sorRait)):
        if number == sorRait[el] or number < sorRait[el]:
            sorRait.insert(el,number)
            break
else:
    sorRait.append(number)

print("New rating is: ")
print(' '.join(map(str,sorRait)))