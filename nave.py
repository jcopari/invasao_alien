import pygame as pg

class Nave:
        def __init__(self,ai_settings, screen):
                self.screen = screen
                self.ai_settings = ai_settings
                self.image = pg.image.load('figuras/ship.bmp')
                self.rect = self.image.get_rect()
                self.screen_rect = screen.get_rect()
                self.rect.centerx = self.screen_rect.centerx
                self.rect.bottom = self.screen_rect.bottom
                self.center = float(self.rect.centerx)
                #Movimentação
                self.movimento_direita = False
                self.movimento_esquerda = False

        
        
        
        def movimento(self):
            if(self.movimento_direita and self.rect.right < self.screen_rect.right):
                if(self.movimento_direita):
                    self.center += self.ai_settings.nave_fator_velocidade
            if(self.movimento_esquerda and self.rect.left > 0):   
                if(self.movimento_esquerda):
                    self.center -= self.ai_settings.nave_fator_velocidade
            #Atualiza OBJETO rect de acordo com o self.center 
            self.rect.centerx = self.center
            
        
        
        def blitme(self):
            self.screen.blit(self.image, self.rect)

