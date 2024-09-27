data = 'MOZARELLA'

def user_guess():
    global data
    user_data = ['_'] * len(data)  # Initialize user_data as underscores
    wrong_guesses = []  # Track wrong guesses
    chances = len(data)
    print('Length of word is: {}'.format(chances))
    
    while chances > 0 and '_' in user_data:  # Keep playing until no chances or word is fully guessed
        user_input = input('Enter a letter to guess the word: ').upper()

        if user_input in data:
            for i in range(len(data)):
                if data[i] == user_input:
                    user_data[i] = user_input  # Replace underscore with the correct guess
        else:
            if user_input not in wrong_guesses:  # Only record wrong guess once
                wrong_guesses.append(user_input)
                chances -= 1  # Reduce chances for wrong guess
                print('Wrong Guess: {}'.format(wrong_guesses))
            
        print('You have {} chances left.'.format(chances))
        print('Current word: ' + "".join(user_data))  # Print the result as a string
    
    if '_' not in user_data:
        print('Congratulations! You guessed the word correctly!')
    else:
        print('Sorry, you ran out of chances. The word was: {}'.format(data))


def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        user_guess()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

play_loop()