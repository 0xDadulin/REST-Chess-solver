import pytest
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_available_moves_king(client):
    # Test available moves for King at e4
    response = client.get("/api/v1/king/e4")
    assert response.status_code == 200
    data = response.get_json()
    expected_moves = {"e5", "d5", "d4", "d3", "e3", "f3", "f4", "f5"}
    assert set(data["availableMoves"]) == expected_moves


def test_available_moves_queen(client):
    # Test available moves for Queen at d4
    response = client.get("/api/v1/queen/d4")
    assert response.status_code == 200
    data = response.get_json()
    expected_moves = {
        "d1",
        "d2",
        "d3",
        "d5",
        "d6",
        "d7",
        "d8",
        "a4",
        "b4",
        "c4",
        "e4",
        "f4",
        "g4",
        "h4",
        "c3",
        "b2",
        "a1",
        "e5",
        "f6",
        "g7",
        "h8",
        "c5",
        "b6",
        "a7",
        "e3",
        "f2",
        "g1",
    }
    assert set(data["availableMoves"]) == expected_moves


def test_available_moves_bishop(client):
    # Test available moves for Bishop at c4
    response = client.get("/api/v1/bishop/c4")
    assert response.status_code == 200
    data = response.get_json()
    expected_moves = {"b3", "a2", "d5", "e6", "f7", "g8", "b5", "a6", "d3", "e2", "f1"}
    assert set(data["availableMoves"]) == expected_moves


def test_available_moves_rook(client):
    # Test available moves for Rook at h1
    response = client.get("/api/v1/rook/h1")
    assert response.status_code == 200
    data = response.get_json()
    expected_moves = {
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "h7",
        "h8",
        "g1",
        "f1",
        "e1",
        "d1",
        "c1",
        "b1",
        "a1",
    }
    assert set(data["availableMoves"]) == expected_moves


def test_available_moves_knight(client):
    # Test available moves for Knight at g1
    response = client.get("/api/v1/knight/g1")
    assert response.status_code == 200
    data = response.get_json()
    expected_moves = {"e2", "f3", "h3"}
    assert set(data["availableMoves"]) == expected_moves


def test_available_moves_pawn(client):
    # Test available moves for Pawn at e2
    # Assuming it's the pawn's first move and it can move two spaces forward
    response = client.get("/api/v1/pawn/e2")
    assert response.status_code == 200
    data = response.get_json()
    expected_moves = {"e3", "e4"}
    assert set(data["availableMoves"]) == expected_moves


def test_available_moves_pawn2(client):
    # Test available moves for Pawn at e3
    response = client.get("/api/v1/pawn/e3")
    assert response.status_code == 200
    data = response.get_json()
    expected_moves = {"e4"}
    assert set(data["availableMoves"]) == expected_moves
