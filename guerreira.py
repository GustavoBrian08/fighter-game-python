import pygame

class Guerreira:
    def __init__(self, jogador, x, y, virar, dados, sprite_sheet, passos_animacao, som):
        self.jogador = jogador
        self.tamanho = dados[0]
        self.imagem_escala = dados[1]
        self.deslocamento = dados[2]
        self.virar = virar
        self.lista_animacao = self.carregarImagens(sprite_sheet, passos_animacao)
        self.acao = 0
        self.indice_quadro = 0
        self.imagem = [self.lista_animacao][self.indice_quadro]
        self.atualiza_tempo = pygame.time.get_ticks()
        self.retangulo = pygame.Rect((x, y, 80, 180))
        self.velocidade_y = 0
        self.correndo = False
        self.pulando = False
        self.atacando = False
        self.ataque_tipo = 0
        self.ataque_cooldown = 0
        self.ataque_som = som
        self.dano = False
        self.vida = 100
        self.vivo = True


    def carregarImagens(self, sprite_sheet, passos_animacao):
        lista_animacao = []
        for y, animacao in enumerate(passos_animacao):
            modelo_imagem_lista = []
            for x in range(animacao):
                modelo_imagem = sprite_sheet.subsurface(x * self.tamanho, y * self.tamanho, self.tamanho, self.tamanho)
                modelo_imagem_lista.append(pygame.transform.scale(modelo_imagem, (self.tamanho * self.imagem_escala, self.tamanho * self.imagem_escala)))
            lista_animacao.append(modelo_imagem_lista)
        return lista_animacao