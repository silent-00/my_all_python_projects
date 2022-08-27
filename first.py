#!/bin/python3


# Login and money withdro This project can be use on web or harwaredevices

name = input("Enter your name ")
password = input("Enter your password ")
if name == "silent" and password == "#mrbot":
	print("Login sucesfully")
	
	try:
		amount = int(input("Enter your amount "))
		re_type_amount = int(input("Please re-type the amount "))
		if re_type_amount == amount:
			if amount and re_type_amount > 500 and amount and re_type_amount < 40000:
				account_pass = input("Security account password ")
				if account_pass == "hello":
					print("Sucessfully completed please cheak your money box")
				else:
					print("Account security password is worrng")
			else:
				print("min amount is 500 and max amount is 40000\n")
				print("Please try again")
		else:
			print("Please enter correct amount")
	except:
		print("Something went worrng please try again")	
else:
	print("Identity do not mach")

























