# Funktion zur Berechnung der Gesamtkosten und des Vergleichs mit dem Budget
def berechne_reisekosten(budget, transport, unterkunft, verpflegung):
    gesamtkosten = transport + unterkunft + verpflegung
    differenz = budget - gesamtkosten
    return gesamtkosten, differenz

# Benutzeraufforderung zur Eingabe des Budgets und der Kosten für verschiedene Kategorien
budget = float(input("Gib dein Reisebudget ein: "))
transport = float(input("Gib die geschätzten Transportkosten ein: "))
unterkunft = float(input("Gib die geschätzten Unterkunftskosten ein: "))
verpflegung = float(input("Gib die geschätzten Verpflegungskosten ein: "))

# Berechnung der Gesamtkosten und der Differenz zum Budget
gesamtkosten, differenz = berechne_reisekosten(budget, transport, unterkunft, verpflegung)

# Ausgabe der Ergebnisse
print("\n--- Reisekostenübersicht ---")
print(f"Gesamtkosten der Reise: {gesamtkosten:.2f} CHF")
print(f"Dein Budget: {budget:.2f} CHF")

# Überprüfung, ob das Budget eingehalten wird
if gesamtkosten <= budget:
    print("Die Reise bleibt innerhalb deines Budgets! Du hast noch {:.2f} CHF übrig.".format(differenz))
else:
    print("Achtung! Du überschreitest dein Budget um {:.2f} CHF.".format(abs(differenz)))