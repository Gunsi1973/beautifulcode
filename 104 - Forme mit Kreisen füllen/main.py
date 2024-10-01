import pygame as pg
import random as rnd
import os

# Circle Sizes
rad_minimum = 4
rad_maximum = 20

pg.init()

image = pg.image.load("roger.png")

# Bildschirmauflösung abfragen
screen_info = pg.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Bildgrösse abfragen
image_width = image.get_width()
image_height = image.get_height()

# Prüfen, ob das Bild kleiner oder grösser als der Bildschirm ist
if image_width != screen_width or image_height != screen_height:
    # Bild proportional anpassen, um Bildschirmgrösse zu erreichen
    scale_factor = min(screen_width / image_width, screen_height / image_height)
    new_size = (int(image_width * scale_factor), int(image_height * scale_factor))
    image = pg.transform.scale(image, new_size)
    width, height = new_size
else:
    width, height = image_width, image_height

# Fenster auf die Grösse des Bildes setzen
window = pg.display.set_mode((width, height))

mask = [(x,y) for x in range(image.get_width()) for y in range(image.get_height()) if image.get_at((x,y))[0]] # holt sich alle Pixel, die nicht schwarz sind
rnd.shuffle(mask) # mischt die Pixel, damit sie nicht in Reihenfolge abgearbeitet werden, sonst ist es langweilig

circles_drawn = []

while mask:     # solange noch Pixel in der Liste sind
  
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE: quit()

    # pos = pg.Vector2(rnd.randrange(0, width), rnd.randrange(0, height))
    pos = pg.Vector2(mask.pop())
    rad = rnd.randrange(rad_minimum, rad_maximum)

       
# eleganter Code
    for pos2, rad2 in circles_drawn:
        if pos.distance_to(pos2) - rad - rad2 < 0: break
    else:                                                   # wird nur ausgeführt, wenn die Schleife nicht durch break unterbrochen wurde - geht nur in Python
        pg.draw.circle(window, "green", pos, rad, 2)
        circles_drawn.append((pos, rad))
        pg.display.flip()

# Funktion zum Generieren eines eindeutigen Dateinamens
def get_unique_filename(base_name, extension="png"):
    counter = 1
    while True:
        filename = f"{base_name}_{counter}.{extension}"
        if not os.path.exists(filename):  # Überprüfen, ob der Dateiname bereits existiert
            return filename
        counter += 1

# Speichern des Bildes mit einem eindeutigen Dateinamen
output_file = get_unique_filename("output")
pg.image.save(window, output_file)
print(f"Bild gespeichert als {output_file}")

pg.quit()