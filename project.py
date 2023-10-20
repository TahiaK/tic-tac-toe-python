import random

#GAME FUNCTIONS

def display_board(board):
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('----------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('----------')
    print(board[7]+' | '+board[8]+' | '+board[9])

def player_input():
    marker = ''
    while marker !='X' and marker !='O':
        marker = input('Player 1 choose X or O: ').upper()
    
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else: player2 = 'X'

    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else: return 'Player 2'

def space_check(board, position):
    if board[position] == ' ':
        return True
    else: return False
    #return board[position] == ' '

def full_board_check(board):
    for i in range(1,10): #doesn't include last number 10
        if space_check(board, i): # if true
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position): #check if number entered is within 1-9 or if it has a free position
        position = int(input("Enter your next position (1-9): "))
    return position

def replay(): #return T/F
    answer = ' '
    while answer not in ['Y','N']:
        answer = input("Do you want to play again? (Y or N) ").upper()
    return answer.startswith('Y')

# START GAME

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    print('player1: '+ player1_marker)
    print('player2: '+ player2_marker)
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            (theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break