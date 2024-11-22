import pygame
from sys import exit
import random
from datetime import datetime

# Initialize game and create display window
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 300
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Isogu")
clock = pygame.time.Clock()

# Load images
xp_surface = pygame.image.load('pygame/Graphics/xp.png').convert_alpha()
background_surface = pygame.image.load('pygame/Graphics/background.png').convert()
enemy_surface = pygame.image.load('pygame/Graphics/enemy1.png').convert_alpha()
player_surf = pygame.image.load('pygame/Graphics/player.png').convert_alpha()

# Set initial positions for sprites
enemy_rect = enemy_surface.get_rect(midright=(WINDOW_WIDTH, WINDOW_HEIGHT))
player_rect = player_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# Initialize score variables
score = 0
score_update_time = pygame.time.get_ticks()#

# Font settings for score display
font = pygame.font.Font("freesansbold.ttf", 10)
fontX, fontY = 15, 33

#this is the player and where all its attrtibutes and methods
class player():
    #player movement
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: player_rect.y -= 2
        if keys[pygame.K_s]: player_rect.y += 2
        if keys[pygame.K_d]: player_rect.x += 2
        if keys[pygame.K_a]: player_rect.x -= 2
    

P1 = player()

# Enemy projectile class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame/Graphics/projectile.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT)))

    def move(self):
        self.rect.move_ip(-5, 0)
        if self.rect.left < 0:
            self.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy2(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame/Graphics/projectile2.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT)))

# Instantiate enemies
E1 = Enemy()
E2 = Enemy2()

# Function to display score
def display_score(x, y):
    score_img = font.render(f"{score}", True, (0, 0, 0))
    screen.blit(score_img, (x, y))

# Main game loop
while True:
    # Event handling for quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if player_rect.colliderect(enemy_rect):
        score += 100

    # Update score every second
    if pygame.time.get_ticks() - score_update_time >= 1000:
        score += 1
        score_update_time = pygame.time.get_ticks()

    # Display background and other sprites
    screen.blit(background_surface, (0, 0))
    screen.blit(xp_surface, (-10, -20))
    
    # Basic idle movement for the boss
    enemy_rect.y -= 2
    if enemy_rect.bottom <= 0: enemy_rect.top = WINDOW_HEIGHT
    screen.blit(enemy_surface, enemy_rect)
    screen.blit(player_surf, player_rect)

    # Display the score
    display_score(fontX, fontY)
    
    # Move and draw the projectiles
    E1.move()
    E1.draw(screen)
    E2.move()
    E2.draw(screen)
    P1.movement()

    # Update display and tick clock
    pygame.display.update()
    clock.tick(60)
