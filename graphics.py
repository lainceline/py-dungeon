# graphics.py

import pygame
from math import sin, cos, radians
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, DIRECTIONS

class Graphics:
    def __init__(self, screen):
        self.screen = screen

    def draw_first_person_view(self, player, dungeon):
        self.screen.fill((0, 0, 0))

        px, py = player.x / TILE_SIZE, player.y / TILE_SIZE
        direction = player.direction
        view_depth = 10  # How far the player can see
        fov = 60  # Field of view in degrees
        num_rays = SCREEN_WIDTH  # Number of rays to cast

        def cast_ray(x, y, angle):
            angle_rad = radians(angle)  # Convert angle to radians
            dx = cos(angle_rad)
            dy = sin(angle_rad)
            for depth in range(1, view_depth * TILE_SIZE + 1):
                nx, ny = x + dx * depth / TILE_SIZE, y + dy * depth / TILE_SIZE
                if 0 <= int(nx) < len(dungeon[0]) and 0 <= int(ny) < len(dungeon):
                    if dungeon[int(ny)][int(nx)] == 1:
                        return depth / TILE_SIZE, (nx, ny)
            return None, None

        direction_angles = {'N': 90, 'S': 270, 'E': 0, 'W': 180}
        base_angle = direction_angles[direction]
        half_fov = fov / 2

        for ray in range(num_rays):
            angle = base_angle - half_fov + (ray * fov / num_rays)
            depth, wall_pos = cast_ray(px, py, angle)
            if depth is not None:
                scale = 1 / depth
                wall_height = int(SCREEN_HEIGHT * scale)
                if depth < 1:
                    wall_height = int(wall_height * 0.7)  # Shrink wall if close to the player
                wall_width = 1  # Each ray is 1 pixel wide
                color = (255, 255, 255)
                pygame.draw.rect(self.screen, color, (
                    ray,  # X position based on the ray index
                    SCREEN_HEIGHT // 2 - wall_height // 2,
                    wall_width,
                    wall_height
                ))

    def draw_overhead_map(self, player, dungeon, map_scale=5):
        map_width = len(dungeon[0]) * map_scale
        map_height = len(dungeon) * map_scale
        map_surface = pygame.Surface((map_width, map_height))

        # Draw the dungeon
        for y, row in enumerate(dungeon):
            for x, tile in enumerate(row):
                color = (0, 0, 0) if tile == 0 else (255, 255, 255)
                pygame.draw.rect(map_surface, color, (x * map_scale, y * map_scale, map_scale, map_scale))

        # Draw the player
        player_x = player.x * map_scale // TILE_SIZE
        player_y = player.y * map_scale // TILE_SIZE
        pygame.draw.circle(map_surface, (0, 0, 255), (player_x, player_y), map_scale // 2)

        # Draw the direction
        direction_vectors = {
            'N': (0, -1),
            'S': (0, 1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        dx, dy = direction_vectors[player.direction]
        line_end_x = player_x + dx * map_scale
        line_end_y = player_y + dy * map_scale
        pygame.draw.line(map_surface, (0, 0, 255), (player_x, player_y), (line_end_x, line_end_y), 2)

        # Blit the map to the screen
        self.screen.blit(map_surface, (SCREEN_WIDTH - map_width - 10, 10))

    def draw_debug_info(self, player, dungeon):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player Position: ({player.x // TILE_SIZE}, {player.y // TILE_SIZE}) Direction: {player.direction}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
