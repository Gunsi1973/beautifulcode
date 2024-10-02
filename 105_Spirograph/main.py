import pygame as pg
import random as rnd
import math as m


pg.init()
window_size = pg.Vector2(1200, 800)
window = pg.display.set_mode(window_size)
background = pg.surface.Surface(window_size)

last_position = False
draw_circles = True
draw_lines = True
speed = 0.1

pos1 = window_size / 2
radius1 = pg.Vector2(min(window_size) / 2, 0)
radius2 = radius1 * (rnd.random()) # sichstellen, dass der zweite Kreis kleiner ist als der erste
pos2 = pos1 + radius1 - radius2
radius3 = radius2 * (rnd.random())


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT: quit()
        if event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_ESCAPE, pg.K_q: quit()
                case pg.K_q: quit()
                case pg.K_k: draw_circles = not draw_circles
                case pg.K_l: draw_lines = not draw_lines
                case pg.K_KP_PLUS: speed *= 2
                case pg.K_KP_MINUS: speed /= 2

    window.fill('black')

    pos2 = pos1 + (pos2 - pos1).rotate(speed)
    # scaler = (radius1.length() * 2 * m.pi) / (radius2.length() * 2 * m.pi)   # OMG, so kompliziert gelöst... guck unten für die einfache Lösung
    radius2 = radius2.rotate(-speed * radius1.length() / radius2.length()) # siehe meine erste Lösung - OMG
    radius3 = radius3.rotate(-speed * radius1.length() / radius2.length()) # siehe meine erste Lösung - OMG
    
    pos3 = pos2 + radius3
    window.blit(background, (0, 0))
    if draw_circles:
        pg.draw.circle(window, 'white', pos1, radius1.length(), 1)
        pg.draw.circle(window, 'white', pos2, radius2.length(), 1)
        pg.draw.line(window, 'green', pos2, pos3, 1)
        pg.draw.circle(window, "yellow", pos3, 3)
    
    if draw_lines and last_position:
        pg.draw.line(background, 'red', last_position, pos3, 2)

    last_position = pos3
        
    pg.display.flip()
