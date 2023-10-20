#https://www.youtube.com/watch?v=waY3LfJhQLY&t=1381s
import pygame
import time
import random
pygame.font.init()
WIDTH,HEIGHT = 1000,800
TELA = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Star Dodge")
BG = pygame.image.load("bg.jpeg")
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 1.618
PROJECTILE_WIDTH = 10
PROJECTILE_HEIGHT = 20
PROJECTILE_VEL = 2.6
FONT = pygame.font.SysFont("Comicsans",30)
bestTime = 0
def draw(player,elapsedTime,projectiles,bestTime):
    TELA.blit(BG,(0,0))
    timeText = FONT.render("Time: "+str(round(elapsedTime))+"s",1,"yellow")
    bestTimeText = FONT.render("Best time: "+str(round(bestTime))+"s",1,"yellow")
    TELA.blit(bestTimeText,(800,5))
    TELA.blit(timeText,(10,10))
    pygame.draw.rect(TELA,"red",player)
    for projectile in projectiles:
        pygame.draw.rect(TELA,"white",projectile)
    pygame.display.update()
def main(bestTime):
    run = True
    player = pygame.Rect(200,HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0
    projectile_add_increment = 2000
    projectile_count = 0
    projectiles = []
    hit = False
    while run:
        projectile_count += clock.tick(150)
        elapsedTime = time.time() - startTime
        if projectile_count > projectile_add_increment:
            for i in range(random.randint(1,7)):
                proj_x = random.randint(0,WIDTH - PROJECTILE_WIDTH)
                proj = pygame.Rect(proj_x,-PROJECTILE_HEIGHT,PROJECTILE_WIDTH,PROJECTILE_HEIGHT)
                projectiles.append(proj)
            projectile_add_increment = max(420, projectile_add_increment - 30)
            projectile_count = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if key[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        for projectile in projectiles[:]:
            projectile.y += PROJECTILE_VEL
            if projectile.y > HEIGHT:
                projectiles.remove(projectile)
            elif projectile.y + projectile.height >= player.y and projectile.colliderect(player):
                projectiles.remove(projectile)
                hit = True
                break
        if hit == True:
            game_over = FONT.render("VOCÊ FOI DE ARRASTA PRA CIMA! GAME OVER!",1,"purple")
            TELA.blit(game_over,(WIDTH/2 - game_over.get_width()/2,HEIGHT/2 - game_over.get_height()/2))
            if elapsedTime >= bestTime:
                bestTime = elapsedTime
            pygame.display.update()
            pygame.time.delay(2000)
            break
        draw(player,elapsedTime,projectiles,bestTime)

    main(bestTime)
if __name__ == "__main__":
    main(bestTime)
