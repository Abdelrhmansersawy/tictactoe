import pygame

# Screen size
SIZE = (600, 400)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tile settings
TILE_SIZE = 80
TILE_ORIGIN = (SIZE[0] / 2 - (1.5 * TILE_SIZE), SIZE[1] / 2 - (1.5 * TILE_SIZE))

# Fonts
pygame.font.init()
LARGE_FONT = pygame.font.Font("OpenSans-Regular.ttf", 40)
MEDIUM_FONT = pygame.font.Font("OpenSans-Regular.ttf", 28)
MOVE_FONT = pygame.font.Font("OpenSans-Regular.ttf", 60)

