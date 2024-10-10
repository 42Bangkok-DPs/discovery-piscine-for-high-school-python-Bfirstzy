

def checkmate(board_str):
    board = [list(row) for row in board_str.splitlines()]  
    n = len(board)  
    
    
    def find_king():
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'K':
                    return i, j
        return None

    
    def get_moves(piece):
        if piece == 'P':  
            return [(-1, -1), (-1, 1)]  
        elif piece == 'B':  
            return [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        elif piece == 'R':  
            return [(0, 1), (0, -1), (1, 0), (-1, 0)]
        elif piece == 'Q':  
            return [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)]
        return []

    
    def is_in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    
    def can_capture_king(piece, x, y, king_x, king_y):
        moves = get_moves(piece)
        for dx, dy in moves:
            nx, ny = x, y
            while is_in_bounds(nx + dx, ny + dy):
                nx += dx
                ny += dy
                if board[nx][ny] == 'K':  
                    return True
                elif board[nx][ny] != '.':  
                    break
        return False

    
    king_x, king_y = find_king()  
    
    if king_x is None:
        print("Error: King not found.")
        return

    for i in range(n):
        for j in range(n):
            piece = board[i][j]
            if piece in ['P', 'B', 'R', 'Q']:  
                if can_capture_king(piece, i, j, king_x, king_y):
                    print("Success")  
                    return
    
    print("Fail")  
