import turtle as tu
import random

# Turtle initialisieren
tu.speed("fastest")               # Schnellste Zeichen-Geschwindigkeit
tu.bgcolor("black")               # Hintergrundfarbe

# Farben für die Spiralgalaxie definieren
farben = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

# Parameter für die Spirale
anzahl_linien = 120                # Anzahl der Linien in der Spirale
linienlänge = 5                    # Startlänge der Linie
linienwachstum = 3                 # Wie stark die Linienlänge pro Drehung zunimmt
winkel = 59                        # Winkel der Drehung für die Spirale

# Schleife zum Zeichnen der Spiralgalaxie
for i in range(anzahl_linien):
    tu.color(farben[i % len(farben)]) # Wähle die Farbe aus der Liste (wiederholt sich)
    tu.forward(linienlänge)           # Zeichne die Linie
    tu.left(winkel)                   # Drehe die Turtle
    linienlänge += linienwachstum     # Erhöhe die Länge der Linie für die nächste Runde

# Programm beenden
tu.done()
