# player.py

from constants import PLAYER_START_HP, PLAYER_START_ATTACK, PLAYER_START_DEFENSE, DIRECTIONS, TILE_SIZE

class Player:
    def __init__(self, start_x, start_y):
        self.hp = PLAYER_START_HP
        self.attack = PLAYER_START_ATTACK
        self.defense = PLAYER_START_DEFENSE
        self.level = 1
        self.gold = 0
        self.x = start_x * TILE_SIZE + TILE_SIZE // 2
        self.y = start_y * TILE_SIZE + TILE_SIZE // 2
        self.direction = 'N'

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 2

    def collect_gold(self, amount):
        self.gold += amount

    def move(self, dx, dy, dungeon, enemies):
        new_x = self.x + dx * TILE_SIZE
        new_y = self.y + dy * TILE_SIZE
        tile_x = new_x // TILE_SIZE
        tile_y = new_y // TILE_SIZE

        if dungeon[tile_y][tile_x] == 0:
            self.x = new_x
            self.y = new_y

            for enemy in enemies:
                if enemy.x == tile_x and enemy.y == tile_y:
                    return enemy
        return None

    def move_forward(self, dungeon, enemies):
        dx, dy = DIRECTIONS[self.direction]
        return self.move(dx, dy, dungeon, enemies)

    def move_backward(self, dungeon, enemies):
        dx, dy = DIRECTIONS[self.direction]
        return self.move(-dx, -dy, dungeon, enemies)

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        idx = directions.index(self.direction)
        self.direction = directions[(idx + 1) % 4]

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        idx = directions.index(self.direction)
        self.direction = directions[(idx + 1) % 4]
