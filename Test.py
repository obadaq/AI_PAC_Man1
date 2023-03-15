import heapq
import numpy as np
import random

class PacmanGame:
    def __init__(self, size=5):
        self.size = size
        self.board = np.full((self.size, self.size), 1)
        self.obstacles = []
        self.ghost_pos = None
        self.PACman_pos = None
        self.directions = []

    def setup(self):
        self.ghost_pos = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        self.board[self.ghost_pos] = 3
        self.obstacles.append(self.ghost_pos)

        self.PACman_pos = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        while self.PACman_pos == self.ghost_pos:
            self.PACman_pos = (random.randint(0, self.size-1), random.randint(0, self.size-1))

        self.board[self.PACman_pos] = 2
        self.start_pos = [self.PACman_pos]
        self.start_point = self.start_pos[0]

        print("PACman start at: ", self.start_point)
        print("Ghost position is in: ", self.ghost_pos)
        print("PACman has to move the following directions to reach the goal")

    def heuristic(self):
        return np.count_nonzero(self.board == 1)

    def best_first_search(self, start):
        heap = [(self.heuristic(), start)]
        visited = set()
        while heap:
            _, pos = heapq.heappop(heap)
            if pos in visited:
                continue
            visited.add(pos)
            i, j = pos
            if self.board[i, j] == 1:
                self.board[i, j] = 0
                if not np.any(self.board == 1):
                    return
                if len(self.directions) > 0:
                    last_i, last_j = self.directions[-1]
                    if last_i == i:
                        if last_j < j:
                            print("Move right")
                        else:
                            print("Move left")
                    else:
                        if last_i < i:
                            print("Move down")
                        else:
                            print("Move up")
                else:
                    print("Start")
                self.directions.append(pos)
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < self.size and 0 <= nj < self.size and self.board[ni, nj] != 3 and (ni, nj) not in visited:
                    heapq.heappush(heap, (self.heuristic(), (ni, nj)))

game = PacmanGame()
game.setup()
game.best_first_search(game.start_point)
