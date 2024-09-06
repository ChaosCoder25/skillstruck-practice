import pygame
window = pygame.display.set_mode([400,300])
pygame.display.set_caption("Images")
image = pygame.image.load("imagel.png")
windoe.blit(image, [0,0])
pygame.display.flip()