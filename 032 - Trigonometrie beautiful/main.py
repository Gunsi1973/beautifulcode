import pygame as pg
from vektorklasse import Vec, pol2cart_noradians
import math

pg.init()
resolution = Vec(500,500)
screen = pg.display.set_mode(resolution)
center = resolution / 2
radius = min(resolution * 0.4)

clock = pg.time.Clock()

rotating_angle = 0
segment_count = 3


while True:
  clock.tick(40)
  for event in pg.event.get():
    if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or (event.type == pg.KEYDOWN and event.key == pg.K_q):
      quit()
    if event.type == pg.KEYDOWN and event.key == pg.K_KP_PLUS:
      segment_count += 1
    if event.type == pg.KEYDOWN and event.key == pg.K_KP_MINUS:
      segment_count = max(0, segment_count - 1)
  
  
  screen.fill((0,0,0))
  
  pg.draw.circle(screen,pg.Color("darkseagreen4"), center, radius, 3) 
  rotating_angle += 0.03
  rotating_point = pol2cart_noradians(radius, rotating_angle) + center
  pg.draw.circle(screen,pg.Color("darkseagreen4"), rotating_point, 10) 

  for segment_nr in range(segment_count):
    delta_angle = math.pi / segment_count
    segment_start_angle = delta_angle * segment_nr
    segment_end_angle = segment_start_angle + math.pi
    line_start = pol2cart_noradians(radius, segment_start_angle) + center
    line_end = pol2cart_noradians(radius, segment_end_angle) + center
    pg.draw.line(screen,pg.Color("gray29"), line_start, line_end, 1)
    
    #3 Schritte zur Position des oszilierenden goldenen Punktes
    rotierende_punkt_gegen_uhrzeigersinn = rotating_point.rotate2D_noradians(center, -segment_start_angle)
    projezierter_punkt = Vec(rotierende_punkt_gegen_uhrzeigersinn[0], center[1])
    osz_punkt = projezierter_punkt.rotate2D_noradians(center, segment_start_angle)
    pg.draw.circle(screen,pg.Color("darkgoldenrod1"), osz_punkt, 10) 

  #und hier wird das im Hintergrund gezeichnete Bild angezeigt
  pg.display.flip()

pg.quit()