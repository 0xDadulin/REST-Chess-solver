import pytest
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_validate_move_king(client):
    # Test if move is valid for King from e4 to e5
    response = client.get("/api/v1/king/e4/e5")
    assert response.status_code == 200
    data = response.get_json()
    assert data["move"] == "valid"


def test_validate_move_queen(client):
    # Test if move is valid for Queen from d4 to h4
    response = client.get("/api/v1/queen/d4/h4")
    assert response.status_code == 200
    data = response.get_json()
    assert data["move"] == "valid"


def test_validate_move_bishop(client):
    # Test if move is valid for Bishop from c4 to f7
    response = client.get("/api/v1/bishop/c4/f7")
    assert response.status_code == 200
    data = response.get_json()
    assert data["move"] == "valid"


def test_validate_move_rook(client):
    # Test if move is valid for Rook from h1 to h8
    response = client.get("/api/v1/rook/h1/h8")
    assert response.status_code == 200
    data = response.get_json()
    assert data["move"] == "valid"


def test_validate_move_knight(client):
    # Test if move is valid for Knight from g1 to f3
    response = client.get("/api/v1/knight/g1/f3")
    assert response.status_code == 200
    data = response.get_json()
    assert data["move"] == "valid"


def test_validate_move_pawn(client):
    # Test if move is valid for Pawn from e2 to e4
    # This assumes it's the pawn's first move
    response = client.get("/api/v1/pawn/e2/e4")
    assert response.status_code == 200
    data = response.get_json()
    assert data["move"] == "valid"


def test_validate_move_pawn2(client):
    # Test if move is valid for Pawn from e3 to e4
    response = client.get("/api/v1/pawn/e3/e4")
    assert response.status_code == 200
    data = response.get_json()
    assert data["move"] == "valid"
