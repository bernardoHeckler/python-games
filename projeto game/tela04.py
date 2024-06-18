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
    pygame.draw.line(tela,preto,(0,300),(800,300), 3) #linha preta
    pygame.draw.line(tela,preto,(50,100),(50,500), 3) #linha preta
    pygame.draw.line(tela,preto,(50,100),(100,400), 3) #linha preta
    pygame.draw.line(tela,preto,(150,150),(100,400), 3) #linha preta
    pygame.draw.line(tela,preto,(150,150),(150,480), 3) #linha preta
    pygame.draw.line(tela,preto,(150,480),(300,100), 3) #linha preta
    pygame.draw.line(tela,preto,(540,480),(300,100), 3) #linha preta

    
    pygame.display.update()




pygame.quit()