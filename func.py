def print_board(gamestate):
    symbols = [' ', 'X', 'O']
    board = [symbols[num] if num in [-1, 1] else symbols[0] for num in gamestate]
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print("_________")
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print("_________")
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print("_________")

def print_guide():
    print('1 | 2 | 3')
    print("_________")
    print("4 | 5 | 6")
    print("_________")
    print("7 | 8 | 9")

def play_turn(player, gamestate):
    if player == 'X':
        move = input("play your turn, X. type 'idk' to bring up the guide:")
        if move == 'idk':
            print_guide()
            print("heres the guide...")
        else:
            try:
                move -= 1
                if gamestate[move] == 0:
                    gamestate[move] = 1
                    return gamestate
                else:
                    print("thats not a valid move")
            except:
                print("read the guide dumbass")
                print_guide()
    else:
        pass