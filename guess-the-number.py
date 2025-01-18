import matplotlib.pyplot as plt
import random


number= random.randint(1,100)
print(number)

userguesses = []


print('I have a number in mind and you have to guess.\
	   \nIt is an integer between 0 and 100')


while 1:
	userinput= input("Guess an integer:")
	while not userinput.isdigit():
		userinput= input("not integer, Guess an integer:")
	userinput= int(userinput)
	userguesses.append(userinput)

	if userinput == number:
		print("you win")
		break
	elif userinput < number:
		print('Go up')		
	else:
		print('Go down')




print('you have ', len(userguesses), 'atempts')
print(f"You have {userguesses} atempts.")


# Plotting
myX = []
for i in range(len(userguesses)):
	i+=1
	myX.append(i)
	
plt.figure(figsize= (15,5))
plt.title('user progress toward the target')
plt.xlabel('number of atempts')
plt.ylabel('user atempts')
plt.plot(myX, userguesses, len(userguesses), number, '*', markerfacecolor= 'r', markersize=50, markeredgecolor= 'r')
plt.show()
