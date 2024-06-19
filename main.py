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
font4 = pygame.font.Font("font/ARCADECLASSIC.TTF", 36)


background_imagem = pygame.image.load('img/background.jpg').convert()
background_imagem = pygame.transform.scale(background_imagem, (largura, altura))


pygame.mixer.init()

def musica1():
    pygame.mixer.music.load('sound/TheSynthWars.mp3')
    
    return pygame.mixer.music.play(-1)

def musica2():
    pygame.mixer.music.load('sound/musica do combate.mp3')

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
Casa_estrela = pygame.image.load('mapas/Casa estrela.jpg').convert_alpha()

sprite_adryan = pygame.image.load('sprites/sprites_a.png').convert_alpha()
sprite_caio = pygame.image.load('sprites/sprites_c.png').convert_alpha()
sprite_gustavo = pygame.image.load('sprites/sprites_g.png').convert_alpha()
sprite_kelvin = pygame.image.load('sprites/sprites_k.png').convert_alpha()

sprite_personagens = [sprite_adryan,sprite_gustavo, sprite_kelvin, sprite_caio]

matriz_sprite = [[6,8,4,4,3,6,3,3,3,2], [6,8,4,3,3,7,3,3,3,3], [6,8,4,4,3,6,3,3,3,2], [6,8,4,3,3,6,3,3,3,3]]
nomes = ["Adryan","Gustavo","Kelvin","Caio"]


# Lista dos personagens
personagens = [personagem_adryan, personagem_gustavo, personagem_kelvin, personagem_caio]
mapas = [bibliotecaI, bibliotecaII, blocolaranja, complexoesportivo, frentebiblioteca, blocoverde, museu, Casa_estrela]





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
    nome_mapas = ["Biblioteca I", "Biblioteca II", "Bloco Laranja", "Complexo Esportivo", "Frente Biblioteca", "Bloco Verde", "Museu", "Casa estrela"]
    botao2 = Button_mapas(x, y, personagem_redimensionada, nome_mapas[i], tela, font_p_mapas)
    botoes_mapa.append(botao2)


def quit_game():
    pygame.quit()
    sys.exit()

def start_game():
    return False
def show_score():
    return None



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
    if score_clicked:
        score = "Score"
        return score







