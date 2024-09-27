import board
import random


def draw_board(board):
    row_1 = "{}|{}|{}".format(board[0],board[1],board[2])
    row_2 = "{}|{}|{}".format(board[3],board[4],board[5])
    row_3 = "{}|{}|{}".format(board[6],board[7],board[8])
    print(row_1+'\n'+row_2+'\n'+row_3)
    

def user_move(board,user_type):
    user_choice = int(input('Enter numbers between 1-9:')) - 1
    if board[user_choice] != ' ':
        print('Space is already taken.')
        user_move(board,user_type)
    else:
        board[user_choice] = user_type
        available_spaces.remove(user_choice)
        
             
def check_win(board,X_O):
    if board[0] == board[1] == board[2] ==X_O or board[3] == board[4] == board[5] ==X_O or board[6] == board[7] == board[8] ==X_O or board[0] == board[3] == board[6] ==X_O or board[1] == board[4] == board[7] ==X_O or board[2] == board[5] == board[8] ==X_O or board[2] == board[4] == board[6] ==X_O or board[0] == board[4] == board[8] ==X_O:
        play =False
        print('Hooray! {} has Won'.format(X_O))
    else:
        play = True
    return play
 
 
def comp_move(board,user_type):
    computer_choice = random.choice(available_spaces)
    board[computer_choice]=user_type
    available_spaces.remove(computer_choice)
    
    
board = [" "]*9
draw_board(board)
play = True     
available_spaces = [0,1,2,3,4,5,6,7,8] 
computer_or_friend = input('Would you like to play against computer or friend?(c or f):') 
while play==True:
    user_move(board,'X')
    play=check_win(board,'X')
    draw_board(board)
    if play==False:
        continue
    if computer_or_friend == 'f':
        user_move(board, 'o')
    elif computer_or_friend == 'c':
        comp_move(board, 'o')
    play=check_win(board,'o')
    draw_board(board)


print('End Game')
    

    
    
