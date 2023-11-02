from .base_figure import Figure


class Bishop(Figure):
    def list_available_moves(self):
        # Get the current position in numeric form
        column, row = self.position
        col_idx = "abcdefgh".index(column)
        row_idx = int(row) - 1

        moves = []

        # Calculate diagonal moves
        for d_col, d_row in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Diagonal directions
            for i in range(1, 8):
                new_col_idx = col_idx + d_col * i
                new_row_idx = row_idx + d_row * i

                # Check if the new position is within the board limits
                if 0 <= new_col_idx < 8 and 0 <= new_row_idx < 8:
                    new_col = "abcdefgh"[new_col_idx]
                    new_row = str(new_row_idx + 1)
                    moves.append(new_col + new_row)

                # If the new position is not on the board, break the loop for this direction
                else:
                    break

        return moves

    def validate_move(self, dest_field: str):
        # Check if the destination field is a valid move for a bishop
        if dest_field in self.list_available_moves():
            return True
        else:
            return False
