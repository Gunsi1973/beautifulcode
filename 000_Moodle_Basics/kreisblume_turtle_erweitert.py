import turtle as tu
import random

# Turtle initialisieren
tu.speed("fastest")               # Schnellste Zeichen-Geschwindigkeit
tu.bgcolor("lightblue")            # Hintergrundfarbe
farben = ["purple", "blue", "pink", "red", "orange", "green"]  # Farbpalette

# Kreisblume zeichnen
anzahl_kreise = 36                 # Anzahl der Kreise für die Blume
winkel = 360 / anzahl_kreise       # Winkel zwischen den Kreisen

for _ in range(anzahl_kreise):
    tu.color(random.choice(farben)) # Zufällige Farbe aus der Palette wählen
    radius = random.randint(30, 60) # Zufälligen Radius für die Kreise wählen
    tu.circle(radius)               # Kreis zeichnen
    tu.left(winkel)                 # Drehe die Turtle für den nächsten Kreis

# Programm beenden
tu.done()
