from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_speed, player_x, player_y, player_image, w, h):
        super().__init__()
        self.player_speed = player_speed
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def myach(self):
        self.s_x = 3
        self.s_y = 3
        self.rect.y += self.s_y
        self.rect.x += self.s_x
        
        if sprite.collide_rect(ere, self):
            self.s_y *= -1
        if self.rect.y < 0:
            lose1 = font.SysFont('Arial', 35).render('бал нижнему', True, (255, 255, 0))
            mw.blit(lose1, (300, 250))
        if sprite.collide_rect(rer, self):
            self.s_y *= -1
        if self.rect.x > 700:
            lose2 = font.SysFont('Arial', 35).render('бал верхнему', True, (255, 255, 0))
            mw.blit(lose2, (300, 250))
            
    


class Player(GameSprite):
    def update_d(self):
        key1 = key.get_pressed()
        if key1[K_a] and self.rect.x >= 1:
            self.rect.x -= self.player_speed
        if key1[K_d] and self.rect.x <= 600:
            self.rect.x += self.player_speed
    def update_u(self):
        key1 = key.get_pressed()
        if key1[K_RIGHT] and self.rect.x >= 1:
            self.rect.x += self.player_speed
        if key1[K_LEFT] and self.rect.x <= 600:
            self.rect.x -= self.player_speed

font.init()
mw = display.set_mode((700, 500))
display.set_caption('PING PONG')
backround = transform.scale(image.load('tenis.jpg'), (700, 500))
mixer.init()
mixer.music.load('elevator-music-vanoss-gaming-background-music.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.1)
rer = Player(5, 350, 400, 'pngwing.com (1).png', 100, 100)
ere = Player(5, 350, 0, 'pngwing.com (2).png', 100, 100)
wew = Ball(5, 350, 200, 'pngwing.com (3).png', 20, 20)

poops1 = 3
poops2 = 3

dad1 = 0
dad2 = 0
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        mw.blit(backround, (0,0))
        rer.update_d()
        rer.reset()
        ere.update_u()
        ere.reset()
        wew.reset()
        wew.myach()
        



        



        display.update()
    time.Clock().tick(60)

