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

    
   def isItTheNumber(self,machineGuess):
       self.userguesses.append(machineGuess)
       if machineGuess < self.secretNumber:
           return "Go up"
       else:
           return "Go down"
       
   def __str__(self):
      return f"You WIN.\nYou have {len(self.userguesses)} atempts.\natempts are : {self.userguesses} "  

   def getUpper(self):
       return self.upper
     
   def getLower(self):
       return self.lower
     
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



class Guesser():
    '''
    A class to represent the guessing machine (The Guesser)
    '''
    def __init__(self, upper: int, lower: int):
        self.upper = upper
        self.lower = lower
        self.guess = 0

    def createNewGuess(self):
        self.guess = random.randint(self.lower, self.upper)

    def reciveHint(self, hint):
        if hint == "Go up":
            self.lower = self.guess
        else:
            self.upper = self.guess
        
          

if __name__ == "__main__":
    guessing_game = GuessingGame(1000, 1)
    guesser = Guesser(guessing_game.getUpper(),guessing_game.getLower())
    
    guessing_game.startGame()
    
    while guesser.guess != guessing_game.secretNumber:   
        guesser.createNewGuess()
        guesser.reciveHint(guessing_game.isItTheNumber(guesser.guess))
    
    print(guessing_game)
    guessing_game.plotGuesses()
    