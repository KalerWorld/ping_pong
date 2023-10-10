#Подключение библиотеки
from pygame import *
from random import randint
#Создание фоновой музыки
mixer.init()
#mixer.music.load('space.ogg')
#mixer_music.play()
#fire = mixer.Sound('fire.ogg')
#-----------------------
#Подключение шрифта
font.init()
#-----------------------
window = display.set_mode((800,600))#Объект окна
background = Surface((800,600))
background.fill((112, 78, 10))
class GameSprite(sprite.Sprite):
    def __init__(self,speed,x,y):
        super().__init__()
        self.image = Surface((100,100))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,speed, x, y,number):
        super().__init__(speed, x, y)
        self.number = number
    def update(self):
        keys = key.get_pressed()
        if self.number == 1:
            if keys[K_UP] and self.rect.y>0:
                self.rect.y-=self.speed
            if keys[K_DOWN] and self.rect.y<500:
                self.rect.y+=self.speed
        else:
            if keys[K_w] and self.rect.y>0:
                self.rect.y-=self.speed
            if keys[K_s] and self.rect.y<500:
                self.rect.y+=self.speed
            
class Ball(GameSprite):
    def __init__(self, speed, x, y):
        super().__init__(speed, x, y)
        self.image = Surface((50,50))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player = Player(5,0,100,1)#Объект игрока
player2 = Player(5,700,100,2)#Объект игрока
players = sprite.Group()
players.add(player)
players.add(player2)
ball = Ball(10,400,300)
win = font.Font(None,72).render('Win',True,(255,255,255))
Game = True
clock = time.Clock()#Часы
#-----------------------
#Массив со всеми врагами
#---------------
Finish = False
while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
    if Finish == False:
        window.blit(background,(0,0))#Отрисовка заднего фона
        # Destroyed = font.Font(None,32).render('уничтожнено:'+str(player.destroyed),True,(255,255,255))
        # Missed = font.Font(None,32).render('Пропущенно:'+str(player.Missed),True,(255,255,255))
        # window.blit(Destroyed,(0,0))
        # window.blit(Missed,(0,20))
        ball.update()
        ball.reset()
        players.update()
        players.draw(window)
        #Проверка на события
    #Отрисовка
    display.update()
    #Частота кадров
    clock.tick(60)
    
