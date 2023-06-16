import pygame
from pygame import *
pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((127,255,212))
clock = pygame.time.Clock()
event_left = False
event_right = False
event_left2 = False
event_right2 = False
speed_x = 3
speed_y = 3
font1 = pygame.font.Font(None, 70)
game_over = 0
class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

class Picture(Area):
    def __init__(self, file_name, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.image = pygame.image.load(file_name)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Laber(Area):
    def set_text(self, text, fsize, text_color):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))



ball = Picture('ball.png', 222.5, 350, 62, 61, None)
platform = Picture('platform.png', 200, 450, 167, 35, None)
platform2 = Picture('platform.png', 200, 50, 167, 35, None)
start_x = 5
start_y = 5

game = True
count = 9
while game:
    ball.draw()
    platform.draw()
    platform2.draw()
    pygame.display.update()
    window.fill((127,255,212))
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                event_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                event_right = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                event_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                event_left = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                event_right2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                event_right2 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                event_left2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                event_left2 = False
    if event_right == True:
        platform.rect.x += 3
    if event_left == True:
        platform.rect.x -= 3
    if event_right2 == True:
        platform2.rect.x += 3
    if event_left2 == True:
        platform2.rect.x -= 3
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.colliderect(platform.rect) == True:
       speed_y *= -1
    if ball.colliderect(platform2.rect) == True:
       speed_y *= -1
    if ball.rect.x <= 0 or ball.rect.x >= 450:
        speed_x *= -1
    if ball.rect.y <= 0:
        speed_y *= -1
        
    

        


