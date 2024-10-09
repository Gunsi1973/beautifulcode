# zahlenratespiel.py

import random

print("Willkommen zum Zahlenratespiel!")
print("Ich habe eine Zahl zwischen 1 und 100 ausgewählt.")
print("Kannst du sie erraten?")

# Generiere eine zufällige Zahl zwischen 1 und 100
geheimzahl = random.randint(1, 100)

# Variablen initialisieren
versuche = 0
gefunden = False

# Spielschleife
while not gefunden:
    # Eingabe der Spieler*in
    tipp = int(input("Gib deinen Tipp ein: "))
    versuche += 1
    
    # Überprüfe den Tipp
    if tipp < geheimzahl:
        print("Zu niedrig! Versuch's nochmal.")
    elif tipp > geheimzahl:
        print("Zu hoch! Versuch's nochmal.")
    else:
        # Zahl wurde korrekt geraten
        gefunden = True
        print("Glückwunsch! Du hast die Zahl", geheimzahl, "erraten.")
        print("Du hast", versuche, "Versuche gebraucht.")

print("Danke fürs Spielen!")
