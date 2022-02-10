# FUNCTIONS
def find(letter, list): # is letter in list? True/False
  return any(letter in word for word in list)
#-------------------------------
def Screen(guessed_right, image, lives, word_to_guess): # displays sectret word as "_ " and correct guessed letters.
  word = ""
  for i in range(0, len(word_to_guess)):
    if word_to_guess[i].upper() in guessed_right:
      word = word + word_to_guess[i] + " "
    else:
      word = word + "_ "
  print(image[-lives -1])
  print(word)#.capitalize())
#-----------------------------------
def difficulty_level():
  image = []
  image.clear()
  lives = 0
  while True:
     print("-DIFFICULTY-")
     print("[1]EASY\n[2]NORMAL\n[3]HARD")
     difficulty = input("Please choose your difficulty:")
     print()
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
#-----------------------------------------------
def get_random_countries():
  lines = []
  f = open("countries-and-capitals.txt")
  lines = f.readlines()
  valid_input = False
  while valid_input == False:
    chocaco = input("-WORDLISTS-\n[co]COUNTRIES\n[ca]CAPITALS\nMake your choice: ")
    countries = []
    capitals = []
    if chocaco == "co":
      for country in lines:
        countries.append(country.split('|')[0].strip())
      return random.choice(countries)
    elif chocaco == "ca":
      for capital in lines:  
        capitals.append(capital.split('|')[-1].strip())
      return random.choice(capitals)
    else:
      print ("You have to choose between \"co\" and \"ca\" ")
#----------------------------------------------------------------
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
#------------------------------------------------------------------------------
#-------------------------------------------MAIN-------------------------------------------------------------------------------
#Variables:
import random
from hangman_ASCII_art import *
runtime = True
guessed_right = []
already_tried_letters = []
word_as_letters = []
#-----------------------------------------------gameloop:--------------------------------------------
while runtime == True:
  # clear variables:
  godmode = False
  win_count = 0
  word_as_letters.clear()
  guessed_right.clear()
  already_tried_letters.clear()
  # set variables:
  lives, image = difficulty_level() #set difficulty
  word_to_guess = get_random_countries() #set word_to_guess
  for i in range(0, len(word_to_guess)):
      word_as_letters.append(word_to_guess[i].upper())
  if " " in word_as_letters:
    guessed_right.append(" ")
    win_count = win_count + 1
  valid_guess = False
  while valid_guess == False: 
    Screen(guessed_right, image, lives, word_to_guess)
    print(f"Lives: {lives}") 
    if godmode == True: # print the solution if godmode is on
      print(f"Solution: {word_to_guess}")
    guess = input("Guess a letter\n(Type \"QUIT\" to quit the Game)").upper() # get input as upper (guess)
    if len(guess) > 1:
      if guess == "QUIT":
        print("bye")
        valid_guess = True
        runtime = False
      elif guess == "GODMODE": # enables godmode/ cheatmode
        godmode = True
      else:
        print("Please just one letter!") #below has just one letter
    else:
      if guess.isalpha() == True:
        if find(guess, already_tried_letters) == True:
          print("-" * 23, f"\nYou've allready tried this letter!\nAlready tried letters: {already_tried_letters}")
        else:
          already_tried_letters.append(guess)
          if find(guess, word_as_letters) == True: # shows if input is in the word.
            print("-" * 23, "\nhurray")
            guessed_right.append(guess) #adds guess to guessed_right
            win_count = win_count + 1 * word_as_letters.count(guess) #counts correct letters
            if len(word_as_letters) == win_count:
              Screen(guessed_right, image, lives, word_to_guess)
              print("!!!YOU WON!!!")
              valid_guess = True
              runtime = new_game(runtime)
          else:
            print("-" * 23, "\nbooooo")
            lives = lives - 1
            if lives == 0:
              Screen(guessed_right, image, lives, word_to_guess)
              print(f"-GAME OVER-\nThe correct word is {word_to_guess}.")
              valid_guess = True
              runtime = new_game(runtime)
      else:
        print("Please try a letter!")

