#!/anaconda2/bin/python

import re
import json
from datetime import datetime

print('-------------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------')
print('                              Scrabble Scorecard                                     ')
print('-------------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------')
print('Enter all words made in a turn separated with space. For e.g.: TIGER TWO')
print('Enter double/triple letter words within () after the letter. For e.g: TIG(2)ER TW(3)O')
print('Enter double/triple word within [] after the word. For e.g.: TIG(2)ER[2] TW(3)O[3]')
print('Enter blank letter with (0) after the letter. For e.g.: T(0)IGER T(0)WO')
print('-------------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------')

# Dic of Scrabble points
LETTERPOINTDICT = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

# Set of valid characters
VALIDCHARS = set('abcdefghijklmnopqrstuvwxyz023()[] ')

# List of markup characters
MARKUPCHARS = ['(', '0', '2', '3', ')', '[', ']']

# Get the number of players
while True:
    rawinput = raw_input('Enter number of players playing the game (1-4): ').strip()

    if set(rawinput) <= set('1234') and len(rawinput) > 0:
        break

numberofplayers = int(rawinput)

print('-------------------------------------------------------------------------------------')

# Get the names of the players
index = 0
players = []
while index < numberofplayers:
    playername = ''
    while len(playername) == 0:
        playername = str(raw_input('Enter player name: '))

    players.append(playername)
    index = index + 1

runningpoints = [0] * numberofplayers

print('-------------------------------------------------------------------------------------')

# This list will save all the moves of the game
game = []

# Start the game
while True:
    playerindex = 0
    while playerindex < numberofplayers:
        # Strictly allow only valid characters that we can process.
        # We will keep asking for the input till we get a valid one
        while True:
            rawinput = str(raw_input('Enter words by player ' + players[playerindex] + ': ')).strip().lower()
            if set(rawinput) <= VALIDCHARS and len(rawinput) > 0:
                break

        words = rawinput.split()
        
        # Now we need to parse the words based on the following rules:
        # Double/Triple letter is denoted with (2) or (3) just after the letter
        # Blank tile will be denoted with (0) just after the letter
        # Double/Triple word is denoted with [2] or [3] just after the word
        turnpoints = 0
        turnwords = []
        for word in words:
            bonusletters = list([m.start() for m in re.finditer('\([023]\)', word)])
            bonusletterindex = [index - 1 for index in bonusletters]

            # Calculate points
            wordpoints = 0
            letters = list(word)
            for index, letter in enumerate(letters):     
                letterbonus = 1
                if index in bonusletterindex:
                    letterbonus = int(letters[index+2])
                
                if letter not in MARKUPCHARS:                    
                    wordpoints = wordpoints + LETTERPOINTDICT[letter] * letterbonus

            # Check if there is word bonus
            if letters[-1] == ']' and letters[-3] == '[':
                wordpoints = wordpoints * int(letters[-2])

            plainword = ''.join( c for c in word if  c not in MARKUPCHARS)
            print(plainword.upper() + ' - ' + str(wordpoints))

            # Save the words
            turnword = {}
            turnword['PLAINWORD'] = plainword.upper()
            turnword['WORDPOINTS'] = wordpoints
            turnwords.append(turnword)

            turnpoints = turnpoints + wordpoints

        # Add bonus points if all tiles used
        bonuspoints = 50 if str(raw_input('Add 50 bonus points? (y/n): ')) == 'y' else 0
        turnpoints = turnpoints + bonuspoints

        print('Points earned in this turn: ' + str(turnpoints))  

        # Soring the final points
        runningpoints[playerindex] = runningpoints[playerindex] + turnpoints

        # Save the turn data in a dictionary
        turn = {}
        turn['PLAYER'] = players[playerindex]
        turn['TURNWORDS'] = turnwords
        turn['BONUSPOINTS'] = bonuspoints
        turn['TURNPOINTS'] = turnpoints
        turn['RUNNINGPOINTS'] = runningpoints[playerindex]

        # Append turn to game
        game.append(turn)

        # Next player
        playerindex = playerindex + 1

        print('-------------------------------------------------------------------------------------')

    print('-------------------------------------------------------------------------------------')
    
    # Show current points status
    for index, player in enumerate(players):
        print(player + ': ' + str(runningpoints[index]))

    print('-------------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------------')

    continuegame = str(raw_input('Continue? (y/n): '))
    if continuegame == 'n':
        break
    
    print('-------------------------------------------------------------------------------------')

# Save the game to a file
filename = datetime.now().strftime('%d-%b-%Y-%H-%M') + '.txt'
with open(filename, 'w') as gamefile:
    gamefile.write(json.dumps(game))
