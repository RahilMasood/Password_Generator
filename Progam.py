import string
import random

# Getting password length
l = int(input("Enter password length: "))

print('''Choose what your password should include from these: 
		1. Letters
		2. Digits
		3. Special characters
		4. Exit''')

cl = " "

# For checking the strength of passwords
strength_count = []

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		strength_count.append(1)
		# Adding letters to possible characters
		cl += string.ascii_letters
	elif(choice == 2):
		strength_count.append(2)
		# Adding digits to possible characters
		cl += string.digits
	elif(choice == 3):
		strength_count.append(3)
		# Adding special characters to possible characters
		cl += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(l):

	# Picking a random character from our character list
	rc = random.choice(cl)
	
	# appending a random character to password
	password.append(rc)

# printing password
print("The random password generated is " + "".join(password))
sc = set(strength_count)

# Having a password less than 8 charecters makes it weak
if l < 8:
    sc = [0]

if len(sc) == 3:
    print("Password strength: VERY STRONG")
elif len(sc) == 2:
    print("Password strength: STRONG")
elif len(sc) == 1:
    print("Password strength: WEAK")
else:
    print('Password Strength: VERY WEAK')
