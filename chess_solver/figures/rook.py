from .base_figure import Figure


class Rook(Figure):
    def list_available_moves(self):
        # Assuming 'self.position' is a string in the format 'e2', 'h1', etc.
        column, row = self.position[0], self.position[1]

        # Generating moves in the column (vertically)
        moves_column = [
            f"{column}{r}" for r in "12345678" if f"{column}{r}" != self.position
        ]

        # Generating moves in the row (horizontally)
        moves_row = [f"{c}{row}" for c in "abcdefgh" if f"{c}{row}" != self.position]

        # Combining vertical and horizontal moves
        return moves_column + moves_row

    def validate_move(self, dest_field: str):
        # Check if the destination field is a valid move for the rook
        if dest_field in self.list_available_moves():
            return True
        return False
