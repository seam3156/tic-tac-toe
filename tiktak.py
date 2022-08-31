#! /bin/python

print("Tik Tak Toe Game")

# default cell names
cells = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#set winner
winner = 'N'
#counter used to switch between players
pcounter = 1

# updates the board
def setboard(cells):
    board = (f"""
      #   #
    {cells[0]} # {cells[1]} # {cells[2]}
    #########
    {cells[3]} # {cells[4]} # {cells[5]}
    #########
    {cells[6]} # {cells[7]} # {cells[8]}
      #   # 
    """)
    return board

# checks if there is a winner
def win(cells):
    for column in range(3):
        if cells[column] == cells[column+3] and cells[column] == cells[column+6]:
            return cells[column]
    for row in range(3):
        if cells[row*3] == cells[row*3+1] and cells[row*3] == cells[row*3+2]:
            return cells[row*3]
    if cells[0] == cells[4] and cells[0] == cells[8]:
        return cells[0]
    if  cells[2] == cells[4] and cells[2] == cells[6]:
        return cells[2]
    for each in cells:
        if each == 'o' or each == 'x':
            draw = True
        else:
            draw = False
            break
    if draw == True:
        return 'D'
    return 'N'

# gets the users input
def UserInput(cells, counter):
    if pcounter % 2 == 0:
        player = 'x'
    else:
        player = 'o'
    choise = int(input(f"draw {player} in cell: "))
    while  choise < 1 or choise > 9 or cells[choise - 1] == 'o' or cells[choise - 1] == 'x':
        choise = int(input(f"draw {player} in cell: "))
    cells[choise - 1] = player
    return cells

#main program

# will play the game until there is a winner or a draw
while winner == 'N':
    board = setboard(cells)
    print(board)
    cells = UserInput(cells, pcounter)
    winner = win(cells)
    pcounter += 1
    
board = setboard(cells)
print(board)
# prints result (draw or win)
if winner == 'D':
    print("The game ended in a tie")
else:    
    print(f"player {winner} won the game!")