from random import choice
game_choice = ['rock','paper','scissor']
computer_choice = choice(game_choice)
play = True
while play==True:
    play_game = input('Do you want to play game(y or n):')
    if play_game == 'y':
        user_input = input('Enter your choice :')
        if user_input == computer_choice:
            print('Tie Game')
        else:
            if user_input == 'paper' and computer_choice =='rock' or user_input =='scissor' and  computer_choice =='paper' or user_input =='rock' and  computer_choice =='scissor':
                print('User won')
                print('Computer choice:{},User choice:{}'.format(computer_choice,user_input))
            elif user_input == 'paper' and computer_choice =='scissor' or user_input =='scissor' and  computer_choice =='rock' or user_input =='rock' and  computer_choice =='paper':
                print('Computer won')
            
    elif play_game == 'n':
        break
print('Thanks For Playing! We expect you back again!')