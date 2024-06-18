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
    pygame.draw.line(tela,preto,(0,0),(800,600), 3) #linha preta
    
    pygame.display.update()




pygame.quit()