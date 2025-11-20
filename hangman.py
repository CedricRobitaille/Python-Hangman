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

## Get fetch request to the api. Ending with a json parser.
response = requests.get("https://random-word-api.vercel.app/api?words=1").json()
## Results from response comes in as ['word']

## response[0] will then return the single word outside of the array.
lives = 6
word = response[0]

letters = []


for index in range(len(word)):
  letters.append(word[index])

print(letters)
