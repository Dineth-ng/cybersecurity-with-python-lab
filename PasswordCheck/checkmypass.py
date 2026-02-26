
#Checks:
#	Length
#	Uppercase letters
#	Numbers
#	Special characters






def check_security_l1():
	mark = 0 
	passUpper = 0

	is_len = False
	has_upper = False	
	special_letter  = False
	user_digit = False	
	#first check length:

	userpass = input(">> Enter Your password : ")
	
	
	if len(userpass) <=8 :
		print(">>[1] condition is fail ....")
	
	else:
		print(">>[1] condition is pass ....")
		mark = mark + 1
		is_len = True
	
	#second Uppercase letters:
	for char in userpass:
		if char.isupper():
			passUpper = passUpper + 1
		
	
	if passUpper >= 2:
		print(">>[2] condition is pass ....")
		mark = mark + 1
		has_upper = True
	else:
		print(">>[2] condition is fail ....")
	
		
	
	#check specialchar

	special_char = "!@#$%^&*()_+=-{}|:?>,`"
	special_mark = 0 
	for i in userpass:
		for z in special_char:
			if i == z:
				special_mark = + 1
		

	if special_mark >= 1:
		print(">>[3] condition is pass ....")
		special_letter = True
		mark = mark + 1
	else:
		print(">>[3] condition is fail ....")
	

	checkNum = 0 
	#check number
	for i in userpass:
		if i.isdigit():
			checkNum = checkNum + 1
	
	
	if checkNum >= 3:
		user_digit = True
		print(">>[4] condition is pass....")
		mark = mark + 1
	else :
		print(">>[4] condition is fail ....")

	# Give result 

	match mark:
		case 1 :
			output = "Weak password"
		case 2 :
			output = " Weak Password"
		case 3 :
			output = " Normal Password"
		case 4 : 
			output = " Good Password " 		
		
	print("\n>> Your Password is :-> " , output)




print(">> Protec Your Self" )
print("\n[1] password strong check \t [2] password security check \n[3] try dictionary attack \t [99] exit ")
userinput = input(">> ")

match userinput:
	case 1:
		check_security_l1()
	case 2:
		print(">> coming soon:")
	case 2:
		print(">> coming soon:")
	case 99:
		print(">> Exiting ...")
