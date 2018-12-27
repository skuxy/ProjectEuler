#! /usr/bin/env python
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

from itertools import permutations

POSSIBLE_DIRECTIONS = ('D', 'R')


class Grid:
    def __init__(self, x_len, y_len):
        self.x_len = x_len
        self.y_len = y_len

    def get_all_paths(self):
        """ This is bruteforce version """
        return permutations('D' * self.x_len + 'R' * self.y_len)

    def count_all_paths(self):
        cnt = 0
        for _ in self.get_all_paths():
            cnt += 1

        return cnt


if __name__ == "__main__":
    g = Grid(20, 20)
    print(g.count_all_paths())
