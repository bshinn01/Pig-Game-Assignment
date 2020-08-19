#**********************************
# *  Name  : Breanna Shinn
# * Pledge : I pledge my honor that I have abided by the Stevens Honor System.
# *        :
#**********************************

'''
4-Dice Pig

Adapted from Java to Python by Justin Barish,  11/2018
Modified nov '19 by Toby Dalton

~ ~ ~

To exercise your looping ability, we're going to be filling in a bunch
of blanks. yay!

Pig is a game where players take turns rolling dice.
Traditionally, it's only 2, but this is a variant.

The goal is to have their total score reach a certain # of points.
Players take turns earning points by rolling dice.
Each roll adds that sum onto a round score, which may or may not be added
to their total score, dictated as below:

A person's turn lasts until they want to stop rolling or roll some 1s.

If at any point during the player's turn they roll one 1:
their round ends and their round score is added to their total score.

If they roll two 1s:
they lose all points for the round, and their turn is over.

Three 1s:
they lose all of their points in the game, and their turn is over.

If they recieve the luck of four 1s (four-eyed snake ::S):
they immediately lose the game.

Whenever the player decide to stop their turn, their round points are 
added to their total points.

When a player's total points reach 100 (controllable below), they win.
'''
import random

POINTS_TO_WIN = 100
AI_ROUND_TARGET = 20
fromLoss = False

'''
This Homework has 2 parts:

Part 1 (100 pts): Complete the game for two human players.
That is, fill in all of the methods below

Part 2 (15 pts Extra Credit):
Add in an "AI" as the second player, so you will play against the computer.
The AI takes the place of player 2, and will continue rolling until
it reaches its AI_ROUND_TARGET. NOTE: You *will* need to change some of the
function paramaters (I.E. pass in additional values) and other parts of
functions.
'''

#**   
#**   General Game Stuff
#**

def main():
  '''This is the main function for the pig game'''
  welcome()
  while True:
    # Extra Credit: Choose whether or not to AI for each game, and do the rest.
    playGame()
    if not wantsPlayAgain():
      print('Bye!')
      return

# TODO
def playGame():
  '''Play one game of pig
  Alternates between players, and at the end of a player's turn, 
  prints the overall game score for both players'''

  player = 1
  scores = initScores()
  while not gameOver(scores, fromLoss):
    print()
    print('Current Scores:')
    printScore(scores)
    getMove(scores, player)
    if player == 1:
      player = 2
    else:
      player = 1
    


# TODO
def initScores():
  '''initialize the scores to 0'''
  scores = [0,0]
  return scores


# TODO
def gameOver(scores, fromLoss):
  '''checks if the game is over
  game is over when either player reaches >= POINTS_TO_WIN.
  [ or 4 ones are rolled :3]
  Prints the win message for the player who won
  If no one won, just returns false'''
  if fromLoss == False:
    if scores[0] >= POINTS_TO_WIN:
      printWinMessage(1, scores)
      return True
    elif scores[1] >= POINTS_TO_WIN:
      printWinMessage(2, scores)
      return True
    return False
  else:
    return True


# TODO  
def getMove(scores, player):
  '''gets a player's move.
  Before every move, prints the current round score and the game score for the player.
  Checks if the player wants to continue, and if they do, rolls dice and appropriately changes scores
  '''
  printPlayerMessage(player)
  roundScore = 0

  while True:

    roll = rollDice()

    countOnes = 0
    for die in roll:
      roundScore += die
      if die == 1:
        countOnes += 1

    showRoll(roll)

    printCurrentPlayerScore(scores, player, roundScore)
    
    if countOnes == 4:
      print("Rolled four 1s... Game over")
      if player == 1:
        printWinMessage(2, scores)
      else:
        printWinMessage(1, scores)
      fromLoss = True;
      gameOver(scores, fromLoss)
      break

    elif countOnes == 3:
      print("Rolled three 1s. Score reset!")
      if player == 1:
        scores[0] = 0
      else:
        scores[1] = 0
      break

    elif countOnes == 2:
      print("Rolled two 1s! Round ended, no score added")
      roundScore = 0
      if player == 1:
        player = 2
      else:
        player = 1
      break

    elif countOnes == 1:
      print("Rolled one 1! Round ended, score added")
      if player == 1:
        scores[0] += roundScore
        player = 2
      else:
        scores[1] += roundScore
        player = 1
      break

    else:
      if wantsRollAgain(player) == False:
        if player == 1:
          scores[0] += roundScore
          player = 2
          break
        elif player == 2:
          scores[1] += roundScore
          player = 1
          break
        
def rollDie():
  '''rolls a single die (wow)'''
  return random.randint(1,6)

# TODO
def rollDice():
  '''grabs the roll for four dice'''
  return [rollDie(), rollDie(), rollDie(), rollDie()]

#**   
#**   Checking if we want to [X] again
#**

# TODO
def wantsContinue(response):
  '''Checks if the response a user gives indicates they want to continue.
  assume the user has to give a Y to mean yes and N to mean no'''
  if response == 'Y':
      return True
  elif response == 'N':
    return False

# TODO  
def wantsPlayAgain():
  '''Asks a player if they want to play the game again (use wantsContinue()!)'''
  response2 = input('Would you like to play again? Y/N ')
  return wantsContinue(response2)
  

# TODO
def wantsRollAgain(player):
  '''Asks a player if they want to roll again
  For Part 2, also handle the Computer's decision'''
  print(str(player) + ': ')
  response1 = input('Would you like to roll again? Y/N ')
  return wantsContinue(response1)

#**   
#**   Printing Things
#**

def welcome():
  '''Prints the welcome message for the game.
  We might also print the rules for the game and any other
  information that the user might need to know.'''
  print('Welcome to Pig!')

# TODO
def printScore(scores):
  '''prints the current game score for each player'''
  print('Player 1\'s current score is ' + str(scores[0]))
  print('Player 2\'s current score is ' + str(scores[1]))

def printWinMessage(winningPlayer, scores):
  print()
  print('***********************Player ' + str(winningPlayer) + ' Won!************************')
  print('***********************Final Score:*************************')
  printScore(scores)

# TODO
def showRoll(roll):
  ''' prints out the roll'''
  print(str(roll))

def printPlayerMessage(player):
  print()
  print('--------------------------------------------------------------')
  print('-------------------Player ' + str(player) + '\'s turn----------------------------')
  print('--------------------------------------------------------------')
  print()

# TODO
def printCurrentPlayerScore(scores, player, roundScore):
  '''print the score for a specific player. Prints their round score 
  and their overall game score not including their current round score'''
  if player == 1:
    print('Your current round score is ' + str(roundScore))
    print('Your current game score (not including the current round) is ' + str(scores[0]))
  elif player == 2:
    print('Your current round score is ' + str(roundScore))
    print('Your current game score (not including the current round) is ' + str(scores[1]))

if __name__ == '__main__':
  main()






  
