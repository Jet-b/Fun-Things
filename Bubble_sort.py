import pygame
from random import randrange
import numpy as np
from math import cos, sin, radians
from matplotlib import cm


pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Bubble Sort")

WHITE = (255, 255, 255)

cmap = cm.plasma

def get_color_from_cmap(value, cmap):
    normalized_value = value/ HEIGHT
    rgba_color = cmap(normalized_value)
    return tuple(int(255 * c) for c in rgba_color[:3])

def bubble_sort_once(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def height_to_color(height, max_height):
    normalized = height / max_height
    return (int(255 * normalized), 0, int(255 * (1 - normalized)))

def draw_list_as_bars(lst):
    for i, h in enumerate(lst):
        color = get_color_from_cmap(h, cmap)
        pygame.draw.line(screen, color, (i, HEIGHT), (i, HEIGHT - h), 1)

def draw_list_as_points(lst):
    for i, h in enumerate(lst):
        color = get_color_from_cmap(h, cmap)
        pygame.draw.circle(screen, color, (i, HEIGHT - h), 1)

def draw_list_as_segments(lst):
    for i, h in enumerate(lst):
        color = get_color_from_cmap(h, cmap)
        angle = ((360/WIDTH) * i) - 90
        pygame.draw.line(screen, color, (WIDTH//2, HEIGHT//2), line_to_point(WIDTH//2, HEIGHT//2, angle, min(WIDTH, HEIGHT)//2 - 10), 4)

def line_to_point(x, y, angle, length):
    angle = radians(angle)
    x2 = x + length * cos(angle)
    y2 = y + length * sin(angle)
    return (x2, y2)

if __name__ == "__main__":
    running = True
    sorting = False
    lst = [randrange(0, HEIGHT) for _ in range(WIDTH)]
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    lst = [randrange(0, HEIGHT) for _ in range(WIDTH)]
                if event.key == pygame.K_RETURN:
                    sorting = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    sorting = False

        if sorting:
            lst = bubble_sort_once(lst)
        
        screen.fill(WHITE)
        draw_list_as_segments(lst)
        
        pygame.display.flip()
        



    pygame.quit()
    quit()