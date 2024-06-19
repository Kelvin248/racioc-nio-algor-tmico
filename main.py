import pygame
import time
from functions import *
from personagem_functions import *
from mapas_functions import *
import sys

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("JOGO BÃO")

GRAY = (200, 200, 200)

# Fonte da letra
font2 = pygame.font.Font("font/ARCADECLASSIC.TTF", 90)
font_p = pygame.font.Font("font/ARCADECLASSIC.TTF", 30)
font_p_mapas = pygame.font.Font("font/ARCADECLASSIC.TTF", 17)
fontmenu = pygame.font.Font("font/ARCADECLASSIC.TTF", 50)
font2menu = pygame.font.Font("font/ARCADECLASSIC.TTF", 100)


pygame.mixer.init()

def musica1():
    pygame.mixer.music.load('sound/TheSynthWars.mp3')
    
    return pygame.mixer.music.play(-1)

musica1()

# Carregando a foto
personagem_adryan = pygame.image.load('img/adryan.jpg').convert_alpha()
personagem_gustavo = pygame.image.load('img/gustavo.png').convert_alpha()
personagem_kelvin = pygame.image.load('img/kelvin.jpg').convert_alpha()
personagem_caio = pygame.image.load('img/zeca.jpeg').convert_alpha()

bibliotecaI = pygame.image.load('mapas/bibliotecaI.jpg').convert_alpha()
bibliotecaII = pygame.image.load('mapas/bibliotecaII.jpg').convert_alpha()
blocolaranja = pygame.image.load('mapas/bloco laranja.jpg').convert_alpha()
complexoesportivo = pygame.image.load('mapas/complexo esportivo.jpg').convert_alpha()
frentebiblioteca = pygame.image.load('mapas/frente biblioteca.jpg').convert_alpha()
blocoverde = pygame.image.load('mapas/interior bloco verde.jpg').convert_alpha()
museu = pygame.image.load('mapas/museu universitario.jpg').convert_alpha()
aleatorio = pygame.image.load('mapas/aleatorio.jpg')


# Lista dos personagens
personagens = [personagem_adryan, personagem_gustavo, personagem_kelvin, personagem_caio]
mapas = [bibliotecaI, bibliotecaII, blocolaranja, complexoesportivo, frentebiblioteca, blocoverde, museu, aleatorio]





# Calculando a coordenada x
espacamento_horizontal = 30
total_largura_botoes = botao_largura * len(personagens) + espacamento_horizontal * (len(personagens) - 1)
x_inicial = (largura - total_largura_botoes) // 2

# Calculando a coordenada x para mapas
espacamento_horizontal_mapas = 20
espacamento_vertical_mapas = 10
total_largura_botoes_mapas = botao_largura_mapas * len(mapas) + espacamento_horizontal_mapas * (len(mapas) - 1)
x_inicial_mapas = (largura - total_largura_botoes_mapas) // 2
# Calculando a coordenada x inicial dos mapas
x_inicial_mapas = 50
# Definindo a posição y inicial para as duas linhas de mapas
y_botoes_primeira_linha = 210
y_botoes_segunda_linha = 330



# Criando botões personagem
botoes = []
x = x_inicial
for i, personagem in enumerate(personagens):
    personagem_redimensionada = pygame.transform.scale(personagem, (botao_largura, botao_altura))
    botao = Button_personagens(x, 250, personagem_redimensionada, tela)
    botoes.append(botao)
    x += botao_largura + espacamento_horizontal

# Criando botões mapa

botoes_mapa = []
for i, mapa in enumerate(mapas):
    personagem_redimensionada = pygame.transform.scale(mapa, (botao_largura_mapas, botao_altura_mapas))
    if i < 4:
        x = x_inicial_mapas + i * (botao_largura_mapas + espacamento_horizontal_mapas)
        y = y_botoes_primeira_linha + espacamento_vertical_mapas
    else:
        x = x_inicial_mapas + (i - 4) * (botao_largura_mapas + espacamento_horizontal_mapas)
        y = y_botoes_segunda_linha + espacamento_vertical_mapas
        y += espacamento_vertical_mapas
    nome_mapas = ["Biblioteca I", "Biblioteca II", "Bloco Laranja", "Complexo Esportivo", "Frente Biblioteca", "Bloco Verde", "Museu", "Aleatorio"]
    botao2 = Button_mapas(x, y, personagem_redimensionada, nome_mapas[i], tela, font_p_mapas)
    botoes_mapa.append(botao2)


def quit_game():
    pygame.quit()
    sys.exit()

