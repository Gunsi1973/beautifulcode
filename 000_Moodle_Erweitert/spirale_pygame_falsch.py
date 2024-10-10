import pygame as pg
import math

# PyGame initialisieren
pg.init()
window_size = width, height = 1920, 1080
window = pg.display.set_mode(window_size)

# Farben und Parameter für die Spiralgalaxie
farben = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 255, 255), (0, 0, 255), (128, 0, 128)]
anzahl_linien = 120                # Anzahl der Linien in der Spirale
linienlänge = 5                    # Startlänge der Linie
linienwachstum = 3                 # Wie stark die Linienlänge pro Drehung zunimmt
winkel = 10                        # Winkel der Drehung für die Spirale

# Zentrum der Spiralgalaxie
zentrum_x, zentrum_y = width // 2, height // 2

# Taktgeber und Bildrate
clock = pg.time.Clock()
FPS = 40

# Zeichenschleife mit FPS Bildern pro Sekunde
laufende_linien = 0  # Zähler für die gezeichneten Linien
while True:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT or \
           event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE or \
           event.type == pg.KEYDOWN and event.key == pg.K_q:
            pg.quit()
            quit()

    # Spirale weiterzeichnen, solange die Linienanzahl nicht überschritten ist
    if laufende_linien < anzahl_linien:
        # Farbe auswählen und Kreislinie zeichnen
        color = farben[laufende_linien % len(farben)]
        angle = laufende_linien * math.radians(winkel)   # Winkel in Bogenmaß umrechnen
        
        # Berechnung der Endkoordinaten
        end_x = int(zentrum_x + linienlänge * math.cos(angle))
        end_y = int(zentrum_y + linienlänge * math.sin(angle))

        # Linie vom Zentrum zum berechneten Punkt zeichnen
        pg.draw.line(window, color, (zentrum_x, zentrum_y), (end_x, end_y), 2)

        # Länge und Linienanzahl für die nächste Linie erhöhen
        linienlänge += linienwachstum
        laufende_linien += 1

    # Bildschirm aktualisieren
    pg.display.flip()
