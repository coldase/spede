import pygame
import random

pygame.init()

screen_width = 400
screen_height = 400
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
FPS = 60

class Cards:
    def __init__(self, num=None, maa=None):
        self.maa = maa
        self.num = str(num)
        self.size_x = 100
        self.size_y = 150
        self.nums = [2,3,4,5,6,7,8,9,10,"A","J","K","Q"]
        self.maat = ["C","D","H","S"]
        self.points = 0
        
    def draw_card(self):
        if self.maa and self.num:
            card = pygame.image.load(f"pics\\{self.num}{self.maa}.jpg")
            card = pygame.transform.scale(card, (self.size_x, self.size_y))
            screen.blit(card, (int(screen_width / 2) - int(self.size_x/2), 100))
        else:
            pygame.draw.rect(screen, WHITE, (int(screen_width/2) - int(self.size_x/2), 100, self.size_x, self.size_y))

    def random_card(self):
        self.num = random.choice(self.nums)
        self.maa = random.choice(self.maat)

    def check(self):
        pass

class Button:
    def __init__(self, pos_x, pos_y, color):
        self.size_x = 100
        self.size_y = 50
        self.pos_x = pos_x        
        self.pos_y = pos_y
        self.color = color

    def draw_btn(self):
        btn_rect = pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.size_x, self.size_y))
        return btn_rect
  

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
STEELBLUE = (27.5, 51, 70.6)

clock = pygame.time.Clock()

btn_red = Button(90, 300, RED)
btn_black = Button(210, 300, BLACK)
card = Cards()

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            if btn_red.draw_btn().collidepoint(event.pos):
                card.random_card()

                

    screen.fill(STEELBLUE)
    card.draw_card()
    btn_red.draw_btn()
    btn_black.draw_btn()
    pygame.display.flip()
pygame.quit()