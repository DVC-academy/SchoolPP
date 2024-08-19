def move(board, size):
    for row_num in range(size):
        for col_num in range(size):
            if board[row_num][col_num] == '.':
                return row_num, col_num

