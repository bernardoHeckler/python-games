import pygame, time
pygame.init()
tamanho = (800,600) 
tela = pygame.display.set_mode( tamanho )
clock = pygame.time.Clock()

pygame.display.set_caption("Exemplo 01")


preto = (0,0,0)
branco = (255,255,255)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    tela.fill(branco)
    pygame.draw.line(tela,preto,(70,70),(250,400), 3) #linha preta
    pygame.draw.circle(tela,preto,(70,70),43) #bola preta
    pygame.draw.circle(tela,branco,(70,70),40) #bola preta

    pygame.draw.line(tela,preto,(250,400),(500,340), 3) #linha preta
    pygame.draw.circle(tela,preto,(250,400),43) #bola preta
    pygame.draw.circle(tela,branco,(250,400),40) #bola preta
    
    pygame.draw.line(tela,preto,(500,300),(700,300), 3) #linha preta
    pygame.draw.circle(tela,preto,(500,300),43) #bola preta
    pygame.draw.circle(tela,branco,(500,300),40) #bola preta
        

    pygame.draw.circle(tela,preto,(700, 300),43) #bola preta
    pygame.draw.circle(tela,branco,(700,300),40) #bola preta
    
    pygame.display.update()




pygame.quit()