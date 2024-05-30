# dungeon.py

import random
from constants import DUNGEON_WIDTH, DUNGEON_HEIGHT, FLOOR_COUNT, ENCOUNTER_PROBABILITY
from skeleton import Skeleton

class Dungeon:
    def __init__(self):
        self.floors = [self.generate_maze() for _ in range(FLOOR_COUNT)]
        self.start_x, self.start_y = self.find_starting_position(self.floors[0])
        self.enemies = self.place_enemies(self.floors[0])

    def generate_maze(self):
        maze = [[1 for _ in range(DUNGEON_WIDTH)] for _ in range(DUNGEON_HEIGHT)]

        def carve_passages_from(cx, cy, maze):
            directions = [(0, -2), (0, 2), (2, 0), (-2, 0)]
            random.shuffle(directions)
            for direction in directions:
                nx, ny = cx + direction[0], cy + direction[1]
                if 0 <= nx < DUNGEON_WIDTH and 0 <= ny < DUNGEON_HEIGHT and maze[ny][nx] == 1:
                    maze[cy + direction[1] // 2][cx + direction[0] // 2] = 0
                    maze[ny][nx] = 0
                    carve_passages_from(nx, ny, maze)

        start_x, start_y = 1, 1
        maze[start_y][start_x] = 0
        carve_passages_from(start_x, start_y, maze)

        return maze

    def find_starting_position(self, maze):
        for y in range(DUNGEON_HEIGHT):
            for x in range(DUNGEON_WIDTH):
                if maze[y][x] == 0:
                    return x, y
        return 1, 1  # Default starting position if no path found

    def place_enemies(self, maze):
        enemies = []
        for y in range(DUNGEON_HEIGHT):
            for x in range(DUNGEON_WIDTH):
                if maze[y][x] == 0 and random.random() < ENCOUNTER_PROBABILITY:
                    enemies.append(Skeleton(x, y))
        return enemies
