# package/game.py
import random

class Game2048:
    def __init__(self):
        self.size = 4
        self.board = [[0] * self.size for _ in range(self.size)]
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        """Agrega una ficha (2 o 4) en una celda vacía del tablero."""
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 0]
        if not empty_cells:
            return
        i, j = random.choice(empty_cells)
        self.board[i][j] = 2 if random.random() < 0.9 else 4

    def move_left(self):
        """Realiza el movimiento hacia la izquierda y combina las fichas."""
        moved = False
        for i in range(self.size):
            compressed, merged = self.compress(self.board[i]), [False] * self.size
            for j in range(1, self.size):
                if compressed[j] == compressed[j - 1] and not merged[j - 1]:
                    compressed[j - 1] *= 2
                    compressed[j] = 0
                    merged[j - 1] = True
                    moved = True
            new_row = self.compress(compressed)
            if new_row != self.board[i]:
                moved = True
            self.board[i] = new_row
        if moved:
            self.spawn_tile()
        return moved

    def compress(self, row):
        """Elimina ceros en una fila y los mueve al final."""
        return [num for num in row if num != 0] + [0] * (self.size - len([num for num in row if num != 0]))

    def is_game_over(self):
        """Verifica si el juego ha terminado."""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
                if i < self.size - 1 and self.board[i][j] == self.board[i + 1][j]:
                    return False
                if j < self.size - 1 and self.board[i][j] == self.board[i][j + 1]:
                    return False
        return True
