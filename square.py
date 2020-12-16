import pygame
import random


background_color = (0, 0, 0)
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
running = True


class Apple:
    def __init__(self, color):
        self.Xapple = random.randint(15, width - 15)
        self.Yapple = random.randint(15, height - 15)
        if color == 'blue':
            self.apple_color = (0, 1, 245)
        elif color == 'red':
            self.apple_color = (212, 1, 0)
        elif color == 'yellow':
            self.apple_color = (255, 255, 0)
            #self.Xapple = 22
            #self.Yapple = 322
        self.apple_location = (self.Xapple, self.Yapple)


class Player:
    def __init__(self):
        self.Xplayer = 120
        self.Yplayer = 20
        self.Xplayer_size = 60.0
        self.Yplayer_size = 60.0
        self.player_color = (255, 160, 0)

    def player_movment(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            if self.Xplayer < width - self.Xplayer_size:
                self.Xplayer = self.Xplayer + 0.3
        elif keys_pressed[pygame.K_LEFT]:
            if self.Xplayer > 0:
                self.Xplayer = self.Xplayer - 0.3
                keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            if self.Yplayer > 0:
                self.Yplayer = self.Yplayer - 0.3
                keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_DOWN]:
            if self.Yplayer < height - self.Yplayer_size:
                self.Yplayer = self.Yplayer + 0.3
        return (self.Xplayer, self.Yplayer)


def check_apple_eaten(player, the_big_apple):
    return player.Xplayer + player.Xplayer_size >= the_big_apple.Xapple - 15 and player.Xplayer <= the_big_apple.Xapple + 15\
        and player.Yplayer <= the_big_apple.Yapple + 15 and player.Yplayer + player.Yplayer_size >= the_big_apple.Yapple - 15


player = Player()
the_big_apple = Apple('red')
shrink_apple = Apple('blue')
fullscreen_apple = Apple('yellow')
while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(screen, the_big_apple.apple_color, the_big_apple.apple_location, 15)
    pygame.draw.circle(screen, shrink_apple.apple_color, shrink_apple.apple_location, 15)
    pygame.draw.circle(screen, fullscreen_apple.apple_color, fullscreen_apple.apple_location, 15)
    pygame.draw.rect(screen, player.player_color, pygame.Rect(player.player_movment(), (player.Xplayer_size, player.Yplayer_size)))
    if check_apple_eaten(player, the_big_apple):
        the_big_apple = Apple('red')
        player.Xplayer_size += 10
        player.Yplayer_size += 10
    if check_apple_eaten(player, shrink_apple):
        shrink_apple = Apple('blue')
        player.Xplayer_size -= 10
        player.Yplayer_size -= 10
    if check_apple_eaten(player, fullscreen_apple):
        fullscreen_apple = Apple('yellow')
        fullscreen_apple2 = Apple('red')
        pygame.display.toggle_fullscreen()
    pygame.display.update()