import pygame
import heapq


class Pacman:
    def __init__(self, position):
        self.position = position
        self.direction = "right"

class Board:
    def __init__(self, layout):
        self.layout = layout
        self.rows = len(layout)
        self.cols = len(layout[0])
        self.start = None
        self.goal = None
        self.pacman = None

def main():
    pygame.init()

    board = Board([["#", "#", "#", "#", "#"],
                   ["#", ".", ".", ".", "#"],
                   ["#", ".", "#", ".", "#"],
                   ["#", ".", ".", ".", "#"],
                   ["#", "#", "#", "#", "#"]])

    pac_man = Pacman((1, 1))

    open_list = []
    closed_list = []

    heapq.heappush(open_list, (0, pac_man))

    while open_list:
        current = heapq.heappop(open_list)[1]
        closed_list.append(current)

        if board.layout[current.position[0]][current.position[1]] == ".":
            board.layout[current.position[0]][current.position[1]] = " "

        if current.position == board.goal:
            print("Found the goal!")
            break

        for move in ["left", "right", "up", "down"]:
            if can_move(current, move):
                new_position = get_new_position(current, move)
                new_pac_man = Pacman(new_position)

                if new_pac_man not in closed_list:
                    new_pac_man.direction = move
                    heapq.heappush(open_list, (get_heuristic(new_pac_man, board.goal), new_pac_man))


def can_move(pac_man, direction):
    row, col = pac_man.position

    if direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    elif direction == "up":
        row -= 1
    elif direction == "down":
        row += 1

    return Board.layout[row][col] != "#"


def get_new_position(pac_man, direction):
    row, col = pac_man.position

    if direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    elif direction == "up":
        row -= 1
    elif direction == "down":
        row += 1

    return (row, col)


def get_heuristic(pac_man, goal):
    return abs(pac_man.position[0] - goal[0]) + abs(pac_man.position[1] - goal[1])

if __name__ == "__main__":
    main()
