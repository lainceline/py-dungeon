# constants.py

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 64
DUNGEON_WIDTH = 10
DUNGEON_HEIGHT = 10
FLOOR_COUNT = 5

PLAYER_START_HP = 100
PLAYER_START_ATTACK = 10
PLAYER_START_DEFENSE = 5

SKELETON_HP = 30
SKELETON_ATTACK = 5
SKELETON_DEFENSE = 2
ENCOUNTER_PROBABILITY = 0.5

GOLD_PER_CHEST = 50

# Player directions
DIRECTIONS = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}
