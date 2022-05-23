from settings import Settings
import pygame as pg
from nave import Nave
import funcoes_do_jogo as funcao

def run_game():
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion")
    nave = Nave(ai_settings, screen)
    while(True):
            funcao.checa_eventos(nave)
            nave.movimento()
            funcao.atualiza_tela(ai_settings, screen, nave)


run_game() 
