from Figures import *


class NewGame:
    def __init__(self):
        self.figures = {"white pawns": [Pawn((2, i), True) for i in range(1, 9)],
                        "black pawns": [Pawn((7, i)) for i in range(1, 9)],
                        "white rooks": [Rook((1, 1), True), Rook((1, 8))],
                        "black rook": [Rook((8, 1)), Rook((8, 8))],
                        "white knights": [Knight((1, 2), True), Knight((1, 7), True)],
                        "black knights": [Knight((8, 2)), Knight((8, 7))],
                        "white bishops": [Bishop((1, 3), True), Bishop((1, 6), True)],
                        "black bishops": [Bishop((8, 3)), Bishop((8, 6))],
                        "white queen": [Queen((1, 4), True)],
                        "black queen": [Queen((8, 4))],
                        "white king": [King((1, 5), True)],
                        "black king": [King((8, 5))]}

    def get_current_position(self):
        return self.figures

    def get_readable_current_position(self):
        return "\n".join("{}: {}".format(key, value) for key, values in self.figures.items() for value in values)
