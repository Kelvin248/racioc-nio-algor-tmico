import pygame
from functions import *


pygame.init()

screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("PUC Fight")

#importando sprites
#idle = pygame.image.load('Knight_1/Idle.png').convert_alpha()
#attack1 = pygame.image.load('Knight_1/Attack 1.png').convert_alpha()

#background = pygame.image.load('backgrounds/sky bridge.png')

#Animação = [n° frames,]
ANIMATION_IDLE = [4,]


#criando os jogadores
player_1 = character(100,screen,7,300,400)
player_2 = character(100,screen,7,500,400)



#barra de vida dos personagens

def draw_life_bar(life, x, y):
    ratio = life / 100
    pygame.draw.rect(screen, 'black',(x -2,y -2 , 403,34))
    pygame.draw.rect(screen, 'white',(x,y, 400,30))
    pygame.draw.rect(screen, 'red',(x,y, 400*ratio,30))


def enemy_draw_life_bar(life, x, y):
    ratio = life / 100
    pygame.draw.rect(screen, 'black',(x -2,y -2 , 403,34))
    pygame.draw.rect(screen, 'white',(x,y, 400,30))
    pygame.draw.rect(screen, 'red',(x+(400-(400*ratio)),y, 400*ratio,30))


Clock = pygame.time.Clock()
running =True
while running == True:
    screen.fill('gray')


    #adicionando movimento e limite na tela
    player_1.move(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_k, pygame.K_l, player_2)
    player_2.move(pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT, pygame.K_1,pygame.K_2,player_1)

    #desenhando os jogadores na tela
    player_1.draw('red')
    player_2.draw('blue')

    #desenhando a vida do jogador
    draw_life_bar(player_1.life,20,20)
    enemy_draw_life_bar(player_2.life,780,20)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Clock.tick(60)
    pygame.display.update()

pygame.quit()
