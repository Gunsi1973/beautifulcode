import turtle
screen = turtle.Screen()
def zeichne_kreise(t, radius, farbe):
    t.circle(radius)
    t.color(farbe)

def zeichne_kreisblume(anzahl_kreise,radius, radius_variation, farbpalette):
    t = turtle.Turtle()
    t.pensize(2)
    t.speed(10)

    for i in range(12):
        farbe= farbpalette[i % len(farbpalette)]
        t.color(farbe)
        aktueller_radius = radius + (i * radius_variation)
        zeichne_kreise(t, aktueller_radius, farbe)
        t.right(360 / anzahl_kreise)

screen = turtle.Screen()
farbpalette = ["red", "blue", "purple", "yellow", "brown", "green",]
zeichne_kreisblume(12,50, 5, farbpalette)

screen.exitonclick()

# import turtle

# def zeichne_kreise(t, radius):
#     t.circle(radius)

# def zeichne_kreisblume(anzahl_kreise, radius, radius_variation, farbpalette):
#     t = turtle.Turtle()
#     t.pensize(2)
#     t.speed(0)  # Maximale Geschwindigkeit
    
#     screen = turtle.Screen()
#     screen.tracer(0)  # Animationen deaktivieren
    
#     for i in range(anzahl_kreise):
#         farbe = farbpalette[i % len(farbpalette)]
#         t.color(farbe)
#         aktueller_radius = radius + (i * radius_variation)
#         zeichne_kreise(t, aktueller_radius)
#         t.right(360 / anzahl_kreise)

#     screen.update()  # Zeichnung aktualisieren
#     screen.exitonclick()

# # Hauptprogramm
# farbpalette = ["red", "blue", "purple", "yellow", "brown", "green"]
# zeichne_kreisblume(50, 90, 0, farbpalette)

# import turtle
# import math

# def zeichne_kreise(t, radius):
#     t.circle(radius)

# def zeichne_kreisblume(anzahl_kreise, radius, farbpalette, wellenhoehe, frequenz):
#     t = turtle.Turtle()
#     t.pensize(2)
#     t.speed(0)  # Maximale Geschwindigkeit
    
#     screen = turtle.Screen()
#     screen.setup(width=800, height=600)  # Fenstergröße anpassen
#     # screen.tracer(0)  # Animationen deaktivieren
    
#     # Abstand zwischen den Kreisen
#     abstand = 5
#     start_x = -screen.window_width() // 2  # Startpunkt am linken Rand

#     for i in range(anzahl_kreise):
#         farbe = farbpalette[i % len(farbpalette)]
#         t.color(farbe)
        
#         # Berechnung der Position auf der Sinuslinie
#         x = start_x + i * abstand
#         y = wellenhoehe * math.sin(frequenz * x)
        
#         # Turtle an die neue Position setzen
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
        
#         # Kreis zeichnen
#         zeichne_kreise(t, radius)

#     screen.update()  # Zeichnung aktualisieren
#     screen.exitonclick()

# # Hauptprogramm
# farbpalette = ["red", "blue", "purple", "yellow", "brown", "green"]
# zeichne_kreisblume(
#     anzahl_kreise=180,  # Anzahl der Kreise
#     radius=30,         # Radius der Kreise
#     farbpalette=farbpalette,
#     wellenhoehe=100,    # Höhe der Sinuswelle
#     frequenz=0.05      # Frequenz der Sinuswelle (je kleiner, desto länger die Welle)
# )


