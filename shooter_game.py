from pygame import *
from random import *


def game():
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


    class Player(GameSprite):
        def update(self):
            key1 = key.get_pressed()
            if key1[K_a] and self.rect.x >= 1:
                self.rect.x -= self.player_speed
            if key1[K_d] and self.rect.x <= 600:
                self.rect.x += self.player_speed
        def push(self):
            puly = Puly(20, self.rect.x+50, self.rect.y, 'bullet.png', 5, 10)
            Pulys.add(puly)
    global dad
    dad = 0
    class Enemy(GameSprite):
        def update(self):
            if self.rect.y < 650:
                self.rect.y += self.player_speed
            if self.rect.y >= 650:
                global dad
                dad += 1
                self.rect.x = randint(0, 600)
                self.rect.y = randint(-100, -50)

    class Puly(GameSprite):
        def update(self):
            self.rect.y -= self.player_speed
            if self.rect.y < 0:
                self.kill()

    font.init()

    player = Player(4, 0, 399, 'tyu.png', 100, 100)

    Pulys = sprite.Group()
    mw = display.set_mode((700, 500))
    display.set_caption('LABERINT')
    bg = transform.scale(image.load('5919bd04f21b815c0c8a5bв80.jpg'), (700, 500))
    mixer.init()
    mixer.music.load('feat_Kuplinov_-_Kuplinovyjj_God_71661070.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)
    with open('despasito.txt', 'r') as file:
        main_records = file.read()


    monsters = sprite.Group()
    for i in range(5):
        monster = Enemy(randint(1, 3), randint(0, 600), 1, 'sss.png', 80, 80)
        monster.add(monsters)


    dad1 = 0
    game = True
    finish = False
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    player.push()
                    
        if not finish:
            win = font.SysFont('Arial', 35).render('Вы пропустили: '+str(dad), True, (0, 255, 0))
            mw.blit(bg, (0,0))
            lose = font.SysFont('Arial', 35).render('Вы обезвредили: '+str(dad1), True, (0, 255, 0))
            mw.blit(lose, (0, 35))
            mw.blit(win, (0, 0))
            player.reset()
            player.update()
            monsters.update()
            monsters.draw(mw)
            for i in Pulys:
                i.reset()
                i.update()
            kill = sprite.groupcollide(Pulys, monsters, True, True)
            for i in kill:
                dad1 += 1
                monster = Enemy(randint(1, 3), randint(0, 600), 1, 'sss.png', 80, 80)
                monster.add(monsters)
            if dad >= 5:
                
                lose1 = font.SysFont('Arial', 35).render('Вы проиграли(', True, (255, 255, 0))
                mw.blit(lose1, (300, 250))
                finish = True
                best = ''
                with open('despasito.txt', 'w') as file:
                    if dad1 > int(main_records):
                        file.write(str(dad1))
                        best = 'Вы побили рекорд'
                    else:
                        file.write(str(main_records))
                result = f'Вы унечтожели {best}{str(dad1)}'
                bad = font.SysFont('Arial', 35).render(result, True, (255, 255, 0))
                mw.blit(bad, (200, 300))
                
            display.update()
        else:
            finish = False
            dad = 0
            dad1 = 0
            for i in monsters:
                i.kill()
            
            time.delay(3000)
            for i in range(5):
                monster = Enemy(randint(1, 3), randint(0, 600), 1, 'sss.png', 80, 80)
                monster.add(monsters)
                




















        time.Clock().tick(60)


