class ChessPiece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        if self.name == 'knight':
            return 'N' if self.color == 'white' else 'n'
        return self.name[0].upper() if self.color == 'white' else self.name[0].lower()

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("This method should be overridden in derived classes.")

class Pawn(ChessPiece):
    def is_valid_move(self, start, end, board):
        direction = 1 if self.color == 'white' else -1
        start_row, start_col = start
        end_row, end_col = end
        
        # Standard move forward
        if end_col == start_col:
            if end_row - start_row == direction and board[end_row][end_col] is None:
                return True
            if (end_row - start_row == 2 * direction and
                (start_row == 1 and self.color == 'white' or start_row == 6 and self.color == 'black') and
                board[end_row][end_col] is None and
                board[start_row + direction][start_col] is None):
                return True
        # Capturing
        elif abs(end_col - start_col) == 1 and end_row - start_row == direction:
            target_piece = board[end_row][end_col]
            if target_piece and target_piece.color != self.color:
                return True
        return False

class Rook(ChessPiece):
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        if start_row == end_row:  # Horizontal move
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] is not None:
                    return False
            return True
        elif start_col == end_col:  # Vertical move
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] is not None:
                    return False
            return True
        return False

class Knight(ChessPiece):
    def is_valid_move(self, start, end, board):
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

class Bishop(ChessPiece):
    def is_valid_move(self, start, end, board):
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])
        if row_diff == col_diff:  # Diagonal move
            step_row = 1 if end[0] > start[0] else -1
            step_col = 1 if end[1] > start[1] else -1
            for i in range(1, row_diff):
                if board[start[0] + i * step_row][start[1] + i * step_col] is not None:
                    return False
            return True
        return False

class Queen(ChessPiece):
    def is_valid_move(self, start, end, board):
        return Rook(self.color, 'rook').is_valid_move(start, end, board) or Bishop(self.color, 'bishop').is_valid_move(start, end, board)

class King(ChessPiece):
    def is_valid_move(self, start, end, board):
        # Basic move validation (king moves one square in any direction)
        if max(abs(end[0] - start[0]), abs(end[1] - start[1])) != 1:
            return False
        
        # Check if the king's move places it in check
        original_piece = board[end[0]][end[1]]
        board[end[0]][end[1]] = self
        board[start[0]][start[1]] = None

        in_check = ChessBoard().is_in_check(self.color)

        # Revert the board back to the original state
        board[start[0]][start[1]] = self
        board[end[0]][end[1]] = original_piece

        return not in_check

class ChessBoard:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        board = [[None] * 8 for _ in range(8)]
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(pieces):
            board[0][i] = piece('white', piece.__name__.lower())
            board[1][i] = Pawn('white', 'pawn')
            board[6][i] = Pawn('black', 'pawn')
            board[7][i] = piece('black', piece.__name__.lower())
        return board

    def print_board(self):
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))
        print()

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]

        if piece and piece.is_valid_move(start, end, self.board):
            target_piece = self.board[end_row][end_col]
            if target_piece and target_piece.color != piece.color:
                print(f"{piece} captures {target_piece}.")
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None
            return True
        return False

    def is_in_check(self, color):
        king_pos = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    king_pos = (row, col)
                    break
        
        if not king_pos:
            return False

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color != color:
                    if piece.is_valid_move((row, col), king_pos, self.board):
                        return True
        return False

    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == color:
                    for r in range(8):
                        for c in range(8):
                            if piece.is_valid_move((row, col), (r, c), self.board):
                                original_target = self.board[r][c]
                                self.board[r][c] = piece
                                self.board[row][col] = None
                                if not self.is_in_check(color):
                                    self.board[row][col] = piece
                                    self.board[r][c] = original_target
                                    return False
                                self.board[row][col] = piece
                                self.board[r][c] = original_target
        return True

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_turn = 'white'

    def switch_turn(self):
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
   
    def end_game(self):
        print("Thank you for playing! The game has ended.")
        exit()

    def play(self):
        while True:
            self.board.print_board()
            if self.board.is_in_check(self.current_turn):
                print(f"{self.current_turn} is in check!")

            print(f"{self.current_turn}'s turn. Enter move (e.g., e2 e4) or 'quit' to exit: ")
            move = input().strip().split()

    
            if move[0].lower() == 'quit':
                self.end_game()


            if len(move) != 2 or len(move[0]) != 2 or len(move[1]) != 2:
                print("Invalid move format. Use 'start end' format.")
                continue

            try:
                start = (int(move[0][1]) - 1, ord(move[0][0]) - ord('a'))
                end = (int(move[1][1]) - 1, ord(move[1][0]) - ord('a'))
            except (ValueError, IndexError):
                print("Invalid move. Ensure you use valid coordinates (e.g., e2 e4).")
                continue

            if self.board.move_piece(start, end):
                if self.board.is_checkmate(self.current_turn):
                    print(f"Checkmate! {self.current_turn} loses!")
                    break
                self.switch_turn()

if __name__ == "__main__":
    game = ChessGame()
    game.play()
