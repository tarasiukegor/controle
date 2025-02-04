import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Map Navigation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)
GRAY = (169, 169, 169)

# Fonts
font = pygame.font.Font(None, 36)

# Game states
MAIN_MAP = "main_map"
TAVERN = "tavern"
CITY_HALL = "city_hall"
MARKET = "market"
FOREST = "forest"
current_state = MAIN_MAP

# Player state
room_taken = False
drunkard_helped = False

def draw_main_map():
    screen.fill(GREEN)
    locations = {
        "Tavern": (100, 200),
        "City Hall": (300, 200),
        "Market": (500, 200),
        "Forest": (700, 200)
    }
    for name, pos in locations.items():
        pygame.draw.rect(screen, BROWN, (pos[0], pos[1], 120, 80))
        text = font.render(name, True, WHITE)
        screen.blit(text, (pos[0] + 10, pos[1] + 25))
    return locations

def draw_tavern():
    screen.fill(BROWN)
    options = ["Talk to Innkeeper", "Talk to Drunkard", "Get a Drink", "Leave"]
    for i, option in enumerate(options):
        text = font.render(option, True, WHITE)
        screen.blit(text, (WIDTH//2 - 100, 180 + i * 50))
    return options

dialogue_active = False
dialogue_node = 1
talking_to = "innkeeper"

def get_dialogue_graphs():
    return {
        "innkeeper": {
            1: ("Hello, traveler! Welcome to the Tavern.", {"Who are you?": 2, "Goodbye.": None}),
            2: ("I am the innkeeper. How can I help you?", {"I need a room.": 3 if not room_taken else 5, "Just looking around.": None}),
            3: ("We have cozy rooms for 5 gold.", {"I'll take one.": 4, "Too expensive.": None}) if not room_taken else None,
            4: ("Here is your key. Enjoy your stay!", None),
            5: ("You already took a room. Enjoy your stay!", None)
        },
        "drunkard": {
            1: ("*Hic* You got some coin for a drink?", {"Here, take one gold.": 2 if not drunkard_helped else 3, "No, go away.": None}),
            2: ("You're a real friend! *Hic* Cheers!", {"Enjoy!": None}) if not drunkard_helped else None,
            3: ("You already gave me a drink! *Hic* Thanks again!", None)
        }
    }

def draw_dialogue():
    global dialogue_node, talking_to
    pygame.draw.rect(screen, BLACK, (100, 400, 600, 150))
    dialogue_graphs = get_dialogue_graphs()
    
    if dialogue_node is None or talking_to not in dialogue_graphs or dialogue_graphs[talking_to].get(dialogue_node) is None:
        return None
    
    text, choices = dialogue_graphs[talking_to][dialogue_node]
    text_render = font.render(text, True, WHITE)
    screen.blit(text_render, (120, 420))
    
    y_offset = 460
    for choice, next_node in (choices or {}).items():
        choice_render = font.render(choice, True, WHITE)
        screen.blit(choice_render, (120, y_offset))
        y_offset += 40
    
    close_button = font.render("Close", True, WHITE)
    pygame.draw.rect(screen, GRAY, (650, 450, 100, 40))
    screen.blit(close_button, (670, 460))
    
    return choices

def main():
    global current_state, dialogue_active, dialogue_node, talking_to, room_taken, drunkard_helped
    running = True
    while running:
        screen.fill(WHITE)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if current_state == MAIN_MAP:
            locations = draw_main_map()
        elif current_state == TAVERN:
            options = draw_tavern()
            if dialogue_active:
                choices = draw_dialogue()
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_state == MAIN_MAP:
                    for name, pos in locations.items():
                        x, y = pos
                        if x <= mouse_x <= x + 120 and y <= mouse_y <= y + 80:
                            current_state = name.lower().replace(" ", "_")
                elif current_state == TAVERN:
                    if 180 <= mouse_y <= 230:
                        talking_to = "innkeeper"
                        dialogue_active = True
                        dialogue_node = 1
                    elif 230 <= mouse_y <= 280:
                        talking_to = "drunkard"
                        dialogue_active = True
                        dialogue_node = 1
                    elif 280 <= mouse_y <= 330:
                        print("You got a drink!")
                    elif 330 <= mouse_y <= 380:
                        current_state = MAIN_MAP
                        dialogue_active = False
                    elif dialogue_active:
                        if 650 <= mouse_x <= 750 and 450 <= mouse_y <= 490:
                            dialogue_active = False
                        else:
                            y_offset = 460
                            for choice, next_node in (choices or {}).items():
                                if y_offset <= mouse_y <= y_offset + 40:
                                    if next_node:
                                        dialogue_node = next_node
                                        if talking_to == "innkeeper" and dialogue_node == 4:
                                            room_taken = True
                                        elif talking_to == "drunkard" and dialogue_node == 2:
                                            drunkard_helped = True
                                    else:
                                        dialogue_active = False
                                    break
                                y_offset += 40
    
    pygame.quit()

if __name__ == "__main__":
    main()
