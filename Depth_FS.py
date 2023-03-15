import heapq
from collections import deque

# Define the board and obstacles
board = [[2 for _ in range(6)] for _ in range(6)]
board[3][3] = 3  # Ghost position
obstacles = [(3, 3)]


def heuristic(node):
    return abs(node[0]-5) + abs(node[1]-5)


def depth_first_search(start):
    stack = [(start, [start])]
    visited = set()
    while stack:
        pos, path = stack.pop()
        if pos in visited:
            continue
        visited.add(pos)
        i, j = pos
        if board[i][j] == 2:
            board[i][j] = 0
            if not any(2 in row for row in board):
                print("Directions:", path)
                return
            if len(path) > 1:
                last_i, last_j = path[-2]
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
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < 5 and 0 <= nj < 5 and board[ni][nj] != 3 and (ni, nj) not in visited:
                stack.append(((ni, nj), path + [(ni, nj)]))

depth_first_search((0, 0))
