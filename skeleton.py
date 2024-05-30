# skeleton.py

from constants import SKELETON_HP, SKELETON_ATTACK, SKELETON_DEFENSE

class Skeleton:
    def __init__(self, x, y):
        self.hp = max(SKELETON_HP, 1)
        self.attack = SKELETON_ATTACK
        self.defense = SKELETON_DEFENSE
        self.x = x
        self.y = y
