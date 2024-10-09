# lissajous_animation.py

import pygame
import math

# PyGame initialisieren
pygame.init()

# Bildschirmgröße und Farben
width, height = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)

# Bildschirm erstellen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animierte Lissajous-Figur")

# Lissajous-Parameter
A, B = width // 3, height // 3     # Amplituden
a, b = 3, 2                        # Frequenzen
delta = math.pi / 2                # Phasenverschiebung

# Laufzeitparameter
t = 0                              # Startzeit
clock = pygame.time.Clock()        # Kontrolle der Bildrate

# Hauptschleife für die Animation

screen.fill(black)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bildschirm leeren


    # Koordinaten berechnen
    x = int(width / 2 + A * math.sin(a * t + delta))
    y = int(height / 2 + B * math.cos(b * t))

    # Punkt zeichnen
    pygame.draw.circle(screen, white, (x, y), 3)

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Zeitvariable erhöhen und Bildrate setzen
    t += 0.01
    clock.tick(60)

pygame.quit()
