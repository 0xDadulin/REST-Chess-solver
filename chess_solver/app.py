from typing import Type, Union, Dict, Tuple
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from figures.king import King
from figures.bishop import Bishop
from figures.queen import Queen
from figures.rook import Rook
from figures.knight import Knight
from figures.pawn import Pawn

# Initialize Flask application
app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Root endpoint to welcome users to the Chess Solver API."""
    return "Welcome to the Chess Solver API!"


# Mapping of chess figure names to their respective classes
FIGURE_MAP: Dict[str, Type[Union[King, Queen, Bishop, Rook, Knight, Pawn]]] = {
    "king": King,
    "queen": Queen,
    "bishop": Bishop,
    "rook": Rook,
    "knight": Knight,
    "pawn": Pawn,
}


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def available_moves(
    chess_figure: str, current_field: str
) -> Union[str, Tuple[str, int]]:
    """Endpoint to get available moves for a given chess figure from a given position."""
    # Validate if the provided field is valid
    if not is_valid_chess_field(current_field):
        raise InvalidFieldError()

    # Retrieve the figure class from the FIGURE_MAP; raise error if not found
    figure_class = FIGURE_MAP.get(chess_figure.lower())
    if not figure_class:
        raise InvalidFigureError()

    # Initialize the figure and get the list of available moves
    figure = figure_class(current_field)
    moves = figure.list_available_moves()

    # Return the moves as a JSON response
    return (
        jsonify(
            {
                "availableMoves": moves,
                "error": None,
                "figure": chess_figure,
                "currentField": current_field,
            }
        ),
        200,
    )


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def validate_move(
    chess_figure: str, current_field: str, dest_field: str
) -> Union[str, Tuple[str, int]]:
    """Endpoint to validate if a move is legal for a given chess figure from a given position to a destination."""
    # Validate if both the provided fields are valid
    if not is_valid_chess_field(current_field) or not is_valid_chess_field(dest_field):
        raise InvalidFieldError()

    # Retrieve the figure class from the FIGURE_MAP; raise error if not found
    figure_class = FIGURE_MAP.get(chess_figure.lower())
    if not figure_class:
        raise InvalidFigureError()

    # Initialize the figure and check if the move is valid
    figure = figure_class(current_field)
    is_valid = figure.validate_move(dest_field)

    # Raise error if the move is not valid
    if not is_valid:
        raise InvalidMoveError()

    # Return the validation result as a JSON response
    return (
        jsonify(
            {
                "destField": dest_field,
                "move": "valid" if is_valid else "invalid",
                "figure": chess_figure,
                "error": None if is_valid else "Move not permitted.",
                "currentField": current_field,
            }
        ),
        200,
    )


# Custom exception classes
class InvalidFigureError(Exception):
    """Exception raised when an invalid chess figure is requested."""

    pass


class InvalidFieldError(Exception):
    """Exception raised when an invalid field is provided."""

    pass


class InvalidMoveError(Exception):
    """Exception raised when an invalid move is attempted."""

    pass


# Error handlers for custom exceptions
@app.errorhandler(InvalidFigureError)
def handle_invalid_figure(error: InvalidFigureError) -> Tuple[str, int]:
    """Error handler for InvalidFigureError."""
    return jsonify({"error": "Invalid chess figure."}), 404


@app.errorhandler(InvalidFieldError)
def handle_invalid_field(error: InvalidFieldError) -> Tuple[str, int]:
    """Error handler for InvalidFieldError."""
    return jsonify({"error": "Invalid field."}), 409


@app.errorhandler(InvalidMoveError)
def handle_invalid_move(error: InvalidMoveError) -> Tuple[str, int]:
    """Error handler for InvalidMoveError."""
    return jsonify({"error": "Move not permitted."}), 409


def is_valid_chess_field(field: str) -> bool:
    """Utility function to validate if a given field is a valid chess board field."""
    valid_fields = [
        f"{letter}{number}" for letter in "abcdefgh" for number in "12345678"
    ]
    return field in valid_fields


@app.errorhandler(Exception)
def handle_exception(e: Exception) -> Tuple[str, int]:
    """Error handler for general exceptions."""
    if isinstance(e, HTTPException):
        return e.get_response()

    return jsonify(error=str(e)), 500


# Entry point for running the Flask application
if __name__ == "__main__":
    app.run(debug=True, port=8000)
