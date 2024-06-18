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
    pygame.draw.line(tela,preto,(10,30),(400,580), 3) #linha preta
    pygame.draw.line(tela,preto,(790,30),(400,580), 3) #linha preta
    pygame.draw.line(tela,preto,(10,30),(790,30), 3) #linha preta
    
    pygame.display.update()




pygame.quit()