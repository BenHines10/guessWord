import random

word = ""
wins = 0
losses = 0
letterList = []
playAgain = True
userDefinedPath = "C:\\Users\\jhine\\Desktop\\words.txt"

def generateWord(filepath):
    filepath = ("")
    f = open(userDefinedPath)
    words = f.read()
    words = words.split("\n")
    word = random.choice(words)
    word = word.upper()
    word = list(word)
    print("Word = " + "".join(word))
    return word

def buildWord(letterList, word):
    deliveredWord = ["_ "] * len(word)
    for i in range(len(word)):
        for j in range(len(letterList)):
            if letterList[j] == word[i]:
                deliveredWord[i] = letterList[j]
    return deliveredWord

def checkSuccess(deliveredWord, word, userInput):
    message = ""
    print("Success so far: " + "".join(buildWord(deliveredWord, word)))
    if "".join(buildWord(letterList, word)) == "".join(word):
        message = "You won."
    else:
        message = "You're not finished yet..."
    return message

while playAgain == True:
    word = generateWord(userDefinedPath)
    gameLength = len(word) + 5
    print("Game starting...")
    for i in range(gameLength):
        userInput = input(
            "Input \'L\' to guess a letter, \'W\' to guess a word: \n")
        # Necessary to apply the string altering functions like .upper(), etc
        str(userInput)
        userInput = userInput.strip().upper()[:1]
        if userInput == "L":
            userInput = input("Guess a letter: \n")
            str(userInput)
            userInput = userInput.strip().upper()[:1]
            letterList.append(userInput)
            print("Success so far: " + "".join(buildWord(letterList, word)))
            if "".join(buildWord(letterList, word)) == "".join(word):
                print("You won.")
                break
            else:
                print("You're not finished yet...")
        elif userInput == "W":
            userInput = input("Guess a word: \n")
            str(userInput)
            userInput = userInput.strip().upper()
            if str(userInput) == "".join(word):
                wins += 1
                print("You won. Total wins = " + str(wins) + ". Total loses = " + str(losses))
                break
            else:
                print("Incorrect...")
        else:
            print("Input not recognized.")
        i += 1
    if i >= gameLength:
        losses += 1
        print("You ran out of attempts. You lost. Total wins = " + str(wins) + ". Total loses = " + str(losses))
    userInput = input("Play Again? (Y/N): ")
    userInput = userInput.strip().upper()[:1]
    if userInput == "Y":
        playAgain = True
    else:
        playAgain = False
        print("Exiting...")
