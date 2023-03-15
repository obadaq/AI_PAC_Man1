import heapq
import random

# Define the board and obstacles
board_size = 5
board = [[0 for _ in range(board_size)] for _ in range(board_size)]
pills = set()
ghost_pos = (random.randint(0, board_size-1), random.randint(0, board_size-1))

# Place pills and avoid ghost position
for i in range(board_size):
    for j in range(board_size):
        if (i, j) == ghost_pos:
            board[i][j] = 3
        else:
            board[i][j] = 1
            pills.add((i, j))

def heuristic(pos):
    return min(abs(pos[0] - p[0]) + abs(pos[1] - p[1]) for p in pills)

def a_star(start):
    heap = [(heuristic(start), start)]
    visited = set()
    directions = []
    while heap:
        _, pos = heapq.heappop(heap)
        if pos in visited:
            continue
        visited.add(pos)
        i, j = pos
        if (i, j) in pills:
            pills.remove((i, j))
            if not pills:
                print("Directions:", directions)
                return
            if len(directions) > 0:
                last_i, last_j = directions[-1]
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
            directions.append((i, j))
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < board_size and 0 <= nj < board_size and board[ni][nj] != 3 and (ni, nj) not in visited:
                heapq.heappush(heap, (heuristic((ni, nj)), (ni, nj)))

a_star((0, 0))
