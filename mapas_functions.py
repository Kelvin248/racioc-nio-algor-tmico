import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)




# Classe botão mapas
class Button_mapas():
    def __init__(self, x, y, imagem, nome, Tela, Fonte):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.hovered_p1 = False
        self.hovered_p2 = False
        self.nome = nome
        self.tela = Tela
        self.fonte = Fonte

    def draw2(self, selected_p1):
        if selected_p1 or self.hovered_p1:
            pygame.draw.rect(self.tela, WHITE, self.rect.inflate(8, 8), 4)
        else:
            pygame.draw.rect(self.tela, BLACK, self.rect.inflate(8, 8), 4)
        self.tela.blit(self.imagem, self.rect.topleft)
        # Renderizando o nome do mapa com borda preta
        self.draw_text_with_border(self.nome, self.fonte, (128, 0, 0), BLACK, self.rect.left + 5, self.rect.top + 5)

    def draw_text_with_border(self, text, font, color, border_color, x, y):
        text_surface = font.render(text, True, border_color)
        offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for ox, oy in offsets:
            self.tela.blit(text_surface, (x + ox, y + oy))
        text_surface = font.render(text, True, color)
        self.tela.blit(text_surface, (x, y))

def draw_text(text, font, color, x, y, tela):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    tela.blit(text_surface, text_rect)
