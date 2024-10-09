# taschenrechner.py

# Definition der Funktionen

def addieren(a, b):
    """Addiert zwei Zahlen."""
    return a + b

def subtrahieren(a, b):
    """Subtrahiert die zweite Zahl von der ersten."""
    return a - b

def multiplizieren(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b

def dividieren(a, b):
    """Dividiert die erste Zahl durch die zweite."""
    if b == 0:
        return "Fehler: Division durch Null"
    return a / b

def dezimal_zu_binaer(n):
    """Wandelt eine Dezimalzahl in eine Binärzahl um."""
    return bin(n)[2:]  # Entfernt das '0b'-Präfix von Python-Binärzahlen

def potenzieren(a, b):
    """Berechnet a hoch b."""
    return a ** b

# Hauptprogramm mit Benutzer*innen-Menü

print("Willkommen zum Taschenrechner!")

while True:
    print("\nWähle eine Rechenart:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Dezimal zu Binär")
    print("6. Potenzieren")
    print("7. Beenden")

    wahl = input("Deine Wahl: ")

    if wahl == '7':
        print("Danke fürs Benutzen des Taschenrechners!")
        break

    if wahl in ['1', '2', '3', '4', '6']:
        a = float(input("Gib die erste Zahl ein: "))
        b = float(input("Gib die zweite Zahl ein: "))

        if wahl == '1':
            print("Ergebnis:", addieren(a, b))
        elif wahl == '2':
            print("Ergebnis:", subtrahieren(a, b))
        elif wahl == '3':
            print("Ergebnis:", multiplizieren(a, b))
        elif wahl == '4':
            print("Ergebnis:", dividieren(a, b))
        elif wahl == '6':
            print("Ergebnis:", potenzieren(a, b))

    elif wahl == '5':
        n = int(input("Gib eine Dezimalzahl ein: "))
        print("Binärdarstellung:", dezimal_zu_binaer(n))

    else:
        print("Ungültige Auswahl. Bitte wähle erneut.")

print("Programm beendet.")
