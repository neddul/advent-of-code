# #Part one
with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n\n')

bingo_dim = 5 #5x5 board

drawn_numbers = [int(c) for c in rows[0].split(',')]
boards = rows[1:]
boards = [[[int(value) for value in row.split()] for row in board.split('\n')] for board in boards]

def mark_bingo_box(bingo_board, drawn_number):
    for i in range(bingo_dim):
        for j in range(bingo_dim):
            if bingo_board[i][j] == drawn_number:
                bingo_board[i][j] = "X"
    return bingo_board

def update_bingo_boards(list_of_all_bingo_boards, drawn_number):
    for i in range(len(list_of_all_bingo_boards)):
        list_of_all_bingo_boards[i] = mark_bingo_box(list_of_all_bingo_boards[i], drawn_number)
    return list_of_all_bingo_boards

def check_for_bingo_in_board(bingo_board):
    for i in range(bingo_dim):
        row = []
        for j in range(bingo_dim):
            if bingo_board[i][j] == "X":
                row.append(True)

        if len(row) == 5:
            # print("Row true")
            # print("------------------------------")
            # print_board(bingo_board)
            # print("------------------------------")

            return True
        
    for i in range(bingo_dim):
        col = []
        for j in range(bingo_dim):
            if bingo_board[j][i] == "X":
                col.append(True)

        if len(col) == 5:
            #print("col true")
            return True
    return False

def check_bingo_for_all_boards(list_of_all_bingo_boards):
    for i in range(len(list_of_all_bingo_boards)):
        if check_for_bingo_in_board(list_of_all_bingo_boards[i]):
            #print(i)
            return True, i
    return False, -400

def score_of_winning_board(bingo_board, winning_number):
    board_sum = 0
    #print(winning_number)
    for i in range(bingo_dim):
        for j in range(bingo_dim):
            if type(bingo_board[i][j]) == int:
                board_sum += bingo_board[i][j]
    return board_sum*winning_number

#Recursively removes all boards that has a board with bingo in it
def remove_boards_with_bingo(list_of_all_bingo_boards):
    bingo_bool, index = check_bingo_for_all_boards(list_of_all_bingo_boards)
    if len(list_of_all_bingo_boards) > 1 and bingo_bool:
        list_of_all_bingo_boards.pop(index)
        return remove_boards_with_bingo(list_of_all_bingo_boards)
    return list_of_all_bingo_boards
        
def print_board(board):
    for i in range(bingo_dim):
        row = ""
        for j in range(bingo_dim):
            row += f"{board[i][j]}".rjust(3)
        
        print(row)

def bingo(list_of_drawn_numbers, boards):
    number_to_be_drawn = 0
    
    while len(boards) > 1:
        # print(list_of_drawn_numbers[number_to_be_drawn])
        number = list_of_drawn_numbers[number_to_be_drawn]
        boards = update_bingo_boards(boards, number)
        # for board in boards:
        #     print_board(board)
        #     print()
        # #print(len(boards))
        boards = remove_boards_with_bingo(boards)
        number_to_be_drawn+=1
    
    #Last board may not be done when it is the last board remaning
    for number in list_of_drawn_numbers:
        boards = update_bingo_boards(boards, number)
        did_bingo, board_number = check_bingo_for_all_boards(boards)
        
        if did_bingo:
            #print(boards[board_number])
            return score_of_winning_board(boards[board_number], number)


        
score = bingo(drawn_numbers, boards)

print(score)