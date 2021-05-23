import pygame

pygame.init()

#tela principal
window = pygame.display.set_mode((500, 600))
pygame.display.set_caption('Diploma Battle')

background = pygame.image.load('imagens/fachada_insper.jpg').convert()

game = True

#Loop principal
while game:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            game = False

    
    window.fill((0, 0, 0))  # Preenche com a cor preta
    window.blit(background, (10, 10))

    #Atualiza jogo
    pygame.display.update()  

pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
