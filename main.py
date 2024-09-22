import pygame

pygame.init()

win_width = 500
win_height = 500

clock = pygame.time.Clock()

window = pygame.display.set_mode((win_width,win_height))
window.fill((204,255,255))

font = pygame.font.Font(None,32)
text = ""
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                text ="Клавишу Y нажали"
            if event.key == pygame.K_q:
                text = "Клавишу Q нажали"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
                text = "Клавишу Y отпустили"
            if event.key == pygame.K_q:
                text = "Клавишу Q отпустили"
    pygame.display.update()
    window.blit(font.render(text, True,(0, 0, 0), (225, 255, 255)),(win_width/2, win_height/2))
    clock.tick(60)