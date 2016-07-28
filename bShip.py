from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))



if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
       
elif guess_row>5 or guess_row<0:
    print "Outside the range"
elif guess_col>5 or guess_col<0:
    print "Outside the range"
else:
    print "You missed my battleship!"
    board[guess_row][guess_col] = "X"
    print ship_row
    print ship_col
print_board(board)
        
        
    
