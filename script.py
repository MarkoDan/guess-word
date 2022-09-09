import random

MAX_GUESSES = 10
words = [
'computer','phone','car','house',
'watch','glasses','keyboard','tree',
'pen','book','wallet', 'dog'
]

randomIndex = random.randrange(0, len(words))

def guessWords(words):
    numGuesses = 1
    while True:
        while numGuesses <= MAX_GUESSES:
            guess = input(f"Guess the word *{shuffleWord(words[randomIndex])}*")
            if guess != words[randomIndex]:
                continue
            else:
                break
        numGuesses += 1
        if numGuesses > MAX_GUESSES:
            print("You ran out of guesses.")
            
        
        
def shuffleWord(word):
    shuffled = ""
    array = []
    i = 0
    while i < len(word):
        number = random.randrange(0, len(word))
        if number not in array:
            shuffled += word[number]
            i += 1
        array.append(number)
    return shuffled


guessWords(words)