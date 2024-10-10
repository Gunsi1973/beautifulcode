import random
import string

def passwort_generieren(länge, grossbuchstaben=True, kleinbuchstaben=True, zahlen=True, sonderzeichen=True):
    """Generiert ein zufälliges Passwort und stellt sicher, dass alle ausgewählten Zeichentypen enthalten sind."""
    
    # Listen der Zeichen basierend auf den Optionen
    grossbuchstaben_set = string.ascii_uppercase if grossbuchstaben else ""
    kleinbuchstaben_set = string.ascii_lowercase if kleinbuchstaben else ""
    zahlen_set = string.digits if zahlen else ""
    sonderzeichen_set = string.punctuation if sonderzeichen else ""
    
    # Überprüfen, ob mindestens ein Zeichensatz ausgewählt ist
    if not any([grossbuchstaben, kleinbuchstaben, zahlen, sonderzeichen]):
        return "Fehler: Es wurde kein Zeichensatz ausgewählt."
    
    # Mindestens ein Zeichen aus jedem gewählten Set zufällig auswählen
    ausgewählte_zeichen = []
    if grossbuchstaben:
        ausgewählte_zeichen.append(random.choice(grossbuchstaben_set))
    if kleinbuchstaben:
        ausgewählte_zeichen.append(random.choice(kleinbuchstaben_set))
    if zahlen:
        ausgewählte_zeichen.append(random.choice(zahlen_set))
    if sonderzeichen:
        ausgewählte_zeichen.append(random.choice(sonderzeichen_set))

    # Auffüllen des Passworts mit zufälligen Zeichen bis zur gewünschten Länge
    restlänge = länge - len(ausgewählte_zeichen)
    alle_zeichen = grossbuchstaben_set + kleinbuchstaben_set + zahlen_set + sonderzeichen_set
    ausgewählte_zeichen.extend(random.choice(alle_zeichen) for _ in range(restlänge))
    
    # Zeichen mischen, um die Reihenfolge zu zufälligen
    random.shuffle(ausgewählte_zeichen)
    
    # Passwort als String zurückgeben
    return ''.join(ausgewählte_zeichen)

def passwort_bewerten(passwort):
    """Bewertet die Stärke des generierten Passworts und gibt eine Rückmeldung."""
    länge = len(passwort)
    hat_grossbuchstaben = any(c.isupper() for c in passwort)
    hat_kleinbuchstaben = any(c.islower() for c in passwort)
    hat_zahlen = any(c.isdigit() for c in passwort)
    hat_sonderzeichen = any(c in string.punctuation for c in passwort)
    
    # Stärke basierend auf Kriterien bewerten
    punkte = sum([hat_grossbuchstaben, hat_kleinbuchstaben, hat_zahlen, hat_sonderzeichen])
    
    if länge >= 12 and punkte == 4:
        return "Stark"
    elif länge >= 8 and punkte >= 3:
        return "Mittel"
    else:
        return "Schwach"

# Benutzer*inneneingaben
print("Willkommen zum erweiterten Passwortgenerator!")
länge = int(input("Wie lang soll das Passwort sein? (min. 8 Zeichen): "))
grossbuchstaben = input("Grossbuchstaben verwenden? (j/n): ").lower() == 'j'
kleinbuchstaben = input("Kleinbuchstaben verwenden? (j/n): ").lower() == 'j'
zahlen = input("Zahlen verwenden? (j/n): ").lower() == 'j'
sonderzeichen = input("Sonderzeichen verwenden? (j/n): ").lower() == 'j'

# Passwort generieren und bewerten
generiertes_passwort = passwort_generieren(länge, grossbuchstaben, kleinbuchstaben, zahlen, sonderzeichen)
stärke = passwort_bewerten(generiertes_passwort)

# Ergebnisse ausgeben
print("Generiertes Passwort:", generiertes_passwort)
print("Passwortstärke:", stärke)
