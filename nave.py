import pygame as pg

class Nave:
        def __init__(self, screen):
                self.screen = screen
                self.image = pg.image.load('figuras/ship.bmp')
                self.rect = self.image.get_rect()
                self.screen_rect = screen.get_rect()
                self.rect.centerx = self.screen_rect.centerx
                self.rect.bottom = self.screen_rect.bottom
                self.movimento_direita = False

        def pra_direita(self):
            if(self.movimento_direita):
                self.rect.centerx += 1

        def blitme(self):
            self.screen.blit(self.image, self.rect)

