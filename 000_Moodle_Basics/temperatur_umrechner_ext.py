# temperaturumrechner.py

# Benutzer*inneneingabe zur Auswahl der Umrechnungsrichtung
print("Willkommen zum Temperaturumrechner!")
print("1: Celsius in Fahrenheit umrechnen")
print("2: Fahrenheit in Celsius umrechnen")
wahl = input("Wähle die Umrechnung (1 oder 2): ")

if wahl == "1":
    # Eingabe der Celsius-Temperatur
    celsius = float(input("Gib die Temperatur in Celsius ein: "))
    
    # Umrechnung in Fahrenheit
    fahrenheit = celsius * 9/5 + 32
    
    # Ergebnis auf zwei Dezimalstellen gerundet ausgeben
    print(f"{celsius} Grad Celsius sind {fahrenheit:.2f} Grad Fahrenheit.")

elif wahl == "2":
    # Eingabe der Fahrenheit-Temperatur
    fahrenheit = float(input("Gib die Temperatur in Fahrenheit ein: "))
    
    # Umrechnung in Celsius
    celsius = (fahrenheit - 32) * 5/9
    
    # Ergebnis auf zwei Dezimalstellen gerundet ausgeben
    print(f"{fahrenheit} Grad Fahrenheit sind {celsius:.2f} Grad Celsius.")

else:
    print("Ungültige Auswahl. Bitte starte das Programm neu und wähle 1 oder 2.")
