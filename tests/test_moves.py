# tests/test_moves.py
from src.model.game_board import GameBoard

def test_move_left():
    game = GameBoard()
    game.board = [[2, 2, 0, 0], [4, 0, 4, 0], [2, 0, 2, 2], [0, 4, 0, 4]]
    game.move_left()
    assert game.board == [[4, 0, 0, 0], [8, 0, 0, 0], [4, 2, 0, 0], [8, 0, 0, 0]]

def test_move_right():
    game = GameBoard()
    game.board = [[2, 2, 0, 0], [4, 0, 4, 0], [2, 0, 2, 2], [0, 4, 0, 4]]
    game.move_right()
    assert game.board == [[0, 0, 0, 4], [0, 0, 0, 8], [0, 0, 2, 4], [0, 0, 0, 8]]

def test_move_up():
    game = GameBoard()
    game.board = [[2, 0, 2, 0], [2, 0, 2, 4], [0, 4, 0, 0], [4, 0, 4, 4]]
    game.move_up()
    assert game.board == [[4, 4, 4, 8], [4, 0, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def test_move_down():
    game = GameBoard()
    game.board = [[2, 0, 2, 0], [2, 0, 2, 4], [0, 4, 0, 0], [4, 0, 4, 4]]
    game.move_down()
    assert game.board == [[0, 0, 0, 0], [4, 0, 4, 0], [4, 4, 4, 8], [4, 0, 4, 0]]
