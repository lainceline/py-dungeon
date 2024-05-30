# battle.py

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Battle:
    def __init__(self, screen, player, enemy):
        self.screen = screen
        self.player = player
        self.enemy = enemy
        self.turn = 'player'
        self.log = []

    def draw_battle_screen(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)

        # Draw player
        player_text = font.render(f'Player HP: {self.player.hp}', True, (255, 255, 255))
        self.screen.blit(player_text, (50, 50))

        # Draw enemy
        enemy_text = font.render(f'Skeleton HP: {self.enemy.hp}', True, (255, 255, 255))
        self.screen.blit(enemy_text, (SCREEN_WIDTH - 250, 50))

        # Draw ASCII Skeleton
        ascii_skeleton = [
            "  _____ ",
            " /     \\",
            "| () () |",
            " \\  ^  /",
            "  ||||| ",
            "  ||||| "
        ]
        for i, line in enumerate(ascii_skeleton):
            line_text = font.render(line, True, (255, 255, 255))
            self.screen.blit(line_text, (SCREEN_WIDTH - 250, 100 + i * 20))

        # Draw combat log
        log_y = 300
        for log_entry in self.log[-5:]:  # Display last 5 log entries
            log_text = font.render(log_entry, True, (255, 255, 255))
            self.screen.blit(log_text, (50, log_y))
            log_y += 30

        pygame.display.flip()

    def update(self):
        if self.turn == 'player':
            self.player_attack()
        else:
            self.enemy_attack()

    def player_attack(self):
        damage = max(0, self.player.attack - self.enemy.defense)
        self.enemy.hp -= damage
        self.log.append(f"Player attacks! Skeleton takes {damage} damage.")
        self.turn = 'enemy'
        if self.enemy.hp <= 0:
            self.log.append('Player won the battle!')

    def enemy_attack(self):
        damage = max(0, self.enemy.attack - self.player.defense)
        self.player.hp -= damage
        self.log.append(f"Skeleton attacks! Player takes {damage} damage.")
        self.turn = 'player'
        if self.player.hp <= 0:
            self.log.append('Player is defeated!')