def start_game():
    return False
def show_score():
    print("Mostrando pontuações...")
    # Aqui você pode adicionar a lógica para mostrar as pontuações



def button(text, x, y, width, height, raio, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    button_clicked = False

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(tela, active_color, (x + raio, y, width - 2 * raio, height))
        pygame.draw.rect(tela, active_color, (x, y + raio, width, height - 2 * raio))
        pygame.draw.circle(tela, active_color, (x + raio, y + raio), raio)
        pygame.draw.circle(tela, active_color, (x + width - raio, y + raio), raio)
        pygame.draw.circle(tela, active_color, (x + raio, y + height - raio), raio)
        pygame.draw.circle(tela, active_color, (x + width - raio, y + height - raio), raio)
        if click[0] == 1 and action:
            action()
            button_clicked = True
    else:
        pygame.draw.rect(tela, inactive_color, (x + raio, y, width - 2 * raio, height))
        pygame.draw.rect(tela, inactive_color, (x, y + raio, width, height - 2 * raio))
        pygame.draw.circle(tela, inactive_color, (x + raio, y + raio), raio)
        pygame.draw.circle(tela, inactive_color, (x + width - raio, y + raio), raio)
        pygame.draw.circle(tela, inactive_color, (x + raio, y + height - raio), raio)
        pygame.draw.circle(tela, inactive_color, (x + width - raio, y + height - raio), raio)
    
    draw_text(text, fontmenu, GRAY, x + width / 2, y + height / 2, tela)
    return button_clicked
def main(start):
    # Carregue a imagem de fundo
    background_image = pygame.image.load("img/puc.jpg").convert()
    background_image = pygame.transform.scale(background_image, (largura, altura))
    
    # Desenhe a imagem de fundo na tela
    tela.blit(background_image, (0, 0))
    draw_text("PUC   FIGHT", font2menu, BLACK, largura // 2, 104, tela)
    draw_text("PUC   FIGHT", font2menu, VERMELHO, largura // 2, 100, tela)
    
    # Desenhe os botões e capture as ações
    start_clicked = button("START", 250, 200, 300, 70, 25, VERMELHO, BLACK, start_game)
    score_clicked = button("SCORE", 250, 300, 300, 70, 25, VERMELHO, BLACK, show_score)
    sair_clicked = button("SAIR", 250, 400, 300, 70, 25, VERMELHO, BLACK, quit_game)
    
    if start_clicked:
        start = False
        return start










selected_index_p2 = 3
selected_index_p1 = 0
counter = 0
start = True
variavel = 0
Clock = pygame.time.Clock()
while start:
    if variavel == 0:
        start_menu = True
        def main_menu():
            start_menu = True
            while start_menu:
                start_menu = main(start_menu)
                if start_menu == False:
                    return 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:

                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            start_menu = False
                            pygame.quit()
                            sys.exit()
                pygame.display.update()
        main_menu()
        if main_menu() == 1:
            variavel = 1



    if variavel == 1:
        # Iniciando o mixer de som
        pygame.mixer.init()

        som_selecao = pygame.mixer.Sound("sound/selecaosound.mp3")
        selecionado = pygame.mixer.Sound('sound/selecionado.mp3')


        background_imagem = pygame.image.load('img/background.jpg').convert()
        background_imagem = pygame.transform.scale(background_imagem, (largura, altura))

        start_personagem = True
        while start_personagem:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
                elif event.type == pygame.KEYDOWN:
                    # Teclas de jogador 1 (P1)
                    if event.key == pygame.K_a:
                        selected_index_p1 = (selected_index_p1 - 1) % len(botoes)
                        som_selecao.play()
                    elif event.key == pygame.K_d:
                        selected_index_p1 = (selected_index_p1 + 1) % len(botoes)
                        som_selecao.play()
                    # Teclas de jogador 2 (P2)
                    elif event.key == pygame.K_LEFT:
                        selected_index_p2 = (selected_index_p2 - 1) % len(botoes)
                        som_selecao.play()
                    elif event.key == pygame.K_RIGHT:
                        selected_index_p2 = (selected_index_p2 + 1) % len(botoes)
                        som_selecao.play()
                    elif event.key == pygame.K_RETURN:
                        selecionado.play()
                        print("P1 selecionou:", selected_index_p1)
                        print("P2 selecionou:", selected_index_p2)
                        time.sleep(1)
                        variavel = 2
                        start_personagem = False
                    elif event.key == pygame.K_ESCAPE:
                        variavel = 0
                        start_personagem = False
            
            tela.blit(background_imagem, (0, 0))
            draw_text("SELECIONE", font2, BLACK, largura // 2 + 4, 100, tela)
            draw_text("SELECIONE", font2, VERMELHO, largura // 2, 103, tela)
            
            for i, botao in enumerate(botoes):
                botao.draw(i == selected_index_p1, i == selected_index_p2)
            
            pygame.display.update()
    
    
    if variavel == 2:
        # Iniciando o mixer de som
        pygame.mixer.init()

        som_selecao = pygame.mixer.Sound("sound/selecaosound.mp3")
        selecionado = pygame.mixer.Sound('sound/selecionado.mp3')


        selected_index = 0

        start_mapa = True
        while start_mapa:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # Teclas de jogador 1 (P1)
                    if event.key == pygame.K_a:
                        selected_index = (selected_index - 1) % len(botoes_mapa)
                        som_selecao.play()
                    elif event.key == pygame.K_d:
                        selected_index = (selected_index + 1) % len(botoes_mapa)
                        som_selecao.play()
                    elif event.key == pygame.K_w:
                        selected_index = (selected_index - 4) % len(botoes_mapa)
                        som_selecao.play()
                    elif event.key == pygame.K_s:
                        selected_index = (selected_index + 4) % len(botoes_mapa)
                        som_selecao.play()
                    elif event.key == pygame.K_RETURN:
                        print("Mapa selecionado:", selected_index)
                        selecionado.play()
                        time.sleep(.5)
                        pygame.mixer.stop()
                        variavel = 3
                        start_mapa = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.mixer.stop()
                        time.sleep(0.5)
                        variavel = 1
                        start_mapa = False
            tela.blit(background_imagem, (0, 0))
            draw_text("SELECIONE", font2, BLACK, largura // 2 + 4, 100, tela)
            draw_text("SELECIONE", font2, VERMELHO, largura // 2, 103,tela)
            for i, botao2 in enumerate(botoes_mapa):
                botao2.draw2(i == selected_index)
            pygame.display.update()


    if variavel == 3:

        IDLE = pygame.image.load('sprites/Fighter/Idle.png').convert_alpha()

        FIGHTER_SIZE = 128
        FIGHTER_SCALE = 2.3
        FIGHTER_OFFSET = [44,50]
        FIGHER_DATA = [FIGHTER_SIZE, FIGHTER_SCALE, FIGHTER_OFFSET]
        #Animação = [n° frames/linha]
        ANIMATION_IDLE = [6,4,10,4,3,8,3,2,3]

        def draw_life_bar(life, x, y):
            ratio = life / 100
            pygame.draw.rect(tela, 'black',(x -2,y -2 , 253,24))
            pygame.draw.rect(tela, 'white',(x,y, 250,20))
            pygame.draw.rect(tela, 'red',(x,y, 250*ratio,20))


        def enemy_draw_life_bar(life, x, y):
            ratio = life / 100
            pygame.draw.rect(tela, 'black',(x -2,y -2 , 253,24))
            pygame.draw.rect(tela, 'white',(x,y, 250,20))
            pygame.draw.rect(tela, 'red',(x+(250-(250*ratio)),y, 250*ratio,20))



        player_1 = character(100,5,40,400, 180, FIGHER_DATA, IDLE,ANIMATION_IDLE, tela)
        player_2 = character(100,5,680,400, 180, FIGHER_DATA, IDLE, ANIMATION_IDLE, tela)


        pygame.mixer.music.stop()
        start_jogo = True
        while counter<=3 and start_jogo:

            tela.fill('gray')

            #adicionando movimento e limite na tela
            player_1.move(pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_k, pygame.K_l,pygame.K_j, player_2)
            player_2.move(pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT, pygame.K_1,pygame.K_2,pygame.K_3,player_1)


            #atualizando sprite
            player_1.update_sprites()
            player_2.update_sprites()

            #desenhando os jogadores na tela
            player_1.draw('red')
            player_2.draw('blue')

            #desenhando a vida do jogador
            draw_life_bar(player_1.life,20,20)
            enemy_draw_life_bar(player_2.life,530,20)

            if player_1.life <= 0:
                counter += 1
                start_jogo = False
                variavel = 3
            if player_2.life <=0:
                counter += 1
                start_jogo = False
                variavel = 3
            if counter == 3:
                start_jogo = False
                variavel = 2
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_jogo = False
                    start = False
                elif event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        start_jogo = False
                        start = False
                        variavel = 2

            Clock.tick(60)
            pygame.display.update()
