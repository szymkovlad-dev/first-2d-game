from venv import create
import pygame

#Inityalize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 1500
WINDOW_HIGH = 900
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGH))
pygame.display.set_caption("2d game")

#The main game loop
running = True
while running:
#Loop through a list of event objects that have occurred
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#End the game
pygame.quit()