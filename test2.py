import pygame
screen = pygame.display.set_mode((800, 600))
pygame.font.init()
pygame.display.flip()

def principal():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        pygame.time.delay(30)

principal() 