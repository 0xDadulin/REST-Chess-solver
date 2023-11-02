from .base_figure import Figure


class Queen(Figure):
    def list_available_moves(self):
        # The queen combines the power of a rook and bishop and can move any number of squares along a rank, file, or diagonal
        legal_moves = []
        current_column, current_row = self.position
        col_idx = "abcdefgh".index(current_column)
        row_idx = int(current_row) - 1

        # Horizontal and vertical moves
        for i in range(8):
            if i != col_idx:
                legal_moves.append("abcdefgh"[i] + current_row)
            if i != row_idx:
                legal_moves.append(current_column + str(i + 1))

        # Diagonal moves
        for i in range(-7, 8):
            if i != 0:
                new_col_idx = col_idx + i
                new_row_idx = row_idx + i
                if 0 <= new_col_idx < 8 and 0 <= new_row_idx < 8:
                    legal_moves.append("abcdefgh"[new_col_idx] + str(new_row_idx + 1))
                new_row_idx = row_idx - i
                if 0 <= new_col_idx < 8 and 0 <= new_row_idx < 8:
                    legal_moves.append("abcdefgh"[new_col_idx] + str(new_row_idx + 1))

        return legal_moves

    def validate_move(self, dest_field: str):
        # Check if the destination field is a valid move for the queen
        return dest_field in self.list_available_moves()
