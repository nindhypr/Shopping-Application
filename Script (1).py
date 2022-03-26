pencil_price = 2
money = 10

input_count = input('How many pencils do you want?: ')
count = int(input_count)
total_price = pencil_price * count

print('You will buy ' + str(count) + ' pencils')
print('The total price is ' + str(total_price) + ' dollar')

if money > total_price:
	print('You will buy ' + str(count) + ' pencils')
	print('You have ' + str(money - total_price) + ' dollar left')
elif money == total_price:
	print('You will buy ' + str(count) + ' pencils')
	print('You do not have money')
else:
	print('You do not have enough money')
	print('You can not buy that many pencils')