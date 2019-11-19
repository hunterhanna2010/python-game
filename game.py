import random

# does the player want to play again?
def play_again():
    answer = input("Would you like to play again?")
    answer = answer.lower()
    # allow for player answer to be 'y' or 'yes'
    if answer == 'y' or 'yes':
        # call play_game function
        play_game()
    else:
        # It is a no
        pass

def get_word():
    # a list of words to randomize
    words = ['josh', 'marisa', 'tristin', 'evelynn', 'lazarus', 'lydia']
    return random.choice(words)

def play_game():
    # a string value for any alphabet character
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # the current word is the result of the randomized choice from the list of words
    current_word = get_word()
    # an empty list for any player guess
    letters_guessed = []
    # player has 5 tries O->-< == HANGMAN
    tries = 5
    # the player's guess starts with a False value so it can be flipped when the guess matches the current word
    guessed = False
    # first prompt for the player. A hint for how many letters are in the current word
    print('The Word Contains', len(current_word), 'letters.')
    print(len(current_word) * "*")
    # Initialize a while loop: while guessed is false and attempts are greater than 0
    while guessed == False and tries > 0:
        # give the player a message indicating how many total tries they have left
        print("You have " +str(tries)+ " tries")
        # each player input is a player_guess. 
        player_guess = input("Please guess one letter or the full word.")
        print(player_guess)
        player_guess = player_guess.lower()
        # Edge Cases where the user inputs one letter
        if len(player_guess) == 1:
            if player_guess not in alpha:
                print("You have not entered an alphabet character.")
            elif player_guess in letters_guessed:
                print("You have already entered that letter.")
            elif player_guess not in current_word:
                print("Too bad. That letter is not part of the word.")
                # append letters_guessed list and decrement the tries the player can have
                letters_guessed.append(player_guess)
                tries -= 1
            elif player_guess in current_word:
                print("YES! That letter is in the word.")
                # letters_guessed still needs to be appended whether a correct guess or incorrect
                letters_guessed.append(player_guess)
        # user inputs whole word
        elif len(player_guess) == len(current_word):
            if player_guess == current_word:
                print("Well Done! You guessed the whole word.")
                guessed = True
            else:
                print("Sorry. That is not the word.")
                tries -= 1
        # user inputs a guess that is not the same length as the word
        else:
            print("Your guess is not the same length as the word")
            tries -= 1
        # status reflects the player status throughout their guesses. begin with an empty string because they haven't guessed yet
        status = ''
        # if the player hasn't guessed the correct word or letter
        if guessed == False:
            # for each letter in the current word
            for letter in current_word:
                # and if that letter is appended to the letters_guessed list
                if letter in letters_guessed:
                    # player status is assigned to the letter they guessed
                    status += letter
                else:
                    # show their status in the current word with the correct guesses
                    status += ' * '
                    print(status)
        # if the player correctly guesses the right word, flip their guessed value to True
        if status == current_word:
            print("Hey! You guessed the word!")
            guessed = True
        # if they cannot guess the word within 5 attempts, player loses.
        elif tries == 0:
            print("You have run out of guesses. So Sorry player.")
    # call play again function block
    play_again()


play_game()





# your_input = input('please enter something:')
# print("you entered {your_input}")
# a word the player should guess
# word = hunter
# # player guesses before loosing = 6
# total_player_guesses = 6
# # guess-count the player
# count = 0

# guess = input("I'm thinking of a word. Choose wisely: ")
# while (guess) != word:
#     if (guess) 





# answer = 43
# guess = input("I'm thinking of a number between 1 and 100: ")
# while int(guess) != answer:
#     if int(guess) < answer:
#         guess = input("Too low. Guess again: ")
#     else:
#         guess = input("Too high. Guess again: ")
# print("You guessed right")