import pygame as pg

# pygame ab Version 2.0 wird benötigt
# Installation im Terminal mit
#   --> pip install pygame (windows)
#   --> pip3 install pygame (mac)
#   --> sudo apt-get install python3-pygame (Linux Debian/Ubuntu/Mint)

pg.init()
window_size = width, height = 1920, 1080
window = pg.display.set_mode(window_size)


clock = pg.time.Clock()
FPS = 40

# Zeichenschleife mit FPS Bildern pro Sekunde
while True:
  clock.tick(FPS)
  window.fill('black')

  for event in pg.event.get():
    if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE: quit()

  pg.display.flip()
