# REST Chess Solver

Welcome to the REST Chess Solver API! This Flask-based web service allows you to find available moves for various chess pieces from any given position on a standard chess board.

## Features

- **Get Available Moves:** You can fetch the available moves for any of the standard chess pieces (King, Queen, Bishop, Rook, Knight, and Pawn) from a given position.
- **Validate Moves:** Validate if a specific move is legal for a given chess piece from a given position to a destination.

## How to Use

### Available Moves Endpoint

To get available moves for a chess piece from a given position:

`/api/v1/<chess_figure>/<current_field>`

For example:

`/api/v1/queen/e4`

### Validate Move Endpoint

To validate if a move is legal for a given chess piece from a given position to a destination:

`/api/v1/<chess_figure>/<current_field>/<dest_field>`

For example:

`/api/v1/queen/e4/g6`

## Docker

You can run this API using Docker. The Docker image is available on Docker Hub:

[Chess Solver Docker Image](https://hub.docker.com/r/0xdadulin/chess_solver)

To pull the image and run:

`docker pull 0xdadulin/chess_solver`
`docker run -p 8000:8000 0xdadulin/chess_solver`

Visit `http://localhost:8000` in your browser to access the API.

## Source Code

All the source code for this project is available on GitHub:

[REST Chess Solver Repository](https://github.com/0xDadulin/REST-Chess-solver)

## Error Handling

The API has built-in error handling for invalid chess figures, invalid fields, and invalid moves.

## Conclusion

This REST Chess Solver API is designed to be simple yet functional. It serves as a demonstration of Flask API development and usage, as well as chess game logic. Feedback and contributions are welcome!

