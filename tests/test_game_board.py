from src.model.game_board import GameBoard

def test_initialization():
    game = GameBoard()
    assert game.score == 0
    assert all(cell == 0 for row in game.board for cell in row)  # Comprobamos que todas las celdas estén en 0

def test_spawn_number():
    game = GameBoard()
    game.spawn_number()
    non_empty_cells = sum(1 for row in game.board for cell in row if cell != 0)
    assert non_empty_cells == 1  # Una celda debería estar ocupada

def test_score_update():
    game = GameBoard()
    game.score = 0
    game.update_score(10)
    assert game.score == 10