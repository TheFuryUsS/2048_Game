# tests/test_game.py
import pytest
from package.game import Game2048

def test_initial_board():
    game = Game2048()
    non_zero_tiles = sum(tile != 0 for row in game.board for tile in row)
    assert non_zero_tiles == 2  # Al iniciar, el tablero debe tener dos celdas diferentes de cero

def test_move_left():
    game = Game2048()
    game.board = [
        [2, 2, 4, 8],
        [0, 4, 0, 4],
        [2, 0, 2, 2],
        [8, 8, 0, 0],
    ]
    game.move_left()
    expected_board = [
        [4, 4, 8, 0],
        [8, 0, 0, 0],
        [4, 2, 0, 0],
        [16, 0, 0, 0],
    ]
    assert game.board == expected_board

def test_game_over():
    game = Game2048()
    game.board = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    assert game.is_game_over() is True

def test_not_game_over():
    game = Game2048()
    game.board = [
        [2, 4, 2, 4],
        [4, 0, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    assert game.is_game_over() is False
