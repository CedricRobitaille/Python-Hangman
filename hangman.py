# Hangman Application
## The goal is to have the PC start with a hidden word.
## The user is then requested to guess a letter.
## If the letter is found within the hidden word, it showcases it.
## Otherwise, the bad guess removes a user's life.

### To do this, instead of having an array of 1000 different words hand-written,
### I will attempt to do an API call to: https://random-word-api.vercel.app/api?words=1
### The API is quite simple, request 1 word, receive 1 random word.

### Through a google search, Im seeing I will need to use the `requests` py library.
### This is the article where I learned about the library: https://medium.com/@noorfatimaafzalbutt/fetching-data-through-apis-with-python-a-comprehensive-guide-e3b335de0067
###

## Import Library to do fetch calls
import requests


print("Welcome to Hangman!")
print("How To Play:\nIn order to win, you must guess the random hidden word, 1 letter at a time!\n")


word = ""
letters = []
guesses = []
progress = []
lives = 6


def gameStart():
  word_size = input("To get started, please select a word size:\n# ")
  
  if not word_size.isdigit():
    "Sorry, the value provided is not a valid number."
    gameStart()
    return;
  if int(word_size) < 0 or int(word_size) > 12:
    print("\nSorry, the number provided is out of range.")
    gameStart()
    return;

  print("Loading word...")
  ## Get fetch request to the api. Ending with a json parser.
  ## Results from response comes in as ['word']
  response = requests.get("https://random-word-api.vercel.app/api?words=1&length=" + str(word_size)).json()
  ## response[0] will then return the single word outside of the array.
  global word
  word = response[0]

  for index in range(len(word)):
    letters.append(word[index].lower())
    progress.append("_")

  print(letters)
  print(progress)
  print("A Word has been selected. Good luck!")
  informUser()
  


def userPrompt():
  print("Current Progress:")
  print(" ".join(progress) + "\n")

  user_input = input("Guess a letter:\n> ")
  print("\n\n\n\n\nYou have guessed the letter: " + user_input)

  ### Check that the user's input only contains a single input.
  if len(user_input) == 1:
    ### Check that the user hasn't already guessed that letter!
    if user_input not in guesses:
      guesses.append(user_input.lower()); # .lower to ensure that case does not affect guesses.

      #### User's guess was in the hidden word!
      if user_input in letters:
        for index in range(len(letters)): ## Go through each letter
          if letters[index] == user_input:  ## If the letter matches
            progress[index] = user_input     ## Replace the progress tracker's index
        if "_" not in progress: ## if the progress tracker no longer has empty spots
          print("CONGRATS!!! You guessed the word!")
          continueRequest()
          return;
      
      #### User's guess was not a valid letter
      else: 
        # ! NOTE: I was getting tripped up on this for a while.
        # ! Python treats variable scopes very differently from JS.
        # ! In order to use a global variable locally, I must use the `global` keyword
        global lives
        lives -= 1
        ## BAD GUESS -> Still Alive
        if lives > 0:
          print("Uh oh! Your guess was incorrect!")
          print("You have lost a life.")
        ## DEAD -> End Game
        else:
          print("GAME OVER.\n You ran out of guesses.")
          continueRequest()
          return

      ## Not dead, Continue Playing.
      informUser()
      return

    ## BAD INPUT -> Letter already guessed.
    else:
      print("Sorry, you have already guessed that letter.")
      userPrompt()
      return

  ## BAD INPUT -> Too many letters
  else:
    print("Sorry, " + str(user_input) + " contains too many letters.")
    print("Please guess a single letter.")
    userPrompt()
    return



# Prompt Sequence.
def informUser():
  print("You have " + str(lives) + " lives remaining.\n")
  print("All Letters Guessed:")
  print(", ".join(guesses) + "\n") ## This is CRAZY syntax compared to JS's join method.
  userPrompt()


def continueRequest():
  print("\nWould you like to continue playing?")
  user_input = input("'Y' / 'N' > ")

  validResponses = ["Y", "N"]
  if user_input not in validResponses:
    print("Invalid response...")
    continueRequest()
  elif user_input == "Y":
    global word
    global letters
    global guesses
    global progress
    global lives
    word = ""
    letters = []
    guesses = []
    progress = []
    lives = 6

    gameStart()
  else:
    print("Thanks for playing!")

gameStart()