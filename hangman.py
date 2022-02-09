# PART 1 yes
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1" # sample data, normally the user should choose the difficulty


# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a lettersartszdt
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = [] # this list will contain all the tried letters

def find(letter, list): # sucht letter in liste, gibt boolian
    return any(letter in word for word in list)


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".
guessed_right = [] # contains correct guesses
def Screen(word_as_letters, guessed_right, image, lives): # displays sectret word as "_ " and correct guessed letters.
  word = []
  for i in range(0, len(word_as_letters)):
    if word_as_letters[i] in guessed_right:
      word.append(word_as_letters[i])
      word.append(" ")
    else:
      word.append("_ ")
  print(image[-lives -1])
  print(''.join(str(i) for i in word), sep = "...")
  
  


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4

import random
import hangman_ASCII_art
from hangman_ASCII_art import *

def difficulty_level():
  image = []
  image.clear()
  lives = 0
  while True:
     print("-DIFFICULTY-")
     print("[1]EASY\n[2]NORMAL\n[3]HARD")
     difficulty = input("Please choose your difficulty:")
     if difficulty == "1":
       lives = 7
       image = diff_1
     elif difficulty == "2":
       lives = 5
       image = diff_2
     elif difficulty == "3":
       lives = 3
       image = diff_3
     else:
       print("Please choose difficulty 1, 2 or 3")
       continue
    
     return lives, image

#with open("countries-and-capitals") as f:
   # lines = f.readlines()
#f = open("countries-and-capitals.txt", "rt")
def get_random_countries():
  lines = []
  f = open("countries-and-capitals.txt")
  lines = f.readlines()
  lines
  countries = []
  for country in lines:
    countries.append(country.split('|')[0].strip())
  return random.choice(countries)
  #print(random.choice(countries))

def new_game(runtime):
  loop = True
  while loop == True:
    yn = input("Do you want to play again?(y/n)")
    if yn == "y":
      print("-NEW GAME-")
      loop = False
    elif yn == "n":
      print("bye")
      runtime = False
      loop = False
    else:
      print("please write y or n!")
  return runtime
  
#MAIN-----------------------------------------------------------------------------------------------------------------------------------------
runtime = True
word_as_letters = []
while runtime == True:
  win_count = 0
  word_as_letters.clear()
  guessed_right.clear()
  already_tried_letters.clear()

  lives, image = difficulty_level() #set difficulty
  word_to_guess = get_random_countries()
  for i in range(0, len(word_to_guess)):
      word_as_letters.append(word_to_guess[i].upper())
      word_as_letters.strip()
  #print(word_as_letters)
  #print(word_as_letters[3])

  #print(''.join(str(i) for i in word_as_letters), sep = "...")

  #print("_ " * len(word_to_guess)) #quasi step 3

  valid_guess = False

  #for i in range(0, len(word_as_letters)):
    #guessed_right.append(" ")

  while valid_guess == False: 
    Screen(word_as_letters, guessed_right, image, lives)
    print(f"Lives: {lives}") 
    print(word_to_guess)
    guess = input("Guess a letter\n(Type \"QUIT\" to quit the Game)").upper() # get input as upper (guess)
    if len(guess) > 1:
      if guess== "QUIT":
        print("bye")
        valid_guess = True
        runtime = False
      else:
        print("Please just one letter!") #below has just one letter
    else:
      if find(guess, already_tried_letters) == True:
        print(f"---------------\nYou've allready tried this letter!\nAlready tried letters: {already_tried_letters}")
      else:
        already_tried_letters.append(guess)
        if find(guess, word_as_letters) == True: # shows if input is in the word.
          print("---------------\nhurray")
          guessed_right.append(guess) #adds guess to guessed_right
          win_count = win_count + 1 * word_as_letters.count(guess) #counts correct letters
          if len(word_as_letters) == win_count:
            print("!!!YOU WON!!!")
            valid_guess = True
            runtime = new_game(runtime)
        else:
          print("---------------\nbooooo")
          lives = lives - 1
          if lives == 0:
            Screen(word_as_letters, guessed_right, image, lives)
            print(f"-GAME OVER-\nThe correct word is {word_to_guess}.")
            valid_guess = True
            runtime = new_game(runtime)

# now we just have to define win and lose
#then we can clean up
#maybe add some features


    