import pygame
from map import gamestate, font
import textwrap
from dialogue import *

def run_intro(screen):
    
    # 1 scene
    intro_text = [
        "Vous êtes réveillé par votre serviteur qui vous dit",
        "«Vous m'avez demandé de vous réveiller tôt aujourd'hui»",
        "Michel : Hmpf... Quelle heure est-il ?",
        "Michel se lève brusquement et regarde autour de lui.",
        "\"Je dois partir à 9h30, je dois me dépêcher.\"",
        "Michel s'habille rapidement.",
        "Michel prend un objet parmi trois",
        "Michelle met un autre objet dans la valise"
    ]
    show_text(screen, intro_text)
    
    # 2 scene
    chosen_item = choose_item(screen)
    if chosen_item == "Boîte à cigarettes en bronze":
        dialogues_list["Maire"].supprimer_arc(maire_phrases[0],maire_phrases[2])
        dialogues_list["Maire"].ajouter_arc(maire_phrases[0],maire_phrases[1], ["bonjour"])
    gamestate.inventory.append(chosen_item)

    

    gamestate.current_npc = "Chaffeur"



def show_text(screen, text_lines):
    screen.fill((0, 0, 0))  # Black background
    y_offset = 100
    for line in text_lines:
        waiting = True
        while waiting:
            screen.fill((0, 0, 0))  # Clear screen each time
            screen.blit((font.render("\"espace\" pour continuer",True,'white')),(230,500))

            text_surface = font.render(line, True, "white")
            screen.blit(text_surface, (20, y_offset))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False  # Move to the next line
            
            pygame.time.delay(100)  # Small delay to prevent rapid skipping
        

def choose_item(screen):
    items = ["Boîte à cigarettes en bronze", "Argent extra", "Petite bouteille de vin"]
    item_buttons = []
    selected_item = None
    screen.fill((0, 0, 0))
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit((font.render("Choisir avec soin, ce choix peut être utile plus tard",True,"white")),(20,100))
        for i, item in enumerate(items):
            button_rect = pygame.Rect(100, 200 + i * 60, 400, 50)
            color = "grey" if item != selected_item else "green"
            pygame.draw.rect(screen, color, button_rect)
            text_surface = font.render(item, True, "white")
            screen.blit(text_surface, (button_rect.x + 10, button_rect.y + 10))
            item_buttons.append((button_rect, item))
        
        confirm_button = pygame.Rect(100, 400, 200, 50)
        pygame.draw.rect(screen, "blue", confirm_button)
        confirm_text = font.render("Confirmer", True, "white")
        screen.blit(confirm_text, (confirm_button.x + 10, confirm_button.y + 10))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button_rect, item in item_buttons:
                    if button_rect.collidepoint(event.pos):
                        selected_item = item
                if confirm_button.collidepoint(event.pos) and selected_item:
                    return selected_item
        
        pygame.time.delay(100)