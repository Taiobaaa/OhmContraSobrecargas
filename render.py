import pygame
import globais

functionList = []

print("aaaa")

def AddUpdateFunction(function):
    global functionList
    functionList.insert(1, function)

def RenderGame():
    global functionList

    print(globais.running)

    while globais.running:
        print(globais.running)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globais.running = False
        
        for function in functionList:
            function()
        pygame.display.update()
    pygame.quit()

pygame.init()
globais.tela = pygame.display.set_mode((800,  600))
pygame.display.set_caption("Ohm contra Sobrecargas!")
RenderGame