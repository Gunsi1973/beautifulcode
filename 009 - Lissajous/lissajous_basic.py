# lissajous_static.py

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
pygame.display.set_caption("Statische Lissajous-Figur")

# Lissajous-Parameter
A, B = width // 3, height // 3     # Amplituden
a, b = 3, 7                        # Frequenzen
delta = math.pi / 2                # Phasenverschiebung

# Bildschirm leeren
screen.fill(black)

# Schleife zur Berechnung und Darstellung der Punkte der Lissajous-Figur
for t in range(1000):
    x = int(width / 2 + A * math.sin(a * t * 0.01 + delta))
    y = int(height / 2 + B * math.cos(b * t * 0.01))
    pygame.draw.circle(screen, white, (x, y), 2)

# Bildschirm aktualisieren und anzeigen
pygame.display.flip()

# Warte, bis das Fenster geschlossen wird
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
