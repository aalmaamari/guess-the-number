import random

# Generating the secret number
number= random.randint(1,100)

userguesses = []


print('I have a number in mind and you have to guess.\
	   \nIt is an integer between 0 and 100')


while 1:
    # Prepare user input
	userinput= input("Guess an integer:")
	while not userinput.isdigit():
		userinput= input("not integer, Guess an integer:")
	userinput= int(userinput)
	userguesses.append(userinput)

	# Evaluate The guess
	if userinput == number:
		print("you win")
		break
	elif userinput < number:
		print('Go up')		
	else:
		print('Go down')




print('you have ', len(userguesses), 'atempts')
print(f"Here are your guesses: {userguesses}.")