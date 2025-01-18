import matplotlib.pyplot as plt
import random
import sqlite3
import json


class GuessingGame:
   '''
   A class to represent the whole game
   '''

   def __init__(self, upper: int, lower: int):
      self.upper = upper
      self.lower = lower
      self.secretNumber = 0
      self.userguesses = []

   def startGame(self):
       self.secretNumber = random.randint(self.lower,self.upper)
    #    print(f"I have a number in mind and you have to guess.\
	#    \nIt is an integer between {self.lower} and {self.upper}")

    
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

class DataBaseManager():

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def createTable(self, table_name: str):
        self.query =f"CREATE TABLE IF NOT EXISTS {table_name} ( id INTEGER PRIMARY KEY AUTOINCREMENT, atempts TEXT NOT NULL, numberOfGuesses INTEGER NOT NULL, number INTEGER NOT NULL)"
        self.cursor.execute(self.query)
        db.connection.commit()  

    def insertAtemptsData(self, userguesses, secretNumber):
        userguesses_json = json.dumps(userguesses)
        db.cursor.execute('INSERT INTO atemptsData (atempts, numberOfGuesses, number) VALUES (?,?,?)', (userguesses_json, len(userguesses), secretNumber))
        db.connection.commit()

    def fetchAgame(self, id):
        ''' retrive one raw from db using id'''
        self.cursor.execute('SELECT * FROM atemptsData WHERE id=?', (id,))
        result = self.cursor.fetchall()
        return result

    
    def fetchAtempt(self, id):
        ''' retrive atempts array from db using id'''
        result = self.fetchAgame(id)
        atempts_array = json.loads(result[0][1])
        return atempts_array

if __name__ == "__main__":
    
    db = DataBaseManager('guessGameResult.db')
    db.createTable("atemptsData")

    for runs in range(1000):
        guessing_game = GuessingGame(1000, 1)
        guesser = Guesser(guessing_game.getUpper(), guessing_game.getLower())
     
        guessing_game.startGame()
        
        while guesser.guess != guessing_game.secretNumber:   
            guesser.createNewGuess()
            guesser.reciveHint(guessing_game.isItTheNumber(guesser.guess))

        db.insertAtemptsData(guessing_game.userguesses, guessing_game.secretNumber)


    

    db.connection.close()