import pygame
import time
import random
WIDTH,HEIGHT = 1000,800
TELA = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Star Dodge")
BG = pygame.image.load("bg.jpeg")
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 1.618
def draw(player):
    TELA.blit(BG,(0,0))
    pygame.draw.rect(TELA,"red",player)
    pygame.display.update()
clock = pygame.time.Clock()
def main():
    clock.tick(60)
    run = True
    player = pygame.Rect(200,HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if key[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        draw(player)

    pygame.quit()
if __name__ == "__main__":
    main()
