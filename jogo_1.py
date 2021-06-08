import pygame
from constantes import comprimento, altura
from tela_do_jogo import tela_jogo
from tela_inicio import tela_inicio

pygame.init()
pygame.mixer.init()

# ----Gera tela principal
window = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('Diploma Battle')

tela_jogo(window)  #Inicia a tela do jogo?

pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
