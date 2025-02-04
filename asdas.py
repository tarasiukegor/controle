import pygame

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 32)
# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visual Novel RPG")

room_surface = pygame.image.load('room.jpg')
room_surface = pygame.transform.scale(room_surface, (800,600))
# Game states
INTRO, CHOICE, CONFIRM, INVENTORY = "intro", "choice", "confirm", "inventory"
game_state = INTRO

# Intro text
intro_text = [
    "It was a dark and stormy night...",
    "You find yourself in an unfamiliar place.",
    "There are three objects in front of you...",
    "Choose wisely."
]
current_line = 0

def draw_text(text, x, y):
    rendered_text = FONT.render(text, True, WHITE)
    screen.blit(rendered_text, (x, y))

# Character class
class Character:
    def __init__(self):
        self.inventory = []
    
    def add_item(self, item):
        if len(self.inventory) == 0:  # Only allow one item selection
            self.inventory.append(item)

player = Character()

# Items and positions
items = ["Sword", "Shield", "Potion"]
item_positions = [(200, 400), (350, 400), (500, 400)]
selected_item = None

running = True
while running:
    screen.fill(BLACK)
    
    if game_state == INTRO:
        draw_text(intro_text[current_line], WIDTH//2, HEIGHT // 1.2)
    
    elif game_state == CHOICE:
        screen.blit(room_surface, (0,0))
        draw_text("Choose an item:", 300, 100)
        for i, (item, pos) in enumerate(zip(items, item_positions)):
            pygame.draw.rect(screen, BLACK, (*pos, 100, 50))
            draw_text(item, pos[0] + 10, pos[1] + 15)
    
    elif game_state == CONFIRM:
        screen.fill((150, 150, 150))
        draw_text(f"Confirm selection: {selected_item}?", 250, 250)
        pygame.draw.rect(screen, BLACK, (250, 350, 100, 50))
        draw_text("Yes", 275, 365)
        pygame.draw.rect(screen, BLACK , (450, 350, 100, 50))
        draw_text("No", 475, 365)
    
    elif game_state == INVENTORY:
        screen.fill((50, 50, 50))
        draw_text("Inventory:", 300, 100)
        for i, item in enumerate(player.inventory):
            draw_text(f"- {item}", 300, 150 + i * 40)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if game_state == INTRO and event.key == pygame.K_SPACE:
                current_line += 1
                if current_line >= len(intro_text):
                    game_state = CHOICE
            
        if game_state == CHOICE and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i, pos in enumerate(item_positions):
                rect = pygame.Rect(*pos, 100, 50)
                if rect.collidepoint(x, y):
                    selected_item = items[i]
                    game_state = CONFIRM
                    
        if game_state == CONFIRM and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            yes_rect = pygame.Rect(250, 350, 100, 50)
            no_rect = pygame.Rect(450, 350, 100, 50)
            if yes_rect.collidepoint(x, y):
                player.add_item(selected_item)
                game_state = INVENTORY
            elif no_rect.collidepoint(x, y):
                game_state = CHOICE
print("popa")
pygame.quit()
