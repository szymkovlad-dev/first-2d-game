from venv import create
import pygame

#Inityalize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 1500
WINDOW_HIGH = 900
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGH))
pygame.display.set_caption("2d game")

#Game classes
class Game():
    """A class to help manage gameplay"""

    def __init__(self):
        """initialize the game"""
        pass

    def __update__(self):
        """update the game"""
        pass

    def __draw__(self):
        """draw the game"""
        pass

    def __add_werewolf__(self):
        """add werewolf to the game"""
        pass

    def __check_collisions__(self):
        """check collisions that affect gameplay"""
        pass

    def __check_round_completion__(self):
        """check if player survived"""
        pass

    def __check_game_over__(self):
        """check if player lose the game"""
        pass

    def __start_new_round__(self):
        """start round"""
        pass

    def __pause_game__(self):
        """pause the game"""
        pass

    def __reset_game__(self):
        """reset The game"""
        pass

#Create sprite groups
my_player_group = pygame.sprite.Group()

#Set images
background_image = pygame.image.load("resources/Images/background.png").convert_alpha()
background_image = pygame.transform.scale(background_image,(WINDOW_WIDTH,WINDOW_HIGH))
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)

#The main game loop
running = True
while running:
#Loop through a list of event objects that have occurred
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Blit the background
    display_surface.blit(background_image,background_rect)

#Update display
    pygame.display.update()

#End the game
pygame.quit()