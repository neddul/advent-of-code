# #Part one
with open("input_test.txt",'r') as f:
    data = f.read()
rows = data.split('\n\n')

bingo_dim = 5 #5x5 board

rolls = [int(c) for c in rows[0].split(',')]
boards = rows[1:]
boards = [[[int(value) for value in row.split()] for row in board.split('\n')] for board in boards]

def mark_bingo_box(bingo_board, drawn_number):
    for i in range(bingo_dim):
        for j in range(bingo_dim):
            if bingo_board[i][j] == drawn_number:
                bingo_board[i][j] = str(bingo_board[i][j])
    return bingo_board

def update_bingo_boards(list_of_all_bingo_boards, drawn_number):
    for i in range(len(list_of_all_bingo_boards)):
        list_of_all_bingo_boards[i] = mark_bingo_box(list_of_all_bingo_boards[i], drawn_number)
    return list_of_all_bingo_boards

def check_for_bingo_in_board(bingo_board):
    for i in range(bingo_dim):
        row = []
        for j in range(bingo_dim):
            row.append(type(bingo_board[i][j]) == str)
        if False not in row:
            return True
    for i in range(bingo_dim):
        col = []
        for j in range(bingo_dim):
            col.append(type(bingo_board[j][i]) == str)

        if False not in col:
            return True
    return False

def check_bingo_for_all_boards(list_of_all_bingo_boards):
    for i in range(len(list_of_all_bingo_boards)):
        if check_for_bingo_in_board(list_of_all_bingo_boards[i]):
            return True, i
    return False, -400

def score_of_winning_board(bingo_board, winning_number):
    board_sum = 0
    for i in range(bingo_dim):
        for j in range(bingo_dim):
            if type(bingo_board[i][j]) == int:
                board_sum += bingo_board[i][j]
    return board_sum*winning_number


def bingo(list_of_drawn_numbers, boards):
    for number in list_of_drawn_numbers:
        print(number)
        boards = update_bingo_boards(boards, number)
        did_bingo, board_number = check_bingo_for_all_boards(boards)
        
        if did_bingo:
            print(boards[board_number])
            return score_of_winning_board(boards[board_number], number)
        
score = bingo(rolls, boards)

print(score)