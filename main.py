import pygame

# Inicializando o pygame
pygame.init()

# Definindo a taxa de quadros
relogio = pygame.time.Clock()
FPS = 60

# Configurando a tela
tela_largura = 1000
tela_altura = 800
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Fighter Game with Python")

# Definindo variáveis do jogo
rolagem_tela = 0

# Definindo chão do jogo
imagem_chao = pygame.image.load("assets/background/Layers-02/ground.png").convert_alpha()
imagem_chao = pygame.transform.scale(imagem_chao, (tela_largura - 200, tela_altura - 650))
imagem_chao_largura = imagem_chao.get_width()
imagem_chao_altura = imagem_chao.get_height()

# Configurando o fundo com parallax
imagens_fundo = []
for i in range(1, 6):
    imagem_fundo = pygame.image.load(f"assets/background/Layers-02/plx-{i}.png").convert_alpha()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (tela_largura, tela_altura - 140))
    imagens_fundo.append(imagem_fundo)
imagem_fundo_largura = imagens_fundo[0].get_width()


def desenharFundo():
    for x in range(4):
        velocidade_parallax = 1
        for img in imagens_fundo:
            tela.blit(img, ((x * imagem_fundo_largura) - rolagem_tela * velocidade_parallax, 0))
            velocidade_parallax += 0.2

def desenharChao():
    for x in range(15):
        tela.blit(imagem_chao, ((x * imagem_chao_largura) - rolagem_tela * 2.5, tela_altura - imagem_chao_altura))

# Loop principal do jogo
rodando = True
while rodando:
    # definindo a taxa de quadros
    relogio.tick(FPS)

    # desenhando o cenário
    desenharFundo()
    desenharChao()

    # teclas pressionadas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_LEFT] and rolagem_tela > 0:
        rolagem_tela -= 3
    if tecla[pygame.K_RIGHT] and rolagem_tela < 600:
        rolagem_tela += 3

    # evento de manipulação da tela
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # atulização da tela
    pygame.display.update()

pygame.quit()
