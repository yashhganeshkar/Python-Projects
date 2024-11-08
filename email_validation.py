

def email_Validation(email):

	k,j,l = 0,0,0
	try:
		if(len(email)>=6):
			if(email[0].isalpha()):
				if((email[-4]=='.') or (email[-3]=='.')):
					if(('@' in email) and (email.count('@') == 1)):
						for i in email:
							if(i == i.isspace()):
								k = 1
							elif(i.isalpha()):
								if(i == i.upper()):
									j = 1
							elif(i.isdigit()):
								continue
							elif(i == '_' or i == '.' or i == '@'):
								continue
							else:
								l = 1
						if(k == 1 or j == 1 or l == 1):
							print("Invalid Email")
						else:
							print("Valid Email")
					else:
						print("Invalid Email")
				else:
					print("Invalid Email")
			else:
				print("Invalid Email")
		else:
			print("Invaalid Email")
	except TypeError as e:
		print(f"Error Found = {e}")	
	

email = input("Enter Your Email = ")

email_Validation(email)
