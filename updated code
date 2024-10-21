import pygame
from sys import exit
import random

#creates the window of which the game will take place 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 300
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Isogu")
#here we are adding a clock so we can add a frame rate to our game
clock = pygame.time.Clock()

#here we are fetching the images created from my files to create the background and score sprites
xp_surface = pygame.image.load('pygame/Graphics/xp.png').convert_alpha()
background_surface = pygame.image.load('pygame/Graphics/background.png').convert()

#fetches boss sprite while adding a hitbox 
enemy_surface = pygame.image.load('pygame/Graphics/enemy1.png').convert_alpha()
enemy_rect = enemy_surface.get_rect(midright = (WINDOW_WIDTH , WINDOW_HEIGHT ))

#fetches main character sprite and adds hitbox
player_surf = pygame.image.load('pygame/Graphics/player.png').convert_alpha()
player_rect = player_surf.get_rect(center = (WINDOW_WIDTH /2 , WINDOW_HEIGHT /2))






#creating a class for the projectiles which will help for the future when creating more
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame/Graphics/projectile.png').convert_alpha()
        self.surf = pygame.Surface((45,45))
        self.rect = self.surf.get_rect(center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT)))

    #when the projectile leaves the screen it will create a new one
    def move(self):
        self.rect.move_ip(-5,0)
        if (self.rect.left < 0): 
            self.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))

    #simply displays the projectile
    def draw(self, surface):
        surface.blit(self.image, self.rect)

#creating the second projectile to go allong side it
class enemy2(enemy):
    def __init__(self):
        super().__init__()  # Calls the parent class constructor
        self.image = pygame.image.load('pygame/Graphics/projectile2.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT)))

#here we are giving these variables a class to be executed later       
E1 = enemy()
E2 = enemy2()







while True:
    # allows the user to be able to quit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#player movement 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= 2
    if keys[pygame.K_s]:
        player_rect.y += 2
    if keys[pygame.K_d]:
        player_rect.x += 2
    if keys[pygame.K_a]:
        player_rect.x -= 2

    
    # displays all fetched sprites on a surface
    screen.blit(background_surface,(0,0))
    screen.blit(xp_surface,(-10,-20))
    #basic idle movement for the boss
    enemy_rect.y -= 2
    if enemy_rect.bottom <= 0: enemy_rect.top = 300
    screen.blit(enemy_surface,enemy_rect)
    screen.blit(player_surf,player_rect)
    
    #here we are implementing each of the classes executing there methods
    E1.move()
    E1.draw(screen)
    E2.move()
    E2.draw(screen)

    #this is what the screens frame rate will be 
    pygame.display.update()
    clock.tick(60)


