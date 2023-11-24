import pygame

#Inicio do game
pygame.init()

tamanho = 5

tela = pygame.display.set_mode((1500, 135))
clock = pygame.time.Clock()

jogando = True

while jogando:
    
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
    

    tela.fill("Black")

    clock.tick(30)
