import pygame
import random

pygame.init()

screenX = 1066
screenY = 600
screen = pygame.display.set_mode((screenX , screenY))

pygame.display.set_caption("Space Invansion")
icon = pygame.image.load('Player.png')
pygame.display.set_icon(icon)

background = pygame.image.load('Background.jpg')

playerImg = pygame.image.load('Player.png')
playerX = 20
playerY = 268
D_playerV = 2
playerV = 0

enemyImg = pygame.image.load('Enemy.png')
no_of_enemies = 8
enemyX = [screenX + random.randint(100, 600) for i in range (no_of_enemies)]
enemyY = [random.randint(10,screenY - 74) for i in range (no_of_enemies)]
enemy_VX = 2
D_VY = 100
enemy_VY = [random.randint(-D_VY, D_VY)/100 for i in range (no_of_enemies)]

bulletImg = pygame.image.load('bullet.png')
no_of_bullets = 0
bulletX = []
bulletY = []
bullet_VX = 6

d_hearts = 3
hearts = d_hearts
heartImg = pygame.image.load('heart.png')

score = 0
font = pygame.font.Font('freesansbold.ttf', 48)

over_font = pygame.font.Font('freesansbold.ttf', 128)

def collision_detection(a, b, c, d):
    if d > b - 16 and d < b + 48:
        if c > a - 24 and c < a + 48:
            return True
    return False

Running = True
while Running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerV = -D_playerV
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerV = D_playerV
            if event.key == pygame.K_SPACE:
                no_of_bullets += 2
                bulletX.append(playerX + 8)
                bulletY.append(playerY - 2)
                bulletX.append(playerX + 8)
                bulletY.append(playerY + 34)
            if event.key == pygame.K_RETURN:
                score = 0
                hearts = d_hearts
                playerY = 268
                enemyX = [screenX + random.randint(100, 600) for i in range (no_of_enemies)]
                enemyY = [random.randint(10,screenY - 74) for i in range (no_of_enemies)]
                enemy_VY = [random.randint(-D_VY, D_VY)/100 for i in range (no_of_enemies)]
                no_of_bullets = 0
                bulletX.clear()
                bulletY.clear()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerV = 0
        





    if hearts > 0:
        for i in range (no_of_enemies):
            for j in range (no_of_bullets):
                if collision_detection(enemyX[i],enemyY[i],bulletX[j],bulletY[j]):
                    del bulletX[j]
                    del bulletY[j]
                    no_of_bullets -= 1
                    enemyX[i] = screenX + random.randint(100, 600)
                    enemyY[i] = random.randint(10,screenY - 74)
                    enemy_VY[i]  = random.randint(-D_VY, D_VY)/100
                    score += 1
                    break
            enemyX[i] -= enemy_VX
            enemyY[i] += enemy_VY[i]
            if enemyY[i] <= 0 or enemyY[i] >= screenY - 64:
                enemy_VY[i] *= -1
            
            
            if enemyX [i] < 0:
                hearts -= 1
                enemyX[i] = screenX + random.randint(100, 600)
                enemyY[i] = random.randint(10,screenY - 74)
                enemy_VY[i] = random.randint(-D_VY, D_VY)/100
        
        if no_of_bullets > 0 and bulletX[0] > screenX:
            no_of_bullets -= 1
            del bulletX[0]
            del bulletY[0]
        for i in range (no_of_bullets):
            bulletX[i] += bullet_VX

        playerY += playerV
        if playerY <= 0:
            playerY = 0
        elif playerY >= screenY - 64:
            playerY = screenY - 64

    for i in range (no_of_bullets):
        screen.blit(bulletImg, (bulletX[i], bulletY[i]))

    
    for i in range(no_of_enemies):
        screen.blit(enemyImg, (enemyX[i], enemyY[i]))

    screen.blit(playerImg, (playerX, playerY))

    if hearts <= 0:
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, ((screenX/2)-384, (screenY/2)-64))

    score_text = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10,10))

    


    for h in range(hearts):
        screen.blit(heartImg, (screenX + 40* (h - 3), 10))

    

    pygame.display.update()
