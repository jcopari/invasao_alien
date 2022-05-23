import sys
import pygame as pg
from nave import Nave


def checa_keydown(event, nave):
        if(event.type == pg.KEYDOWN):
            if(event.key == pg.K_RIGHT):
                    nave.movimento_direita = True
            elif(event.type == pg.KEYDOWN):    
                if(event.key == pg.K_LEFT):
                    nave.movimento_esquerda = True

def checa_keyup(event, nave):
        if(event.type == pg.KEYUP):
            if(event.key == pg.K_RIGHT):
                    nave.movimento_direita = False
            elif(event.key == pg.K_LEFT):
                    nave.movimento_esquerda = False

def checa_eventos(nave):
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            sys.exit()
        elif(event.type == pg.KEYDOWN):
            checa_keydown(event, nave)
        elif(event.type == pg.KEYUP):
            checa_keyup(event, nave)

def atualiza_tela(ai_settings, screen, nave):
    screen.fill(ai_settings.bg_color)
    nave.blitme()
    pg.display.flip()