import random
import hangman_art
import hangman_words

#Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

#Create a variable called 'lives' to keep track of the number of lives left. 
lives = 6
end_of_game = False

#Import the logo from hangman_art.py and print it at the start the game.
print(hangman_art.logo)

#Create blanks
display = []
for letter in range(len(chosen_word)):
    display.append("_")

#Create a list with the wrong attempts.
wrong_choices = []

#Create a loop until the game ends.
while not end_of_game:
    #User make a guess.
    user_choice = input("Make a guess: ") 
    guess = user_choice.lower()

    #Print the letter if the user has entered a letter they've already guessed.
    if guess in display:
        print(f"You've already guessed {guess}.")
  
    #Check guessed letter.
    position = 0
    for letter in chosen_word:
        position += 1
        if letter == guess:
            display[position - 1] = letter

    #Check if user is wrong. 
    if guess not in chosen_word:
        #Print the letter the user already guessed wrong.
        if guess in wrong_choices:
            print(f"You've already guessed {guess}.")
        else:
            #Print out hte letter and let them know if the letter is not in the chosen_word.
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            #Adds the wrong letter attempt to the wrong_choices list.
            wrong_choices.append(guess)
            #If guess is not a letter in the chosen_word, reduce 'lives' by 1.
            lives -= 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    #If lives goes down to 0 then the game stop and print "You lose."
    elif "_" in display and lives == 0:
        end_of_game = True
        print(f"You lose.\nThe word is: {chosen_word}.")


    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])