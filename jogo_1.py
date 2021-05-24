import pygame
import random

pygame.init()

#tela principal
comprimento = 500
altura = 450

comprimento_fundo = 568
altura_fundo = 513

comprimento_letras = 40
altura_letras = 40

posicao_x_letra = 225
posicao_y_letra = 0
comprimento_jogador = 90
altura_jogador = 90

window = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('Diploma Battle')

background = pygame.image.load('imagens/fachada_insper.jpg').convert()
background_scale = pygame.transform.scale(background, (comprimento_fundo, altura_fundo))
letra_I = pygame.image.load('imagens/letra_i.png').convert_alpha()
letra_D = pygame.image.load('imagens/letra_d.png').convert_alpha()
letra_I = pygame.transform.scale(letra_I, (comprimento_letras, altura_letras))
letra_D = pygame.transform.scale(letra_D, (comprimento_letras, altura_letras))
jogador_imagem = pygame.image.load('imagens/player2.png').convert_alpha()
jogador_imagem = pygame.transform.scale(jogador_imagem, (comprimento_jogador, altura_jogador))

class Letra(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = posicao_x_letra
        self.rect.y = posicao_y_letra
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > comprimento:
            self.rect.x =posicao_x_letra
            self.rect.y = posicao_y_letra
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

class aluno(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = comprimento/2
        self.rect.bottom = altura - 10




todas_letras = pygame.sprite.Group()
jogador = aluno(jogador_imagem)

for a in range(3):
    letraI = Letra(letra_I)
    letraD = Letra(letra_D)
    todas_letras.add(letraI)
    todas_letras.add(letraD)

game = True

clock = pygame.time.Clock() #Ajustando a velocidade
FPS = 30

#Loop principal
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False
    
    todas_letras.update()

    window.fill((0, 0, 0))  # Preenche com a cor preta
    window.blit(background_scale, (-20, 0))

    todas_letras.draw(window)
    window.blit(jogador.image, jogador.rect)
    #Atualiza jogo
    pygame.display.update()  

pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
