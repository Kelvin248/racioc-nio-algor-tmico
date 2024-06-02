import pygame

class character:
    def __init__(self,life,surface, vel, x,y):
        self.rotate = False
        self.life = 100
        self.speed = vel
        self.rect = pygame.Rect((x,y,80,180))
        self.surface = surface
        self.vel_y = 0
        self.jump = True
        self.attack_grid = True
        self.attack_type = 0
        
    
    def move(self,up,down,left,right, attack1,attack2,target):
        key = pygame.key.get_pressed()

        dx = 0
        dy = 0
        
        gravity = 1
        #controles

        if key[left]:
            dx -= self.speed
        if key[right]:
            dx +=self.speed
        if key[up] and self.jump:
            self.vel_y -= 25
            self.jump = False

        #Rotacionando personagens:
        if target.rect.centerx > self.rect.centerx:
            self.rotate = False
        else:
            self.rotate = True

        #gravidade
        self.vel_y += gravity
        dy += self.vel_y 

        #limites da tela

        if self.rect.left + dx <0:
            dx = -self.rect.left
        if self.rect.right + dx > 1200:
            dx = 1200 - self.rect.right
        if self.rect.bottom + dy > 670:
            self.vel_y = 0
            dy = 670 - self.rect.bottom
            self.jump = True
        
        if self.attack_grid:
            if key[attack1] or key[attack2]:
            
                if key[attack1]:
                    self.attack(target,punch=True, kick=False)
                    self.attack_type = 1
                if key[attack2]:
                    self.attack(target, punch=False,kick=True)
                    self.attack_type = 2
        
        
        
        #atualizando posição do personagem
        self.rect.x += dx
        self.rect.y += dy

    def attack(self,target, punch, kick):
        if punch == True:
            punch_attack = pygame.Rect(self.rect.centerx -(1.5* self.rect.width * self.rotate) ,self.rect.y, 1.5*self.rect.width,self.rect.height/2)
            pygame.draw.rect(self.surface,'green',punch_attack)
            if punch_attack.colliderect(target):
                target.life -= 10
                self.attack_grid = False
                pygame.draw.rect(self.surface,'red',punch_attack)
        if kick == True:
            kick_attack = pygame.Rect(self.rect.centerx -(1.5* self.rect.width * self.rotate) ,self.rect.y+90, 1.5*self.rect.width,self.rect.height/2)
            pygame.draw.rect(self.surface,'green',kick_attack)
            if kick_attack.colliderect(target):
                target.life -= 10
                self.attack_grid = False
                pygame.draw.rect(self.surface,'red',kick_attack)
        

    def draw(self, color):
        pygame.draw.rect(self.surface, color, self.rect)
