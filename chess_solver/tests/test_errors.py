import pytest
from flask import json


# Fixture to run app for testing purposes
@pytest.fixture
def client():
    from app import app

    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_invalid_field(client):
    """Test if API returns 409 status code when a field is out of chessboard range"""
    response = client.get("/api/v1/pawn/invalid_field")
    assert response.status_code == 409
    assert json.loads(response.data)["error"] == "Invalid field."


def test_nonexistent_figure(client):
    """Test if API returns 404 status code when a figure is not found in FIGURE_MAP"""
    response = client.get("/api/v1/unicorn/a1")
    assert response.status_code == 404
    assert json.loads(response.data)["error"] == "Invalid chess figure."


def test_invalid_move(client):
    """Test if API returns 409 status code when a figure's move is invalid"""
    # Assuming that moving a pawn from a2 to a5 is invalid
    response = client.get("/api/v1/pawn/a2/a5")
    assert response.status_code == 409
    assert json.loads(response.data)["error"] == "Move not permitted."


def test_server_error(client, monkeypatch):
    """Test if API returns 500 status code when a general exception is thrown"""

    # Simulate an exception by patching a function used by the API endpoint
    def mock_exception(*args, **kwargs):
        raise Exception("Test exception")

    monkeypatch.setattr("app.is_valid_chess_field", mock_exception)

    response = client.get("/api/v1/pawn/a2")
    assert response.status_code == 500
    assert "Test exception" in json.loads(response.data)["error"]
