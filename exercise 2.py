price = {
    'banana' : 4,
    'apple' : 2,
    'orange' : 1.5,
    'pear' : 3
}
#
purchased_items = {
    'banana' : 5,
    'orange' : 3
}
#
for key,values in purchased_items.items():
    keyprice = price[key]
    print('{0}, quantity: {1}, unit price: {2}'.format(key,values,keyprice))
#
total = 0

for key,values in purchased_items.items():
    keyprice = price[key]
    cost = values * price[key]
    print('{0} cost: {1}'.format(key,cost))
    total += cost
print('total cost: ' + str(total))
#
