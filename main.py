import pygame
import random

pygame.init()   # Inicializa o pygame
pygame.display.set_caption('Jogo da cobra')   # Setamos o nome da janela
largura, altura = 800, 600   # Seta o tamanho da janela
tela = pygame.display.set_mode((largura, altura))   # Passa as informações do tamanho da tela como uma Tupla, tem que passar como um tupla
relogio = pygame.time.Clock()

# Variaveis com as cores, são padrão RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0 , 255, 0)

# Parametros da Cobra
tamanho_quadrado = 20  #  Definimos a posição com tamanho do pixel 10
velocidade_atualizacao = 15

def gerar_posicao_comida():

    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20) * 20
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x,comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelho)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_posicao_comida()

    while not fim_jogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # Desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # Atualizar a posicao da Cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        # Desenhar a cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # Se a cobra bateu no própio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_cobra - 1)

        # Atualização da tela
        pygame.display.update()

        # Criar um nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_posicao_comida()

        relogio.tick(velocidade_atualizacao)

rodar_jogo()
