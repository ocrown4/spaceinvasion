import pygame
import random
import math

#initialize pygame

pygame.init()

#Create game screen
screen = pygame.display.set_mode((800,600))

#set icon and title
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ovni.png")
pygame.display.set_icon(icon)
background= pygame.image.load("background.jpg")

#set player variables
img_player=pygame.image.load("nave-espacial.png")
player_x= 368#400(mitad) -32
player_y= 536
player_x_change= 0

#enemy variables
img_enemy= []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 5

for i in range(number_of_enemies):
    img_enemy.append(pygame.image.load("abduction.png"))
    enemy_x.append(random.randint (0,736))
    enemy_y.append(random.randint (30,200))
    enemy_x_change.append(.9)
    enemy_y_change.append(30)

# Score variables
score = 0
score_font = pygame.font.Font("freesansbold.ttf",32)
score_text_x = 10
score_text_y = 10

# End game
end_font = pygame.font.Font("freesansbold.ttf",32)

# End message
def final_message():
    final_text = end_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(final_text, (200, 200))


#bullet variables
img_bullet=pygame.image.load("bala.png")
bullet_x = 0
bullet_y = 536
bullet_x_change = 0
bullet_y_change = 2.3
bullet_visible = False

#show player in screen
def player(x,y):
    screen.blit(img_player,(x, y))
#show enemy
def enemy (x, y, enemy_index):
    screen.blit(img_enemy[enemy_index], (x, y))

#Shoot bullet


def shoot_bullet(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(img_bullet, (x + 16, y + 10))



def detect_collision(x_1, y_1, x_2, y_2):
    x_sub = x_2 - x_1
    y_sub = y_2 - y_1
    distance = math.sqrt(math.pow(x_sub,2) + math.pow(y_sub,2))
    if distance < 27:
        return True
    else:
        return False


#Game loop
is_running= True
while is_running:
    screen.blit(background,(0,0) )

    #player_x += 0.1
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            is_running=False
        if event.type == pygame.KEYDOWN:
            #print("A key was press")
            if event.key == pygame.K_LEFT:
                #print("Left arrow pressed")
                player_x_change -= 1.2
            if event.key == pygame.K_RIGHT:
                #print("Right arrow pressed")
                player_x_change += 1.2
            if event.key == pygame.K_SPACE:
                if not bullet_visible:
                    bullet_x = player_x
                    shoot_bullet(player_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print("A key was release")
                player_x_change = 0

    #update player location
    player_x += player_x_change

    # keep player inside the screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    for i in range(number_of_enemies):
        #update enemy location
        enemy_x[i] += enemy_x_change[i]

        #keep the enemy inside the screen
        if enemy_x[i] <= 0:
            enemy_x_change[i] += 0.9
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] -=0.9
            enemy_y[i] += enemy_y_change[i]

        # Detect collision
        collision = detect_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(30, 200)
            bullet_visible = False
            score += 1
            bullet_y = 500
            print(score)
        # show enemy
        enemy(enemy_x[i], enemy_y[i], i)

    # Shoot bullet
    if bullet_y <= -64:
        bullet_y = 500
        bullet_visible = False
    if bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # show player
    player(player_x, player_y)

    #update screen
    pygame.display.update()
    player(player_x,player_y)

    #update screen
    pygame.display.update()