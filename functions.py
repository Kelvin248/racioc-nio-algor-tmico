import pygame

class character:
    def __init__(self,life, vel, x,y,height,data, sprites, steps, surface):
        self.life = life
        self.speed = vel
        self.player_heigth = height
        self.rect = pygame.Rect((x,y,80,self.player_heigth))
        self.surface = surface

        #manipulação de sprites
        self.size = data[0] #colocando as proporções da sprite
        self.image_scale = data[1] #ajeitando a escala do sprite
        self.offset = data[2] #centralizando sprite na hitbox
        self.action = 0 # 0:normal 1:andando 2:pulando 3:ataque1 4:ataque2 5:defesa 6:dano 7:morto 8:vitória
        self.frame_index = 0
        self.animation_list = self.images_load(sprites, steps) #criando uma mátriz com os sprites 
        self.image = self.animation_list[self.action][self.frame_index]  
        self.timer = pygame.time.get_ticks() #timer para atualizar a sprite     
        
        #manipulação dos movimentos
        self.rotate = False 
        self.vel_y = 0
        self.attack_grid = True
        self.live = True

        self.attack_type = 0
        self.attack_accept = False
        self.running = False
        self.jump = True
        self.damage = False
        self.target = 0

    def images_load(self,sprites, steps):
        animation_list = []
        for y, step in enumerate(steps):
            temp_list = []
            for x in range(step):
                temp_img= sprites.subsurface(x*self.size, y*self.size, self.size, self.size)
                temp_list.append(pygame.transform.scale(temp_img, (self.size*self.image_scale,self.size*self.image_scale)))
            animation_list.append(temp_list)
        print(animation_list)
        return animation_list
    

    def move(self,up,down,left,right, attack1,attack2,target):
        self.target = target
        key = pygame.key.get_pressed()
        dx = 0
        dy = 0
        gravity = 1
        
        #controles
        if self.live and target.live and not key[attack1] and not key[attack2]:
            if key[left]:
                dx -= self.speed
                self.running = True
                self.rotate = True
            elif key[right]:
                dx +=self.speed
                self.running = True
            else:
                self.running = False
             
            if key[up] and self.jump:
                self.vel_y -= 20
                self.jump = False
                self.attack_grid = False
            if key[down]:
                self.player_heigth *= 0.5


        #Rotacionando personagens:
        if target.rect.centerx > self.rect.centerx and not key[left]:
            self.rotate = False
        else:
            self.rotate = True

        #gravidade
        self.vel_y += gravity
        dy += self.vel_y 

        #limites da tela
        if self.rect.left + dx <0:
            dx = -self.rect.left
        if self.rect.right + dx > 800:
            dx = 800 - self.rect.right
        if self.rect.bottom + dy > 570:
            self.vel_y = 0
            dy = 570 - self.rect.bottom
            self.jump = True
        
        if self.attack_grid:
            if key[attack1] or key[attack2]:        
                if key[attack1] and not key[attack2]:
                    self.attack(target,punch=True, kick=False)
                    self.attack_type = 1
                    self.attack_accept = True
                if key[attack2] and not key[attack1]:
                    self.attack(target, punch=False,kick=True)
                    self.attack_type = 2
                    self.attack_accept = True
                
        
        #atualizando posição do personagem
        self.rect.x += dx
        self.rect.y += dy

    def update_action(self, newaction):
        #atualizando mudanças de sprites
        if newaction != self.action:
            self.action = newaction
            self.frame_index = 0
            self.timer = pygame.time.get_ticks()


    def update_sprites(self):
        
        if not self.jump:
            self.update_action(2)
        elif self.attack_accept:
            if self.attack_type == 1:
                self.update_action(1)
            if self.attack_type == 2:
                self.update_action(3)
        elif self.running:
            self.update_action(5)
        elif self.life <= 0:
            self.live = False
            self.attack_grid = False
            self.update_action(4)
            if self.image == self.animation_list[self.action][-1]:
                self.frame_index = -1
        elif self.damage:
            self.update_action(6)
            if self.image == self.animation_list[self.action][-1]:
                self.damage = False
                self.target.attack_grid = True
        else:
            self.update_action(0)
        animation_cooldown = 50
        self.image = self.animation_list[self.action][self.frame_index]
        
        if pygame.time.get_ticks() - self.timer > animation_cooldown:
            self.frame_index += 1
            self.timer = pygame.time.get_ticks()

        if self.frame_index == len(self.animation_list[self.action]):
            self.frame_index = 0
            self.attack_accept = False
            self.attack_grid = True




    def attack(self,target, punch, kick):
        if punch == True and self.live:
            punch_attack = pygame.Rect(self.rect.centerx -(1.5* self.rect.width * self.rotate) ,self.rect.y, 1.5*self.rect.width,self.rect.height/2)
            pygame.draw.rect(self.surface,'green',punch_attack)
            if punch_attack.colliderect(target):
                target.life -= 10
                target.damage = True
                self.attack_grid = False
                pygame.draw.rect(self.surface,'red',punch_attack)
        if kick == True and self.live:
            kick_attack = pygame.Rect(self.rect.centerx -(1.5* self.rect.width * self.rotate) ,self.rect.y+90, 1.5*self.rect.width,self.rect.height/2)
            pygame.draw.rect(self.surface,'green',kick_attack)
            if kick_attack.colliderect(target):
                target.life -= 10
                target.damage = True
                self.attack_grid = False
                pygame.draw.rect(self.surface,'red',kick_attack)      

    def draw(self, color):
        img = pygame.transform.flip(self.image, self.rotate, False)
        pygame.draw.rect(self.surface, color, self.rect)
        self.surface.blit(img,(self.rect.x - (self.offset[0]*self.image_scale), self.rect.y - (self.offset[1]*self.image_scale)))
