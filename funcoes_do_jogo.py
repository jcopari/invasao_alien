import sys
import pygame as pg
from nave import Nave


def checa_eventos(nave):
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            sys.exit()
        elif(event.type == pg.KEYDOWN):
            if(event.key == pg.K_RIGHT):
                    nave.movimento_direita = True
        elif(event.type == pg.KEYUP):
            if(event.key == pg.K_RIGHT):
                    nave.movimento_direita = False


def atualiza_tela(ai_settings, screen, nave):
    screen.fill(ai_settings.bg_color)
    nave.blitme()
    pg.display.flip()