def display_board(board):

   
    print('' + board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print('' + board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print('' + board[1] + ' | ' + board[2] + ' | ' + board[3] )

def player_input():
    marker = ' '

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player one! please select "X" or "O": ').upper()
    
    player1_marker = marker
    
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    
    return (player1_marker, player2_marker)

    print(return)

player_input()
