import turtle as tu
import random

# Turtle initialisieren
tu.speed("fastest")               # Schnellste Zeichen-Geschwindigkeit
tu.bgcolor("white")               # Hintergrundfarbe
farben = ["purple", "blue", "pink", "red", "orange", "green", "yellow"]  # Farbpalette

# Funktion, um einen Spirographen zu zeichnen
def spirograph(r, abstand):
    for _ in range(int(360 / abstand)):
        tu.color(random.choice(farben))  # Wähle eine zufällige Farbe
        tu.circle(r)                     # Zeichne einen Kreis
        tu.left(abstand)                 # Drehe die Turtle um den Abstand

# Spirographen zeichnen
tu.width(2)                              # Setze die Breite des Stiftes
spirograph(100, 15)                      # Rufe die Funktion mit Radius 100 und Abstand von 15 Grad auf

# Programm beenden
tu.done()
