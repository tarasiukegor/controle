# import pygame
# from sys import exit
# # Ініціалізація Pygame
# pygame.init()

# screen = pygame.display.set_mode((800,400))
# pygame.display.set_caption("popa")
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     pygame.display.update()

import pygame

# --- Константи ---
TILE_SIZE = 32  # Розмір клітинки
GRID_SIZE = 20  # 20x20 поле
WIDTH, HEIGHT = TILE_SIZE * GRID_SIZE, TILE_SIZE * GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# --- Ініціалізація Pygame ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG: Графова мапа 20x20")

# --- Створення графа (карти) ---
graph = {}  # Кожна клітинка — вершина графа
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        graph[(x, y)] = []
        if x > 0: graph[(x, y)].append((x - 1, y))  # Ліворуч
        if x < GRID_SIZE - 1: graph[(x, y)].append((x + 1, y))  # Праворуч
        if y > 0: graph[(x, y)].append((x, y - 1))  # Вгору
        if y < GRID_SIZE - 1: graph[(x, y)].append((x, y + 1))  # Вниз

# --- Локації (місця входу) ---
locations = {(5, 5): "Магазин", (10, 10): "Таверна", (15, 15): "Темний ліс"}

# --- Гравець ---
player_pos = (0, 0)  # Початкова позиція
in_location = None  # Якщо True, то гравець у локації

# --- Основний цикл ---
running = True
while running:
    screen.fill(WHITE)

    # --- Малюємо сітку ---
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    # --- Малюємо локації (спеціальні клітинки) ---
    for pos, name in locations.items():
        rect = pygame.Rect(pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, RED, rect)

    # --- Малюємо гравця ---
    pygame.draw.rect(screen, BLUE, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.flip()

    # --- Обробка подій ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not in_location:
            mx, my = pygame.mouse.get_pos()
            target_pos = (mx // TILE_SIZE, my // TILE_SIZE)
            if target_pos in graph[player_pos]:  # Якщо клітинка сусідня
                player_pos = target_pos
                if player_pos in locations:  # Якщо це локація, то входимо в неї
                    in_location = locations[player_pos]

    # --- Якщо гравець у локації ---
    while in_location:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Ви в {in_location}", True, BLACK)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

        exit_text = font.render("Натисніть [E], щоб вийти", True, BLACK)
        screen.blit(exit_text, (WIDTH // 2 - 100, HEIGHT // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                in_location = None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                in_location = None  # Повертаємося на карту

pygame.quit()
