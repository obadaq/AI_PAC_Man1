import heapq

# Define the board and obstacles
board = [[2 for _ in range(6)] for _ in range(6)]
board[4][4] = 3  # Ghost position
obstacles = [(4, 4)]


def heuristic():
    return sum(row.count(2) for row in board)


def best_first_search(start):
    heap = [(heuristic(), start)]
    visited = set()
    directions = []
    while heap:
        _, pos = heapq.heappop(heap)
        if pos in visited:
            continue
        visited.add(pos)
        i, j = pos
        if board[i][j] == 2:
            board[i][j] = 0
            if not any(2 in row for row in board):
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
            directions.append(pos)
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < 5 and 0 <= nj < 5 and board[ni][nj] != 3 and (ni, nj) not in visited:
                heapq.heappush(heap, (heuristic(), (ni, nj)))


best_first_search((0, 0))