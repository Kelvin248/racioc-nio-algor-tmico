import pygame
from functions import *


pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("PUC Fight")

#importando sprites
IDLE = pygame.image.load('sprites/Fighter/Idle.png').convert_alpha()

FIGHTER_SIZE = 128
FIGHTER_SCALE = 2.3
FIGHTER_OFFSET = [44,50]
FIGHER_DATA = [FIGHTER_SIZE, FIGHTER_SCALE, FIGHTER_OFFSET]
#Animação = [n° frames/linha]
ANIMATION_IDLE = [6, 4]


#criando os jogadores
player_1 = character(100,5,40,400, 180, FIGHER_DATA, IDLE,ANIMATION_IDLE, screen)
player_2 = character(100,5,680,400, 180, FIGHER_DATA, IDLE, ANIMATION_IDLE, screen)

#barra de vida dos personagens

def draw_life_bar(life, x, y):
    ratio = life / 100
    pygame.draw.rect(screen, 'black',(x -2,y -2 , 253,24))
    pygame.draw.rect(screen, 'white',(x,y, 250,20))
    pygame.draw.rect(screen, 'red',(x,y, 250*ratio,20))


def enemy_draw_life_bar(life, x, y):
    ratio = life / 100
    pygame.draw.rect(screen, 'black',(x -2,y -2 , 253,24))
    pygame.draw.rect(screen, 'white',(x,y, 250,20))
    pygame.draw.rect(screen, 'red',(x+(250-(250*ratio)),y, 250*ratio,20))









Clock = pygame.time.Clock()
running =True
while running == True:
    screen.fill('gray')


    #adicionando movimento e limite na tela
    player_1.move(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_k, pygame.K_l, player_2)
    player_2.move(pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT, pygame.K_1,pygame.K_2,player_1)


    #atualizando sprite
    player_1.update_sprites()
    player_2.update_sprites()

    #desenhando os jogadores na tela
    player_1.draw('red')
    player_2.draw('blue')

    #desenhando a vida do jogador
    draw_life_bar(player_1.life,20,20)
    enemy_draw_life_bar(player_2.life,530,20)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Clock.tick(60)
    pygame.display.update()

pygame.quit()
