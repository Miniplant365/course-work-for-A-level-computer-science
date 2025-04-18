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

#creating a state that the intro animation will be in
intro = False

#creating a state for the leaderboard to be in allowing for it to be permanant
leaderboard = False

#creating a state at which the deathscreen will be at all times till the player dies
deathscreen = False

#initialising the main game as being false
main_game = False

#defining wave so which projectile should be outputted
wave = random.randint(1,5)

#an array to hold all the scores to be displayed
scoringboard = []

#creating a group to store all the animations together
movinganimations = pygame.sprite.Group()

#a group to withstand the bosses animations
bossanimationgroup = pygame.sprite.Group()

#creating an animation group to hold the projectiles
projectilegroup = pygame.sprite.Group()

# creating score variables
score = 0
score_update_time = pygame.time.get_ticks()

# font settings for score display
font = pygame.font.Font("freesansbold.ttf", 10)
fontX, fontY = 15, 33

# Load images
lives_surface = pygame.image.load('pygame/Graphics/player.png').convert_alpha()
xp_surface = pygame.image.load('pygame/Graphics/xp.png').convert_alpha()
background_surface = pygame.image.load('pygame/Graphics/Lives4.png').convert()
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
titlecard =  pygame.image.load('pygame/Graphics/ISOGU.png').convert_alpha()

# Set initial positions for sprites
boss_rect = boss_surface.get_rect(midright=(WINDOW_WIDTH, WINDOW_HEIGHT))
player_rect = player_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
play_button_rect = play_button.get_rect(center=(250, 150))
quit_button_rect = quit_button.get_rect(center=(250, 270))
leaderboard_button_rect = leaderboard_button.get_rect(center=(250, 210))
retry_button_rect = retry.get_rect(center = (250, 150))
menu_button_rect = menu_button.get_rect(center=(245, 230))

class backgroundanimation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animationback = []
        self.is_animating = False
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background1.png').convert_alpha())
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background2.png').convert_alpha())
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background3.png').convert_alpha())
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background4.png').convert_alpha())
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background5.png').convert_alpha())
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background6.png').convert_alpha())
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background7.png').convert_alpha())
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background8.png').convert_alpha())
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background9.png').convert_alpha())
        self.animationback.append(pygame.image.load ('pygame/Graphics/menu_background10.png').convert_alpha())
        self.current_frameofback = 0
        self.image = self.animationback[self.current_frameofback]

        self.rect = self.image.get_rect(topleft=(0, 0))
    
    def animate(self):
        self.is_animating = True

    def update(self):
       
       if self.is_animating == True:
        self.current_frameofback += 0.2

        if self.current_frameofback >= len(self.animationback):
                self.current_frameofback = 0

        self.image = self.animationback[int(self.current_frameofback)]

class bossanimation(backgroundanimation):
    def __init__(self):
        super().__init__ ()
        self.animation_boss = []
        self.is_animating = False
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss1.png').convert_alpha())
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss2.png').convert_alpha())
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss3.png').convert_alpha())
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss4.png').convert_alpha())
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss5.png').convert_alpha())
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss6.png').convert_alpha())
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss7.png').convert_alpha())
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss8.png').convert_alpha())
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss9.png').convert_alpha())
        self.animation_boss.append(pygame.image.load ('pygame/Graphics/boss10.png').convert_alpha())
        self.current_frameofboss = 0
        self.image = self.animation_boss[self.current_frameofboss]

        self.rect = self.image.get_rect(midright=(500, 150))

    def animate(self):
        self.is_animating = True

    def update(self):
       
       if self.is_animating == True:
        self.current_frameofboss += 0.15

        if self.current_frameofboss >= len(self.animation_boss):
                self.current_frameofboss= 0

        self.image = self.animation_boss[int(self.current_frameofboss)]

#creating a class for the intro animation
class intro_animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__ ()
        self.animation_intro = []
        self.is_animating = False
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro1.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro2.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro3.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro4.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro5.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro6.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro7.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro8.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro9.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro10.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro11.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro12.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro13.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro14.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro15.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro16.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro17.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro18.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro19.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro20.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro21.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro22.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro23.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro24.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro25.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro26.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro27.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro28.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro29.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro30.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro31.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro32.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro33.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro34.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro35.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro36.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro37.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro38.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro39.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro40.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro41.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro42.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro43.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro44.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro45.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro46.png').convert_alpha())
        self.animation_intro.append(pygame.image.load ('pygame/Graphics/intro47.png').convert_alpha())
        self.current_frameofintro = 0
        self.image = self.animation_intro[self.current_frameofintro]

        self.rect = self.image.get_rect(topleft=(0, 0))

    def animate(self):
        self.is_animating = True

    def update(self):
       global main_game
       global intro

       if self.is_animating == True:
        self.current_frameofintro += 0.1

        if self.current_frameofintro >= len(self.animation_intro):
            main_game = True
            intro = False
            self.current_frameofintro = 0
            self.is_animating = False

        self.image = self.animation_intro[int(self.current_frameofintro)]


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
            wave = random.randint(1,5)
            self.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))
            
                
    def draw(self, surface):
        surface.blit(self.image, self.rect)

