import random
import string

def passwort_generieren(länge, grossbuchstaben=True, kleinbuchstaben=True, zahlen=True, sonderzeichen=True):
    """Generiert ein zufälliges Passwort mit den ausgewählten Optionen."""
    zeichen = ""
    if grossbuchstaben:
        zeichen += string.ascii_uppercase
    if kleinbuchstaben:
        zeichen += string.ascii_lowercase
    if zahlen:
        zeichen += string.digits
    if sonderzeichen:
        zeichen += string.punctuation

    # Prüfen, ob Zeichen für die Passwortgenerierung vorhanden sind
    if not zeichen:
        return "Fehler: Es wurde kein Zeichensatz ausgewählt."

    # Passwort durch zufällige Auswahl generieren
    passwort = ''.join(random.choice(zeichen) for _ in range(länge))
    return passwort

# Benutzer*inneneingaben
print("Willkommen zum Passwortgenerator!")
länge = int(input("Wie lang soll das Passwort sein? (min. 8 Zeichen): "))
grossbuchstaben = input("Grossbuchstaben verwenden? (j/n): ").lower() == 'j'
kleinbuchstaben = input("Kleinbuchstaben verwenden? (j/n): ").lower() == 'j'
zahlen = input("Zahlen verwenden? (j/n): ").lower() == 'j'
sonderzeichen = input("Sonderzeichen verwenden? (j/n): ").lower() == 'j'

# Passwort generieren und ausgeben
generiertes_passwort = passwort_generieren(länge, grossbuchstaben, kleinbuchstaben, zahlen, sonderzeichen)
print("Generiertes Passwort:", generiertes_passwort)
