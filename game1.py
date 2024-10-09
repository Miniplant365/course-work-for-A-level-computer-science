import pygame
from sys import exit

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 300
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Isogu")
clock = pygame.time.Clock()

xp_surface = pygame.image.load('pygame/Graphics/xp.png').convert_alpha()
background_surface = pygame.image.load('pygame/Graphics/background.png').convert()

enemy_surface = pygame.image.load('pygame/Graphics/enemy1.png').convert_alpha()
enemy_rect = enemy_surface.get_rect(midright = (WINDOW_WIDTH , WINDOW_HEIGHT ))

player_surf = pygame.image.load('pygame/Graphics/player.png').convert_alpha()
player_rect = player_surf.get_rect(center = (WINDOW_WIDTH /2 , WINDOW_HEIGHT /2))

while True:
    # allows the user to be able to quit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= 2
    if keys[pygame.K_s]:
        player_rect.y += 2
    if keys[pygame.K_d]:
        player_rect.x += 2
    if keys[pygame.K_a]:
        player_rect.x -= 2

    
    

    # creates background
    screen.blit(background_surface,(0,0))
    screen.blit(xp_surface,(-10,-20))

    enemy_rect.y -= 2
    if enemy_rect.bottom <= 0: enemy_rect.top = 300
    screen.blit(enemy_surface,enemy_rect)
    screen.blit(player_surf,player_rect)
    
    pygame.display.update()
    clock.tick(60)


