from func import *

gamestate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
running = True
winner = None

print("Let's play tictactoe!")
print("to play, type in a number based on the scoring guide below!")
print_guide()
print("X goes first!")

while running is True:
    gamestate = play_turn('X', gamestate)
    #asess_turn(gamestate)
    gamestate = play_turn('O', gamestate)
    #asess_turn(gamestate)

print("congartulations!")
print(winner + " wins!")