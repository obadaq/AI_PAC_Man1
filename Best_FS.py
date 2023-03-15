import heapq

# Define the board and obstacles
board = [[2 for _ in range(6)] for _ in range(6)]
board[3][3] = 3  # Ghost position
obstacles = [(3, 3)]


def heuristic():
    # Calculate the number of pills remaining on the board
    return sum(row.count(1) for row in board)


def best_first_search(start):
    # Initialize the heap with the start position and its heuristic value
    heap = [(heuristic(), start)]
    # Keep track of visited positions
    visited = set()
    # Keep track of the directions taken to reach the current position
    directions = []
    while heap:
        # Get the position with the smallest heuristic value from the heap
        _, pos = heapq.heappop(heap)
        if pos in visited:
            continue
        visited.add(pos)
        i, j = pos
        if board[i][j] == 2:  # If the current position has Pacman
            board[i][j] = 0  # Remove Pacman from the current position
            if not any(2 in row for row in board):  # If Pacman has eaten all pills
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
                # Add the neighbor position and its heuristic value to the heap
                heapq.heappush(heap, (heuristic(), (ni, nj)))


best_first_search((1, 2))


