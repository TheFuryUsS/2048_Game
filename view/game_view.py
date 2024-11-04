class GameView:
    def display_board(self, board):
        # Muestra el tablero en la consola
        for row in board:
            print(" ".join(str(cell) for cell in row))