personagem_1 = None
personagem_2 = None
lista = None
lista_1 = None
selected_index_p2 = 3
selected_index_p1 = 0
counter = 0
counterp1 = 0
counterp2 = 0
start = True
variavel = 0
vencedor = None

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
                if start_menu == "Score":
                    return 2
                #elif show_score
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
        if main_menu() == 2:
            variavel = 4



    if variavel == 1:
        # Iniciando o mixer de som
        pygame.mixer.init()

        som_selecao = pygame.mixer.Sound("sound/selecaosound.mp3")
        selecionado = pygame.mixer.Sound('sound/selecionado.mp3')


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
                        personagem_1 = sprite_personagens[selected_index_p1]
                        personagem_2 = sprite_personagens[selected_index_p2]
                        lista = matriz_sprite[selected_index_p1]
                        lista_1 = matriz_sprite[selected_index_p2]

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
                        musica2()
                        variavel = 3
                        start_mapa = False
                    elif event.key == pygame.K_ESCAPE:

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

        SPRITE1 = personagem_1
        SPRITE2 = personagem_2

        FIGHTER_SIZE = 128
        FIGHTER_SCALE = 3
        FIGHTER_OFFSET = [46,50]
        FIGHER_DATA = [FIGHTER_SIZE, FIGHTER_SCALE, FIGHTER_OFFSET]

        
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



        player_1 = character(100,5,40,370, 180, FIGHER_DATA, SPRITE1,lista, tela)
        player_2 = character(100,5,680,370, 180, FIGHER_DATA, SPRITE2, lista_1, tela)


        round()
        start_jogo = True
        while counter<=3 and start_jogo:

            fight_scene = pygame.transform.scale(mapas[selected_index], (largura, altura))
            tela.blit(fight_scene, (0,0))

            
            #adicionando movimento e limite na tela
            player_1.move(pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_k, pygame.K_l,pygame.K_j, player_2)
            player_2.move(pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT, pygame.K_1,pygame.K_2,pygame.K_3,player_1)


            #atualizando sprite
            player_1.update_sprites()
            player_2.update_sprites()

            #desenhando os jogadores na tela
            player_1.draw()
            player_2.draw()

            #desenhando a vida do jogador
            draw_life_bar(player_1.life,20,20)
            enemy_draw_life_bar(player_2.life,530,20)


            
            if player_1.image == player_1.animation_list[7][-1] and player_2.image == player_2.animation_list[8][-1]:
                pygame.display.update()
                time.sleep(1)
                counterp2 += 1
                counter += counterp2
                start_jogo = False
                if counterp2 == 2:
                    variavel = 4
                    counterp2 = 0
                    counter = 0
                    vencedor = nomes[selected_index_p2]
            if player_2.image == player_2.animation_list[7][-1] and player_1.image == player_1.animation_list[8][-1]:
                pygame.display.update()
                time.sleep(1)
                counterp1 += 1
                counter += counterp1
                start_jogo = False
                

                if counterp1 == 2:
                    variavel = 4
                    counterp1 = 0
                    counter = 0
                    vencedor = nomes[selected_index_p1]

            if counter == 3:
                start_jogo = False
                variavel = 4
                if counterp1 > counterp2:
                    vencedor = nomes[selected_index_p1]
                else:
                    vencedor = nomes[selected_index_p2]
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        start_jogo = False
                        variavel = 0

            Clock.tick(60)
            pygame.display.update()

    if variavel == 4:
        # Tamanho dos blocos
        block_width = 300
        block_height = 100

        back = pygame.image.load("img/background.jpg")
        back = pygame.transform.scale(back, (largura, altura))

        # Função para desenhar um bloco
        def draw_block(tela, name, x, y):
            block_rect = pygame.Rect(x, y, block_width, block_height)
            
            # Desenha a borda preta
            pygame.draw.rect(tela, BLACK, block_rect)
            
            # Desenha o preenchimento branco
            inner_rect = pygame.Rect(x + 2, y + 2, block_width - 4, block_height - 4)
            pygame.draw.rect(tela, WHITE, inner_rect)
            
            # Desenha o texto
            text = font4.render(name[0], True, BLACK)
            text_rect = text.get_rect(center=block_rect.center)
            tela.blit(text, text_rect)


        #lê o arquivo txt-----------------------------------------------------------
        with open("pontuacao_personagens.txt", 'r') as arquivo:
            pontuacao = arquivo.readlines()

        #Adiciona 1 ponto
        for i, linha in enumerate(pontuacao):
            nome, pontos = linha.strip().split(',')
            if nome == vencedor:
                pontos = int(pontos) + 1 
                pontuacao[i] = f"{nome},{pontos}\n"
                break

        #Faz uma matriz desorganizada
        lista_desatualizada = []
        for i, linha in enumerate(pontuacao):
            nome, pontos = linha.strip().split(',')
            lista_desatualizada.append([])
            lista_desatualizada[i].append(nome)
            lista_desatualizada[i].append(int(pontos))
        print(lista_desatualizada)


        #Organiza a matriz conforme a segunda coluna de cada linha
        lista_atualizada = sorted(lista_desatualizada, key=lambda x: x[1], reverse=True)
        print(lista_atualizada)

        #Escreve no arquivo txt
        with open('pontuacao_personagens.txt', 'w') as arquivo:
            arquivo.writelines(pontuacao)
        arquivo.close()
        ranking = []
        cont = 0
        for i in lista_atualizada:
            ranking.append([])
            ranking[cont].append(f"{cont + 1}°  {lista_atualizada[cont][0]} ({lista_atualizada[cont][1]})")
            cont += 1

        # Função principal
        def main2():
            clock = pygame.time.Clock()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return 0                       

                # Desenha o fundo

                tela.blit(back, (0, 0))

                # Calcula a posição dos blocos
                for i, name in enumerate(ranking):
                    x = (largura - block_width) / 2
                    y = (altura - block_height * 4) / 2 + i * (block_height + 10)
                    draw_block(tela, name, x, y)

                pygame.display.flip()
                clock.tick(60)
        if __name__ == '__main__':
            main2()
            if main2() == 0:
                variavel = 0
                pygame.mixer.music.stop()
                musica1()
