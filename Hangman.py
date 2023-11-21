# imports
import random
from re import I

# Wordlist used for the game
wordList = ["abruptley", "sandman", "discourage", "heart", "facebook", "python"]

# Game Variables
gameStarted = False
gameWord = ""
gameWordLetters = []
gameGuessedLetters = []
gameAttempts = 0

#   Game board details
gameBoardTiles = []


def newGame():
    global gameWord, gameGuessedLetters, gameWordLetters
    
    gameWord = ""
    gameGuessedLetters = []
    gameWordLetters = []

    newGame = input("Would you like to start a new round? (no)")    
    
    if gameStarted == False:
        if (newGame == "yes"):

            startGame()
        


def startGame():
    global gameAttempts

    # Lets start by choosing a word
    chooseWord()
    gameAttempts = 5
    buildTiles()
    print(gameBoardTiles)
    print("Attempts left: " + gameAttempts)
    
    # We update the (bool)gameStarted to True
    gameStarted = True
    while gameStarted == True:
        if "_" in gameBoardTiles:
            playerGuess = input("Your guess: ")
            if processInput(playerGuess):
                buildTiles()
                print(gameBoardTiles)
        else:
            print("You guessed the word!")
            gameStarted = False
            newGame()
        
    
    
    
def processInput(input):
    if len(input) > 0:
        if input not in gameGuessedLetters:
            gameGuessedLetters.append(input)
            return True


def chooseWord():
    global gameWord
    
    # Lets choose a random word from the (list)wordList
    chooseRandomWord = random.randrange(0, len(wordList))
    
    # We set the (str)gameWord to the chosen word
    gameWord = wordList[chooseRandomWord]
    
    # Lets add all the letters from the word to (list)gameRemainingLetters
    for i in gameWord:
        gameWordLetters.append(i)
        
    return True
    


def buildTiles():
    if len(gameBoardTiles) > 0:
        gameBoardTiles.clear()
        
    for i in gameWordLetters:
        
        if i in gameGuessedLetters:
            
            gameBoardTiles.append(i)
            
            continue
        
        gameBoardTiles.append("_")


newGame();


