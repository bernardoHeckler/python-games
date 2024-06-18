import pygame, time  # importar 
pygame.init() #iniciar
tamanho = (800,600) #tupla - largura, altura da tela, resolução
tela = pygame.display.set_mode( tamanho ) 
clock = pygame.time.Clock() # nosso relógio que atualiza os frames da tela

pygame.display.set_caption("Exemplo 01") # janela criada

# cores
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)

# bola se movendo em X
movXBOlinha = 400

# codição
direita = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    tela.fill(branco) # tela preenchida de branco
    pygame.draw.circle(tela,preto,(movXBOlinha,300),50) #bola preto
    pygame.draw.line(tela,preto,(100,100),(300,100), 3) #linha preto
    pygame.draw.rect(tela,preto,(400,100,200,50), 3) #retângulo preto
    
    pygame.display.update() # atualiza/salva tela

    # codição para bolinha bater nas paredes do lado direito e esquerda usando if e else
    if direita == True:    
        if movXBOlinha < 800:
            movXBOlinha = movXBOlinha + 10
        else: 
            direita = False
    else:
        if movXBOlinha > 0:
            movXBOlinha = movXBOlinha - 10
        else:
            direita = True 

    # fps(frames per second) calibrado para 60
    clock.tick(60) #fps



# fecha o programa
pygame.quit()