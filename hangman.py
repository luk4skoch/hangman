# FUNCTIONS
def Credits():
  print("\033[1;33;48m-CODED BY-\nDaniel Kaltner\nLukas Koch\n-BACKGROUNDMUSIC-\nThe Hanging Tree [Lorenzotanyl] [Progressive Psy Remix]")
#--------------------------------------------------------------
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
  print("\033[1;37;48m", image[-lives -1])
  print(word)
#-----------------------------------
def difficulty_level():
  image = []
  image.clear()
  lives = 0
  while True:
     #print("\033[1;34;48m-HANGINGTREE-\033")
     #print("\033[1;34;48m-DIFFICULTY-\033")
     #print("\033[1;32;48m[1]EASY\n\033[1;33;48m[2]NORMAL\n\033[1;31;48m[3]HARD\033")
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
       print("\033[1;31;48mPlease choose difficulty 1, 2 or 3\033")
       continue
     return lives, image
#-----------------------------------------------
def get_random_countries():
  lines = []
  f = open("countries-and-capitals.txt")
  lines = f.readlines()
  valid_input = False
  while valid_input == False:
    chocaco = input("\033[1;34;48m-WORDLISTS-\n\033[1;36;48m[co]COUNTRIES\n[ca]CAPITALS\n\033[1;34;48mMake your choice: ")
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
      print ("\033[1;31;48mYou have to choose between \"co\" and \"ca\" \033")
#----------------------------------------------------------------
def new_game(runtime):
  loop = True
  while loop == True:
    yn = input("\033[1;34;48mDo you want to play again?(y/n)")
    if yn == "y":
      print("-NEW GAME-")
      loop = False
    elif yn == "n":
      Credits()
      runtime = False
      loop = False
    else:
      print("please write y or n!")
  return runtime
#---------------------------------------------------------------------------------------
#------------------------------------------------MAIN-----------------------------------
#Variables:
import random
from hangman_ASCII_art import *
from playsound import playsound
runtime = True
guessed_right = []
already_tried_letters = []
word_as_letters = []
playsound("background_music.mp3", False)
#-------------------------------------------------Title---------------------------------
print(open("tree.txt").read())
#-----------------------------------------------gameloop:-------------------------------
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
    if lives < 4:
      print(f"\033[1;31;48mLives: {lives}\033") 
    elif lives > 5:
      print(f"\033[1;32;48mLives: {lives}\033")
    else:
      print(f"\033[1;33;48mLives: {lives}\033")
    if godmode == True: # print the solution if godmode is on
      print(f"\033[1;31;48mSolution: {word_to_guess}")
    guess = input("\033[1;34;48mGuess a letter\n(Type \"QUIT\" to quit the Game)").upper() # get input as upper (guess)
    if len(guess) > 1:
      if guess == "QUIT":
        Credits()
        valid_guess = True
        runtime = False
      elif guess == "GODMODE": # enables godmode/ cheatmode
        godmode = True
      else:
        print("\033[1;31;48mPlease just one letter!\033") #below has just one letter
    else:
      if guess.isalpha() == True:
        if find(guess, already_tried_letters) == True:
          print("-" * 23, f"\n\033[1;31;48mYou've allready tried this letter!\n\033[1;33;48mAlready tried letters: {already_tried_letters}\033")
        else:
          already_tried_letters.append(guess)
          if find(guess, word_as_letters) == True: # shows if input is in the word.
            print("-" * 23, "\n\033[1;32;48mhurray\033")
            guessed_right.append(guess) #adds guess to guessed_right
            win_count = win_count + 1 * word_as_letters.count(guess) #counts correct letters
            if len(word_as_letters) == win_count:
              Screen(guessed_right, image, lives, word_to_guess)
              print("\033[1;32;48m!!!YOU WON!!!\033")
              valid_guess = True
              runtime = new_game(runtime)
          else:
            print("-" * 23, "\n\033[1;31;48mbooooo\033")
            lives = lives - 1
            if lives == 0:
              Screen(guessed_right, image, lives, word_to_guess)
              print(f"\033[1;31;48m-GAME OVER-\nThe correct word is {word_to_guess}.\033")
              valid_guess = True
              runtime = new_game(runtime)
      else:
        print("\033[1;31;48mPlease try a letter!\033")