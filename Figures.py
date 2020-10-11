class Figure:
    def __init__(self, position, is_white=False):
        self.position = position
        self.is_white = is_white

    def move(self, new_position):
        self.position = new_position

    def __str__(self):
        return str(self.position)

    def get_possible_cages_to_move(self):
        pass


class Pawn(Figure):

    def __init__(self, position, is_white=False):
        super().__init__(position, is_white)
        self.no_moves = True

    def get_possible_cages_to_move(self):
        print(self.position)


class Rook(Figure):
    pass


class Knight(Figure):
    pass


class Bishop(Figure):
    pass


class Queen(Figure):
    pass


class King(Figure):
    pass
