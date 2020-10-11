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

    def get_possible_cages_to_move(self):
        result = []
        if self.is_white:
            result.append((self.position[0] + 1, self.position[1]))
            if self.position[0] == 2:
                result.append((self.position[0] + 2, self.position[1]))
        else:
            result.append((self.position[0] - 1, self.position[1]))
            if self.position[0] == 7:
                result.append((self.position[0] - 2, self.position[1]))
        return result


class Rook(Figure):
    def get_possible_cages_to_move(self):
        return [(self.position[0], i) for i in range(1, 9) if i != self.position[1]] \
               + [(i, self.position[1]) for i in range(1, 9) if i != self.position[0]]


class Knight(Figure):
    def get_possible_cages_to_move(self):
        return [(self.position[0] + i, self.position[1] + j) for i in range(-2, 3, 4) for j in range(-1, 2, 2) if
                i != j and 0 < self.position[0] + i < 9 and 0 < self.position[1] + j < 9] + \
               [(self.position[0] + i, self.position[1] + j) for i in range(-1, 2, 2) for j in range(-2, 3, 4) if
                i != j and 0 < self.position[0] + i < 9 and 0 < self.position[1] + j < 9]


class Bishop(Figure):
    def get_possible_cages_to_move(self):
        return [(i, j) for i in range(1, 9) for j in range(1, 9) if
                abs(self.position[0] - i) == abs(self.position[1] - j) and i != self.position[0]]


class Queen(Figure):
    def get_possible_cages_to_move(self):
        return list(set([(i, j) for i in range(1, 9) for j in range(1, 9) if
                         abs(self.position[0] - i) == abs(self.position[1] - j) and i != self.position[0]] + [
                            (self.position[0], i) for i in range(1, 9) if i != self.position[1]] \
                        + [(i, self.position[1]) for i in range(1, 9) if i != self.position[0]]))


class King(Figure):
    def get_possible_cages_to_move(self):
        res = [(i, j) for i in range(self.position[0] - 1, self.position[0] + 2) for j in
               range(self.position[1] - 1, self.position[1] + 2) if
               0 < i < 9 and 0 < j < 9]
        res.remove(self.position)
        return res
