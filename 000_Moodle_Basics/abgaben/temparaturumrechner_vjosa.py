# Funktion zur Umrechnung von Celsius in Fahrenheit oder von Fahrenheit in Celsius

def celsius_in_fahrenheit(celsius, decimal_places):
    fahrenheit = celsius * (9/5) + 32
    return round(fahrenheit, decimal_places)

def fahrenheit_in_celsius(fahrenheit, decimal_places):
    celsius = (fahrenheit - 32) * (5/9)
    return round(celsius, decimal_places)

# Benutzeraufforderung zur Eingabe der Temperatur in Celsius oder Farenheit
celsius = float(input("Gib die Temperatur in Celsius ein: "))
fahrenheit = float(input("Gib die Temperatur in Fahrenheit ein: "))
decimal_places = int(input("Gib die Anzahl der Dezimalstellen ein, auf die gerundet werden soll: "))


# Umrechnung in Fahrenheit und in Celsius
fahrenheit_gerechnet = celsius_in_fahrenheit(celsius, decimal_places)
celsius_gerechnet = fahrenheit_in_celsius(fahrenheit, decimal_places)

# Ausgabe der Ergebnisse
print(f"{celsius}°C entsprechen {fahrenheit_gerechnet:.2f}°F, gerundet auf {decimal_places} Dezimalstellen.")
print(f"{fahrenheit}°F°C entsprechen {celsius_gerechnet:.2f}°C, gerundet auf {decimal_places} Dezimalstellen.")