import pygame as pg
import random as rnd

# Gift wrapping algorithm
# https://de.wikipedia.org/wiki/Gift-Wrapping-Algorithmus


def gift_wrapping(points):
    # Find the leftmost point
    starting_point = pg.Vector2(min([(p.x, p.y) for p in points]))
    hull = [starting_point]
    
    while True:
        end_point = rnd.choice(points)
        if starting_point == end_point: continue

        for point in points:
            if (end_point - starting_point).cross(point - starting_point) < 0:   # if point is on the left side of the line, if value is negative, otherwise positive
                end_point = point
        
        if end_point == hull[0]:
            return hull
                
        hull.append(end_point)
        starting_point = end_point




pg.init()
window_size = width, height = 1200, 800
window = pg.display.set_mode(window_size)


clock = pg.time.Clock()
FPS = 60
POINT_CLOUD = 35
points = [pg.Vector2(rnd.randrange(width), rnd.randrange(height)) for _ in range(POINT_CLOUD)]

print(points)

while True:
  clock.tick(FPS)
  window.fill('black')

  for event in pg.event.get():
    if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE: quit()
    
    for point in points:
        pg.draw.circle(window, 'white', point, 2)
        
    hull = gift_wrapping(points)

    for point in hull:
        pg.draw.circle(window, 'red', point, 10)
        
    pg.draw.lines(window, 'green', True, hull, 1)
   
  pg.display.flip()
