import matplotlib.pyplot as plt
import random



class GuessingGame:
   '''
   A class to represent the whole game
   '''

   def __init__(self, upper: int, lower: int):
      self.upper = upper
      self.lower = lower
      self.secretNumber = random.randint(lower,upper)
      self.userguesses = []

   def startGame(self):
       print(f"I have a number in mind and you have to guess.\
	   \nIt is an integer between {self.lower} and {self.upper}")

    
   def testGuess(self,userInput):
       self.userguesses.append(userInput)
       if userInput < self.secretNumber:
           print('Go up')
       else:
           print('Go down')
       
   def __str__(self):
      return f"You WIN.\nYou have {len(self.userguesses)} atempts.\natempts are : {self.userguesses} "  
       
   def plotGuesses(self):
        myX = []
        for i in range(len(self.userguesses)):
            i+=1
            myX.append(i)
            
        plt.figure(figsize= (15,5))
        plt.title('user progress toward the target')
        plt.xlabel('number of atempts')
        plt.ylabel('user atempts')
        plt.plot(myX, self.userguesses, len(self.userguesses), self.secretNumber, '*', markerfacecolor= 'r', markersize=50, markeredgecolor= 'r')
        plt.show()




if __name__ == "__main__":

 guessing_game = GuessingGame(100, 0)

 guessing_game.startGame()

 userInput = 0
 while userInput != guessing_game.secretNumber: 
  userInput= input("Guess an integer:")
  while not userInput.isdigit():
    userInput= input("not integer, Guess an integer:")
  userInput= int(userInput)
  guessing_game.testGuess(userInput)

      
  
 print(guessing_game)
 guessing_game.plotGuesses()