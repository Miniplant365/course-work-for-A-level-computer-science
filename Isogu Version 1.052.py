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

  
#defining the live system
lives = 3

#defining whether the menu should be displayed
main_menu = True

#creating a state for the leaderboard to be in allowing for it to be permanant
leaderboard = False

#creating a state at which the deathscreen will be at all times till the player dies
deathscreen = False

#initialising the main game as being false
main_game = False

#defining wave so which projectile should be outputted
wave = random.randint(1,3)

# Load images
lives_surface = pygame.image.load('pygame/Graphics/player.png').convert_alpha()
xp_surface = pygame.image.load('pygame/Graphics/xp.png').convert_alpha()
background_surface = pygame.image.load('pygame/Graphics/Lives1.png').convert()
boss_surface = pygame.image.load('pygame/Graphics/Boss1.png').convert_alpha()
player_surf = pygame.image.load('pygame/Graphics/player.png').convert_alpha()
play_button = pygame.image.load('pygame/Graphics/play_button.png').convert_alpha()
quit_button = pygame.image.load('pygame/Graphics/quit_button.png').convert_alpha()
leaderboard_button = pygame.image.load('pygame/Graphics/leaderboard.png').convert_alpha()
menu_backgroundsurface = pygame.image.load('pygame/Graphics/menu_background1.png').convert_alpha()
Leaderboard_menu = pygame.image.load('pygame/Graphics/Leaderboard_1.png').convert_alpha()
You_lose = pygame.image.load('pygame/Graphics/You_lose1.png').convert_alpha()
retry = pygame.image.load('pygame/Graphics/Retry_button.png').convert_alpha()
menu_button = pygame.image.load('pygame/Graphics/Menu_button1.png').convert_alpha()
blackscreen = pygame.image.load('pygame/Graphics/Lives1.png').convert_alpha()

# Set initial positions for sprites
boss_rect = boss_surface.get_rect(midright=(WINDOW_WIDTH, WINDOW_HEIGHT))
player_rect = player_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
play_button_rect = play_button.get_rect(center=(250, 150))
quit_button_rect = quit_button.get_rect(center=(250, 270))
leaderboard_button_rect = leaderboard_button.get_rect(center=(250, 210))
retry_button_rect = retry.get_rect(center = (250, 150))
menu_button_rect = menu_button.get_rect(center=(245, 230))

# creating score variables
score = 0
score_update_time = pygame.time.get_ticks()

# font settings for score display
font = pygame.font.Font("freesansbold.ttf", 10)
fontX, fontY = 15, 33

#this is the player and where all its attrtibutes and methods
class player():
    #player movement
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_rect.top > 0:
            player_rect.y -= 2
        if keys[pygame.K_s] and player_rect.bottom < WINDOW_HEIGHT:
            player_rect.y += 2
        if keys[pygame.K_d] and player_rect.right < WINDOW_WIDTH:
            player_rect.x += 2
        if keys[pygame.K_a] and player_rect.left > 0:
            player_rect.x -= 2

P1 = player()

# Enemy projectile class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame/Graphics/projectile.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT)))

    def move(self):
        global wave
        self.rect.move_ip(-8, 0)
        if self.rect.left < 0:
            self.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))
            wave =  random.randint(1,3)
            

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy2(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame/Graphics/projectile2.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT)))

# establish enemies
E1 = Enemy()
E2 = Enemy2()

#Function to display score
def display_score(x, y):
    score_img = font.render(f"{score}", True, (0, 0, 0))
    screen.blit(score_img, (x, y))

#draws the menu aswell as displaying the buttons
def draw_menu():
    screen.blit(menu_backgroundsurface, (0, 0))
    screen.blit(play_button, play_button_rect)
    screen.blit(quit_button, quit_button_rect)
    screen.blit(leaderboard_button, leaderboard_button_rect)

