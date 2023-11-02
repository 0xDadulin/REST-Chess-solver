from .base_figure import Figure


class King(Figure):
    def list_available_moves(self):
        # Define the king's moves: one square in any direction
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        legal_moves = []
        current_column, current_row = self.position
        col_idx = "abcdefgh".index(current_column)
        row_idx = int(current_row) - 1

        # Generate moves within the board boundaries
        for d_col, d_row in moves:
            new_col_idx = col_idx + d_col
            new_row_idx = row_idx + d_row

            # Ensure the move is within the chessboard
            if 0 <= new_col_idx < 8 and 0 <= new_row_idx < 8:
                # Translate back to chess notation
                new_col = "abcdefgh"[new_col_idx]
                new_row = str(new_row_idx + 1)
                legal_moves.append(new_col + new_row)

        return legal_moves

    def validate_move(self, dest_field: str):
        # Check if the destination field is a valid move
        return dest_field in self.list_available_moves()
