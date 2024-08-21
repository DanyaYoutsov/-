from pygame import *
import shooter_game

init()

mw = display.set_mode((600, 600))
fps = time.Clock()
button1 = Rect(200, 200, 200, 50)
button2 = Rect(200, 280, 200, 50)
bg = transform.scale(image.load('rocket.png'), (700, 500))




font.init()
faf = font.SysFont('Arial', 35).render('START', True, (0, 255, 0))
faf1 = font.SysFont('Arial', 35).render('EXIT', True, (0, 255, 0))
running = True
while running:
    mw.blit(bg, (0, 0))
    for e in event.get():
            if e.type == QUIT:
                running = False
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                if button1.collidepoint(e.pos):
                    shooter_game.game()
                if button2.collidepoint(e.pos):
                    running = False
                    quit()
    draw.rect(mw, (100, 100, 100), button1)
    draw.rect(mw, (100, 100, 0), button2)
    mw.blit(faf,(225, 210))
    mw.blit(faf1,(225, 290))








    display.update()
    fps.tick(60)











