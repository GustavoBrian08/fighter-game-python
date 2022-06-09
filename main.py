import pygame

# Inicializando o pygame
pygame.init()

# Configurando a tela
tela_largura = 1000
tela_altura = 800

tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Fighter Game with Python")

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    pygame.display.update()

pygame.quit()
