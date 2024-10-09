import turtle as tu

# Setze die Geschwindigkeit und Hintergrundfarbe
tu.speed("fastest")
tu.bgcolor("white")
tu.left(90)  # Starte die Turtle, die nach oben zeigt

def zeichne_baum(länge):
    """Zeichnet einen rekursiven Baum mit Turtle."""
    if länge < 10:  # Abbruchbedingung
        return

    # Zeichne den Hauptast
    tu.forward(länge)

    # Erstes Verzweigen nach links
    tu.left(30)
    zeichne_baum(länge - 15)

    # Zweites Verzweigen nach rechts
    tu.right(60)
    zeichne_baum(länge - 15)

    # Zurück zur ursprünglichen Position und Richtung
    tu.left(30)
    tu.backward(länge)

# Starte den Baum mit einer Länge von 100
zeichne_baum(100)

# Abschluss
tu.done()