#creates the main game and how it is displayed
def draw_game():
     # Display background and other sprites such as lives
    screen.blit(background_surface, (0, 0))
    screen.blit(xp_surface, (-10, -20))


    #controls display for lives
    if lives == 3:
        screen.blit(lives_surface, (80, 20))
        screen.blit(lives_surface, (100, 20))
        screen.blit(lives_surface, (120, 20))
    elif lives == 2:
        screen.blit(lives_surface, (80, 20))
        screen.blit(lives_surface, (100, 20))
    elif lives == 1:
        screen.blit(lives_surface, (80, 20))
    
    #this waits for the projectile to leave the screen and then generates another wave meaning another projectile
    #global wave
    #if E1.rect.left <= 0 and E2.rect.left <= 0:
        #wave = random.randint(1,3) 


    # Basic idle movement for the boss
    screen.blit(boss_surface, (350, 120))
    screen.blit(player_surf, player_rect)
     
    
    #player movement
    P1.movement()

    # randomly generating projectiles
    if wave == 1:
        E1.move()
        E1.draw(screen)
        E2.move()
        E2.draw(screen)
    elif wave == 2:
        E2.move()
        E2.draw(screen)    
    elif wave == 3:
        E1.move()
        E1.draw(screen)
        



#function allowing for leaderboard to be displayed    
def draw_leaderboard():
    screen.blit(Leaderboard_menu, (0, 0))

#function which implements the death screen and stops the game
def draw_deathscreen():
    screen.blit(blackscreen,(0,0))
    screen.blit(You_lose, (100, 0))
    screen.blit(retry, retry_button_rect)
    screen.blit(menu_button, menu_button_rect)




# Main game loop
while True:
    #checking for menu
    if main_menu:
        draw_menu()
    elif leaderboard:
        draw_leaderboard()
    elif main_game:
        draw_game()
    elif deathscreen:
        draw_deathscreen()

    # allows player to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # checking if any of the buttons have been pressed
        if main_menu and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_button_rect.collidepoint(mouse_pos):
                    main_game = True
                    main_menu = False
                    leaderboard = False
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
                elif leaderboard_button_rect.collidepoint(mouse_pos):
                    leaderboard = True
                    main_menu = False
                    main_game = False 

    #creating conditions to meet for the death screen to display
    if main_menu == False and leaderboard == False and lives <= 0:
        main_game = False
        deathscreen = True

    if deathscreen and event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        if retry_button_rect.collidepoint(mouse_pos):
            main_menu = False
            leaderboard = False
            main_game = True
            deathscreen = False
            
            #reseting all states when retry button pressed meaning that it is a total reset
            lives = 3
            score = 0

            E1.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))
            E2.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))
            #stops projectiles resuming from original spot
            wave = random.randint(1,3)


        elif menu_button_rect.collidepoint(mouse_pos):
            main_game = False
            main_menu = True
            leaderboard = False
            deathscreen = False

    #creating a key that allows for the user to go back to menu anytime they want
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            deathscreen = False 
            main_game = False
            leaderboard = False
            main_menu = True



    #here we are coding the collisions betwen the player and projectiles
    if player_rect.colliderect(E1.rect) or player_rect.colliderect(E2.rect):
        lives = lives - 1
        player_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        pygame.time.delay(500)  # pause after losing a life
        E1.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))
        E2.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))
        

    # Updates score every second
    if pygame.time.get_ticks() - score_update_time >= 1000 and main_game == True:
        score += 1
        score_update_time = pygame.time.get_ticks()

    display_score(fontX, fontY)

    # updates display and clock ticks
    pygame.display.update()
    clock.tick(60)


    # add new projectile

    # wave generation not working

    #leaderboard displayed when menu pressed

    #animation to boss

    #animation to main menu

    #animation to death screen 

    #change background 

###check list###

#scoring under different screens (done)

#death screen buttons (done)

#wave generation issues (done)

#scoring system implementation

#animation

#new projectile
