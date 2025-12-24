from venv import create
import pygame, random

vector = pygame.math.Vector2

#Inityalize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 1500
WINDOW_HIGH = 900
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGH))
pygame.display.set_caption("2d game")

#Sets FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Game classes
class Game():
    """A class to help manage gameplay"""

    def __init__(self):
        """initialize the game"""
        pass

    def update(self):
        """update the game"""
        pass

    def draw(self):
        """draw the game"""
        pass

    def add_werewolf(self):
        """add werewolf to the game"""
        pass

    def check_collisions(self):
        """check collisions that affect gameplay"""
        pass

    def check_round_completion(self):
        """check if player survived"""
        pass

    def check_game_over(self):
        """check if player lose the game"""
        pass

    def start_new_round(self):
        """start round"""
        pass

    def pause_game(self):
        """pause the game"""
        pass

    def reset_game(self):
        """reset The game"""
        pass

class Player(pygame.sprite.Sprite):
    """a class the user can control"""

    def __init__(self, x, y):
        """initialize the player"""
        super().__init__()

        #set constant variables
        self.HORISONTAL_ACCELERATION = 2
        self.VERTICAL_ACCELERATION = 0.8
        self.HORISONTAL_FRICTION = 0.15
        self.speed = 7

        # List os sprites
        self.move_right_sprites = []

        image = pygame.image.load(
            "resources/Images/skeleton_idle.png"
        ).convert_alpha()
        image = pygame.transform.scale(image, (150, 150))

        self.move_right_sprites.append(image)

        self.current_sprite = 0
        self.image = self.move_right_sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)


    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def move(self):
        """move the player"""
        self.acceleration = vector(0,self.VERTICAL_ACCELERATION)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1*self.HORISONTAL_ACCELERATION
            self.animate(self.move_right_sprites, 1)
        if keys[pygame.K_RIGHT]:
            self.acceleration.x = -1 * self.HORISONTAL_ACCELERATION
            self.animate(self.move_right_sprites, 1)

    def check_collisions(self):
        """check for collisions with platforms """
        pass

    def check_animations(self):
        """check to see if jump/fire animations"""
        pass

    def jump(self):
        """jump"""
        pass

    def fire(self):
        """fire a bullet from sword"""
        pass

    def reset(self):
        """reset player position"""
        pass

    def animate(self,sprite_list,speed):
        """animate the player actions"""
        if self.current_sprite < len(sprite_list)-1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]



#Create sprite groups
my_player_group = pygame.sprite.Group()
player = Player(50,810)
my_player_group.add(player)

#Set images
background_image = pygame.image.load("resources/Images/1_game_background.png").convert_alpha()
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

#update an draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)
#Update display
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()
