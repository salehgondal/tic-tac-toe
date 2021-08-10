import string
from random import random


def print_game(slots):
    print("\n")
    for i in range(len(slots)):
        for j in range(len(slots[i])):
            if j < len(slots[i])-1:
                print(slots[i][j]," | ",end=" ")
            else:
                print(slots[i][j])
        if i == len(slots)-1:
            continue
        print("-------------")
    print("\n")
	
win = ['ABC','DEF','GHI','ADG','BEH','CFI','AEI','CEG']




names = []

print("Player 1 Please enter your name:")
names.append(input())

print("Player 2 Please enter your name:")
names.append(input())

print(names[0], "is Player 1 and ", names[1], " is Player 2.\n")

games = [0,0]

def print_scoreboard(names,games):
    print("\n")
    print("=====================")
    print("    SCOREBOARD       ")
    print("=====================")
    print("  ",names[0], " | ", games[0])
    print("---------------------")
    print("  ",names[1], " | ", games[1])
    print("=====================")
    print("\n")

print_scoreboard(names,games)



def process_move(moves,player,mark):
    moves[player].append(mark)
    moves[player] = sorted(moves[player])

while True:
    
    # Initialize all game variables
    slots = []
    for row in range(3):
        slots.append(list(string.ascii_uppercase[3*row:3*row+3]))
    
    grid_positions = list(string.ascii_uppercase[:9])
    
    moves = [[],[]]
    
    rn = random()
    
    if rn > 0.5:
        v = 1
    else:
        v = 0
    
    for i in range(v,v+9):
        print_game(slots)
        player = (i%2)
        while True:
            print(names[player],",Please select an available box from the grid. (Enter q to quit.): ", end="")
            mark = input().upper()
            #mark = mark.upper()
            if mark == 'Q':
                print("Do you really want to quit? y/n")
                x = input()
                if x == 'y':
                    print("Quitting...")
                    quit()
                else:
                    continue
                    
            if mark not in grid_positions:
                print("Invalid Input!")
                print("\n")
                continue
            break
            
        grid_positions.remove(mark)
        
        process_move(moves,player,mark)
        
        for row in range(len(slots)):
            for val in range(len(slots[row])):
                if mark == slots[row][val]:
                    slots[row][val] = player+1
        
    # Check Result
        for comb in win:
            winner = None
            if all(c in "".join(moves[player]) for c in comb):
                print_game(slots)
                print(names[player],"Wins!!!")
                winner = player
                break
        if winner is not None:
            break
        
    # check if result possible
        
        for comb in win:
            if all(c in "".join(sorted(moves[player]+grid_positions)) for c in comb):
                draw_ind = 0
                break
            else:
                draw_ind = draw_ind + 1
                
        
        if len(grid_positions) == 0 or draw_ind == len(win):
            print_game(slots)
            print("The game is a draw!")
            winner = None
            break
        

    
    if winner is not None:
        games[winner] = games[winner] + 1
    
    print_scoreboard(names,games)
    print("Do you want to play again? y/n")
    x = input()
    if x == 'y':
        continue
    else:
        print("Quitting...")
        quit()
    
