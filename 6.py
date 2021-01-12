goods = []
features = {'title': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'title': [], 'price': [], 'quantity': [], 'unit': []}
num = 0

while True:
    if input('to exit press Q or enter to continue: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        prop = input(f'enter {f} - ')
        features[f] = int(prop) if(f == 'price' or f == 'quantity') else prop
        analytics[f].append(features[f])
    goods.append((num, features))
    print (f'\n the structure of the product\n{goods}')
    print(f'\nAnalitics by product:\n{"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print('*' * 30)