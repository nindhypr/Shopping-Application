money = 20
items = {'mouse': 2, 'keyboard': 4, 'headphone': 6}

for item_name in items:
	print('--------------------------------------------------')
	print('You have ' + str(money) + ' dollar left in your wallet')
	print('The price for each ' + item_name + ' ' + 'is ' + str(items[item_name]) + ' dollar')

    
	input_count = input('How many ' + item_name + '?:')
	print('You will buy ' + input_count + ' ' + item_name)

	count = int(input_count)
	total_price = items[item_name] * count
	print('The total price is ' + str(total_price) + ' dollar')

	if money >= total_price:
		print('You have purchased ' + input_count + ' ' + item_name)
		money -= total_price

		if money == 0:
			print('You do not have money')
			break

	else:
		print('You do not have enough money')
		print('You can not buy ' + item_name + ' that many')

print('You have ' + str(money) + ' dollar left')