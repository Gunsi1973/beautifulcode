import turtle as tu

# Turtle initialisieren
tu.speed("fastest")         # Geschwindigkeit der Turtle auf das Schnellste setzen
tu.bgcolor("white")          # Hintergrundfarbe
tu.color("purple")           # Farbe der Kreise

# Kreisblume zeichnen
anzahl_kreise = 36           # Anzahl der Kreise
winkel = 360 / anzahl_kreise # Winkel zwischen den Kreisen

for _ in range(anzahl_kreise):
    tu.circle(50)            # Zeichne einen Kreis mit Radius 50
    tu.left(winkel)          # Drehe die Turtle um den Winkel für den nächsten Kreis

# Programm beenden
tu.done()
