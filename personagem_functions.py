import pygame

pygame.init()

# Fonte da letra
font2 = pygame.font.Font("font/ARCADECLASSIC.TTF", 90)
font_p = pygame.font.Font("font/ARCADECLASSIC.TTF", 30)
font_p_mapas = pygame.font.Font("font/ARCADECLASSIC.TTF", 17)


# Defina as CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERMELHO = (108, 34, 34)
AZUL = (0, 0, 255)


# Largura e altura dos botões
botao_largura, botao_altura = 120, 120
botao_largura_mapas, botao_altura_mapas = 160, 110



# Classe botão P1 e P2
class Button_personagens():
    def __init__(self, x, y, imagem, Tela):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.hovered_p1 = False
        self.hovered_p2 = False
        self.tela = Tela

    def draw(self, selected_p1, selected_p2):
        if selected_p1 and selected_p2:
            half_width = (self.rect.width + 8) // 2
            # Borda azul na metade esquerda
            pygame.draw.rect(self.tela, (0, 0, 255), (self.rect.left - 4, self.rect.top - 4, half_width, self.rect.height + 8), 4)
            # Borda vermelha na metade direita
            pygame.draw.rect(self.tela, (255, 0, 0), (self.rect.left + half_width - 4, self.rect.top - 4, half_width, self.rect.height + 8), 4)
        elif selected_p1 or self.hovered_p1:
            pygame.draw.rect(self.tela, (0, 0, 255), self.rect.inflate(8, 8), 4)
        elif selected_p2 or self.hovered_p2:
            pygame.draw.rect(self.tela, (255, 0, 0), self.rect.inflate(8, 8), 4)
        else:
            pygame.draw.rect(self.tela, (0, 0, 0), self.rect.inflate(8, 8), 4)
        self.tela.blit(self.imagem, self.rect.topleft)
        # Renderizar texto "P1" e "P2"
        if selected_p1:
            text_surface_p1 = font_p.render("P1", True, AZUL)
            text_rect_p1 = text_surface_p1.get_rect()
            text_rect_p1.topleft = (self.rect.left + 5, self.rect.top + 5)
            self.tela.blit(text_surface_p1, text_rect_p1)
        if selected_p2:
            text_surface_p2 = font_p.render("P2", True, (255, 0, 0))
            text_rect_p2 = text_surface_p2.get_rect()
            text_rect_p2.topright = (self.rect.right - 5, self.rect.top + 5)
            self.tela.blit(text_surface_p2, text_rect_p2)



def draw_text(text, font, color, x, y, tela):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    tela.blit(text_surface, text_rect)


selected_index_p1 = 0
selected_index_p2 = 3
