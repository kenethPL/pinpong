from pygame import *
'''Clases requeridas'''

#clase principal para sprites
class GameSprite(sprite.Sprite):
    #constructor de clases
       #constructor de clases
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height): # agregue dos parámetros más al crear y establezca el tamaño del rectángulo para la imagen usted mismo
        super().__init__()
 
        # cada sprite debe almacenar una propiedad image - imagen
        self.image = transform.scale(image.load(player_image), (wight, height)) # juntos 55,55 - parámetros
        self.speed = player_speed
 
        # cada sprite debe almacenar una propiedad  rect - el rectángulo en el que está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#la clase heredera del sprite del jugador (controlada por flechas)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#Escena del juego:
back = (200, 255, 255) # color de fondo (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#banderas responsables del estado del juego
game = True
finish = False
clock = time.Clock()
FPS = 60

#creando una pelota y una raqueta  
racket1 = Player('racket.png', 30, 200, 4, 50, 150) # al crear un sprite, se agregan dos parámetros más
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        # si la pelota alcanza los límites de la pantalla, cambie la dirección de su movimiento
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        # si la pelota voló más allá de la raqueta, mostramos la condición de pérdida para el primer jugador
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        # si la pelota pasó volando por la raqueta, mostramos la condición de pérdida para el segundo jugador
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)