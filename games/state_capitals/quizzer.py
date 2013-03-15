"""
Concepts introduced: 
- opening and reading files
- importing a single function from a standard module
"""

from random import choice
import sys

def getquizfile():

  flashcards = []
  f = open('state_capitals.txt', 'r')
  for line in f:
    line = line.strip().split(',')
    flashcards.append(line)
  return flashcards

def playthegame(flashcards):

  while flashcards:
    x = choice(flashcards)
    question = x[0]
    answer = x[1]

    y = raw_input('%s: ' % (question) )
    if y.lower() == 'exit':
      sys.exit()
    elif y.lower() == answer.lower():
      print "Correct!"
      flashcards.remove(x)
    else:
      print "That is not correct, the answer is %s." % (answer)

if __name__ == '__main__':
  quizfile = getquizfile()
  playthegame(quizfile)

