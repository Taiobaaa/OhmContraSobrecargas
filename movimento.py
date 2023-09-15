import pygame
import globais
import render
mov = globais.mov
tela = globais.tela
x = globais.x
y = globais.y
width = globais.width
height = globais.height

def update():
    global x
    global y
    
    teclado = pygame.key.get_pressed()

    if teclado[pygame.K_LEFT]: #isso tudo aqui pega as setinhas do teclado quando voce clica!
        x -= mov

    if teclado[pygame.K_RIGHT]:
        x += mov

    if teclado[pygame.K_UP]:
        y -= mov

    if teclado[pygame.K_DOWN]:
        y += mov

    # globais.x = x
    # globais.y = y

    tela.fill((0,0,0))
    player = pygame.draw.rect(tela, (0,128,0), (x, y, width, height))

render.AddUpdateFunction(update)

    

# while globais.running:
#     teclado = pygame.key.get_pressed()

#     if teclado[pygame.K_LEFT]: #isso tudo aqui pega as setinhas do teclado quando voce clica!
#         x -= mov

#     if teclado[pygame.K_RIGHT]:
#         x += mov

#     if teclado[pygame.K_UP]:
#         y -= mov

#     if teclado[pygame.K_DOWN]:
#         y += mov
#     globais.x = x
#     globais.y = y

#     tela.fill((0,0,0))
#     player = pygame.draw.rect(tela, (0,128,0), (x, y, width, height))
#     # x2 = 200 
#     # y2 = 150
#     # parede = pygame.draw.rect(tela, (255,0,0), (x2, y2, width, height))
#     # if player.colliderect(parede):
#     #     player = pygame.draw.rect(tela, (0,0,255), (x, y, width, height))   
#     #     mov = 0
#     # if mov == 0 and (teclado[pygame.K_DOWN]) :
#     #     mov = 1