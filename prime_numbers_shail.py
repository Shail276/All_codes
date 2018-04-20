# code to find prime numbers

x = [3,4]

for number in x:
	if number > 1:

		for y in range(2,number):
			if (number % y) == 0:
				print (number, ': It is not a prime number')
				break
			else:
				print (number, ':is a prime number')


	else: 
		print (number, ': It is not a prime number') 

