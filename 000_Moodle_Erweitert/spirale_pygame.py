import pygame as pg
import math

# PyGame initialisieren
pg.init()
window_size = width, height = 1920, 1080
window = pg.display.set_mode(window_size)

# Farben und Parameter für die Spiralgalaxie
farben = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 255, 255), (0, 0, 255), (128, 0, 128)]
anzahl_linien = 200                # Anzahl der Linien in der Spirale
linienlänge = 3                    # Startlänge der Linie
linienwachstum = 0.1                 # Wie stark die Linienlänge pro Drehung zunimmt
winkel = 5                       # Winkel der Drehung für die Spirale

# Zentrum der Spiralgalaxie
zentrum_x, zentrum_y = width // 2, height // 2
aktueller_x, aktueller_y = zentrum_x, zentrum_y  # Startpunkt festlegen

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
        # Farbe auswählen
        color = farben[laufende_linien % len(farben)]
        angle = laufende_linien * math.radians(winkel)   # Winkel in Bogenmaß umrechnen
        
        # Berechnung der neuen Endkoordinaten basierend auf dem aktuellen Punkt
        end_x = int(aktueller_x + linienlänge * math.cos(angle))
        end_y = int(aktueller_y + linienlänge * math.sin(angle))

        # Linie vom aktuellen Punkt zum neuen Punkt zeichnen
        pg.draw.line(window, color, (aktueller_x, aktueller_y), (end_x, end_y), 2)

        # Aktualisiere den Startpunkt auf die neuen Endkoordinaten
        aktueller_x, aktueller_y = end_x, end_y

        # Länge und Linienanzahl für die nächste Linie erhöhen
        linienlänge += linienwachstum
        laufende_linien += 1

    # Bildschirm aktualisieren
    pg.display.flip()
