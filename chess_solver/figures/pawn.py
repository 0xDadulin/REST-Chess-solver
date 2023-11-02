from .base_figure import Figure

class Pawn(Figure):
    def list_available_moves(self):
        # Pawns move forward one square, but on their first move, they can move two squares
        initial_row = self.position[1]

        # Determine the color and the direction of the pawn based on the initial row
        if initial_row == '2':  # Starting row for white pawns
            color = 'white'
            direction = 1
            initial_moves = 2 if initial_row == '2' else 1
        elif initial_row == '7':  # Starting row for black pawns
            color = 'black'
            direction = -1
            initial_moves = 2 if initial_row == '7' else 1
        else:  # Any other row, pawn must have moved, therefore it can only move one step
            color = 'white' if initial_row in '3456' else 'black'
            direction = 1 if color == 'white' else -1
            initial_moves = 1

        legal_moves = []
        current_column, current_row = self.position
        row_idx = int(current_row)

        # Generate moves within the board boundaries
        for step in range(1, initial_moves + 1):
            new_row_idx = row_idx + (step * direction)
            # Ensure the move is within the chessboard and to an empty square
            if 0 < new_row_idx <= 8:
                new_row = str(new_row_idx)
                legal_moves.append(current_column + new_row)

        return legal_moves

    def validate_move(self, dest_field: str):
        # Check if the destination field is a valid move for the pawn
        return dest_field in self.list_available_moves()