#a sub classs of enemy with same properties other than the sprite used
class Enemy2(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame/Graphics/projectile2.png').convert_alpha()
        self.rect = self.image.get_rect(center=(random.randint(0, 400), random.randint(0, WINDOW_HEIGHT)))
        

#following along from the code used to create projectiles creating a bonus score for collecting the item
class bonus(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('pygame/Graphics/sushi.jpg')

        self.rect = self.image.get_rect(center = (random.randint(0, 400), random.randint(0, WINDOW_HEIGHT)))


    def draw(self, surface):
        surface.blit(self.image,self.rect)

class flaming_sword(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animation_swing = []
        self.isanimating = False
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame1.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame2.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame3.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame4.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame5.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame6.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame7.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame8.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame9.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame10.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame11.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame12.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame13.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame14.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame15.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame16.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame17.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame18.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame19.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame20.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame21.png').convert_alpha())
        self.animation_swing.append(pygame.image.load ('pygame/Graphics/flame22.png').convert_alpha())
        self.current_frameofsword = 0
        self.image = self.animation_swing[self.current_frameofsword]

        self.rect = self.image.get_rect(center=(random.randint(0, 250), random.randint(0, 200)))


    def animate(self):
        self.isanimating = True

    def update(self):
       global wave

       if self.isanimating == True:
        self.current_frameofsword += 0.15

        if self.current_frameofsword >= len(self.animation_swing):
                self.current_frameofsword = 0
                wave = random.randint(1,5)
                self.rect = self.image.get_rect(center=(random.randint(0, 250), random.randint(0, 200)))


        self.image = self.animation_swing[int(self.current_frameofsword)]
        self.rect = self.image.get_rect(center=self.rect.center)

class laserbeam(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.laser_beam = []
        self.isanimating = False
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser1.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser2.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser3.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser4.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser5.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser6.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser7.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser8.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser9.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser10.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser11.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser12.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser13.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser14.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser15.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser16.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser17.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser18.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser19.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser20.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser21.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser22.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser23.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser24.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser25.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser26.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser27.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser28.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser29.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser30.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser31.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser32.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser33.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser34.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser35.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser36.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser37.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser38.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser39.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser40.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser41.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser42.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser43.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser44.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser45.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser46.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser47.png').convert_alpha())
        self.laser_beam.append(pygame.image.load ('pygame/Graphics/laser48.png').convert_alpha())
        self.current_laser = 0
        self.image = self.laser_beam[self.current_laser]
        self.rect = self.image.get_rect( topleft = (200, 0))


    def animate(self):
        self.isanimating = True

    def update(self):
       global wave

       if self.isanimating == True:
        self.current_laser += 0.1

        if self.current_laser >= len(self.laser_beam):
                self.current_laser= 0
                wave = random.randint(1,5)


        self.image = self.laser_beam[int(self.current_laser)]
        self.rect = self.image.get_rect(topleft=(200, 0))

# establish enemies
E1 = Enemy()
E2 = Enemy2()

#establish the extra point sprite
sushi = bonus()

#Function to display score
def display_score(x, y):
    score_img = font.render(f"{score}", True, (0, 0, 0))
    screen.blit(score_img, (x, y))

#draws the menu aswell as displaying the buttons
def draw_menu():
    #first the menu will check the class backgroundanimation and turn animate to True allowing for the animation to continuesly repeat
    background_anim.animate()
    #this will then display all the frames
    movinganimations.draw(screen) 
    
    screen.blit(titlecard, (10, 20))
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


    #addition of boss animation and movement
    bossanimationgroup.update()
    bossanimationgroup.draw(screen)
    screen.blit(player_surf, player_rect)
     

    #player movement
    P1.movement()

    # randomly generating projectiles
    if wave == 1:
        #by removing the projectiles from the group each time of wave generation means that there are no overlaps
        projectilegroup.empty()
        projectilegroup.add(Enemy2())
        projectilegroup.add(Enemy())

        E1.move()
        E1.draw(screen)
        E2.move()
        E2.draw(screen)
    elif wave == 2:
        projectilegroup.empty()
        projectilegroup.add(Enemy2())
        E2.move()
        E2.draw(screen)    
    elif wave == 3:
        projectilegroup.empty()
        projectilegroup.add(Enemy())
        E1.move()
        E1.draw(screen)
    elif wave == 4:
        projectilegroup.empty()
        projectilegroup.add(sword_animations_start)

        sword_animations_start.animate()
        projectilegroup.update()
        projectilegroup.draw(screen)
    elif wave == 5:
        projectilegroup.empty()
        projectilegroup.add(laser_start)

        laser_start.animate()
        projectilegroup.update()
        projectilegroup.draw(screen)



    #drawing the XP bonuses on the screen 
    sushi.draw(screen)

#function allowing for leaderboard to be displayed    
def draw_leaderboard():
    screen.blit(Leaderboard_menu, (0, 0))

#creating a title to display the leaderboard area
    font = pygame.font.Font("freesansbold.ttf", 20)
    title = font.render("Leaderboard", True, (255, 255, 255))
    screen.blit(title, (180, 20))

#creating a loop that will display the top 5 scores in the scoring board and adjusting the position each time
    count = 1
    position = 20
    for i in scoringboard[:5]:
        stringversion = str(i)
        textofscore = font.render(f"{count}.                            {stringversion}", True, (255,255,255))
        screen.blit(textofscore, (130, 90 + position))
        count += 1
        position += 20

    #add some description of the controls so the player knows how to exit
    font = pygame.font.Font("freesansbold.ttf", 20)
    title = font.render("ESC TO RETURN TO MENU", True, (255, 255, 255))
    screen.blit(title, (120, 250))


#function which implements the death screen and stops the game
def draw_deathscreen():
    screen.blit(blackscreen,(0,0))
    screen.blit(You_lose, (100, 0))
    screen.blit(retry, retry_button_rect)
    screen.blit(menu_button, menu_button_rect)

#creating a function to activate the intro animation
def draw_intro():
    intro_animation_start.animate()
    intro_animation_start.update()
    screen.blit(intro_animation_start.image, intro_animation_start.rect)

#here all the animation groupings are stored

#defining the backround animation and placing it in a group to help with later changes
background_anim = backgroundanimation()
movinganimations.add(background_anim)

#boss animation initialisation and grouping
boss_animationstart = bossanimation()
bossanimationgroup.add(boss_animationstart)

#sword animation grouping
sword_animations_start = flaming_sword()
projectilegroup.add(sword_animations_start)

#laser animation grouping
laser_start = laserbeam()
projectilegroup.add(laser_start)

#grouping of the intro animation
intro_animation_start = intro_animation()


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
    elif intro:
        draw_intro()

    # allows player to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # checking if any of the buttons have been pressed
        if main_menu and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_button_rect.collidepoint(mouse_pos):
                    intro = True
                    main_game = False
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

        #this makes sure to add to the leaderboard system at the end of every game
        if score not in scoringboard:
            scoringboard.append(score)
        
        #makes sure to display with the highest first
        scoringboard.sort(reverse = True)

    #this allows for the functioning of the retry button
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
            wave = random.randint(1,4)


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

    #checking the collision detection between the player and the sword
    if wave == 4 and sword_animations_start.isanimating and player_rect.colliderect(sword_animations_start.rect):
        lives -= 1
        player_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        pygame.time.delay(500)
        sword_animations_start.current_frameofsword = 50
        projectilegroup.empty()#resets all projectiles on the screen
        sword_animations_start.image.get_rect(center=(random.randint(0, 250), random.randint(0, 200)))
        sushi.rect.center = (random.randint(0, 400), random.randint(0, WINDOW_HEIGHT))

    #if wave == 4:
        #pygame.draw.rect(screen, (255, 0, 0), sword_animations_start.rect, 1)
 

    #checking the collision detection between the player and the laser
    if wave == 5 and laser_start.isanimating and player_rect.colliderect(laser_start.rect):
        lives -= 1
        player_rect.center = (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 2)
        pygame.time.delay(500)
        projectilegroup.empty()#resets all projectiles on the screen
        sword_animations_start.image.get_rect(center=(random.randint(0, 250), random.randint(0, 200)))
        sushi.rect.center = (random.randint(0, 400), random.randint(0, WINDOW_HEIGHT))

    #if wave == 5:
        #pygame.draw.rect(screen, (255, 0, 0), laser_start.rect, 1)
 
    #here we are coding the collisions betwen the player and projectiles
    if player_rect.colliderect(E1.rect) or player_rect.colliderect(E2.rect):
        lives = lives - 1
        player_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        pygame.time.delay(500)  # pause after losing a life
        E1.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))
        E2.rect.center = (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))
        sushi.rect.center = (random.randint(0, 400), random.randint(0, WINDOW_HEIGHT)) #to make sure the sushi moves aswell

    #creating an instance where if the player collects the sushi they gain ten points
    if player_rect.colliderect(sushi.rect):
        score += 10
        sushi.rect.center = (random.randint(0, 400), random.randint(0, WINDOW_HEIGHT))

    # Updates score every second
    if pygame.time.get_ticks() - score_update_time >= 1000 and main_game == True:
        score += 1
        score_update_time = pygame.time.get_ticks()
    
    #displaying the score in the game
    display_score(fontX, fontY)

    #this will continuesly loop over and over switching the frames each time
    movinganimations.update()

    #this starts the initial animation of the boss
    boss_animationstart.animate()

    projectilegroup.update()

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

#scoring system implementation(done)

#animation (done)

#new projectile (done)

#intro animation (done)
