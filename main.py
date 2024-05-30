# main.py

import pygame
import sys
from player import Player
from dungeon import Dungeon
from graphics import Graphics
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from battle import Battle

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    graphics = Graphics(screen)

    dungeon = Dungeon()
    start_x, start_y = dungeon.start_x, dungeon.start_y
    player = Player(start_x, start_y)

    current_floor = 0
    in_battle = False
    battle = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not in_battle:
                    if event.key == pygame.K_w:
                        enemy = player.move_forward(dungeon.floors[current_floor], dungeon.enemies)
                        if enemy:
                            in_battle = True
                            battle = Battle(screen, player, enemy)
                    elif event.key == pygame.K_s:
                        enemy = player.move_backward(dungeon.floors[current_floor], dungeon.enemies)
                        if enemy:
                            in_battle = True
                            battle = Battle(screen, player, enemy)
                    elif event.key == pygame.K_a:
                        player.turn_left()
                    elif event.key == pygame.K_d:
                        player.turn_right()
                else:
                    if event.key == pygame.K_SPACE:
                        battle.update()
                        if player.hp <= 0 or battle.enemy.hp <= 0:
                            in_battle = False
                            battle = None

        screen.fill((0, 0, 0))
        if not in_battle:
            graphics.draw_first_person_view(player, dungeon.floors[current_floor])
            graphics.draw_overhead_map(player, dungeon.floors[current_floor])
            graphics.draw_debug_info(player, dungeon.floors[current_floor])
        else:
            battle.draw_battle_screen()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
