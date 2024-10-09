# reisebudget.py

print("Willkommen beim Reisebudget-Rechner!")
print("Bitte gib dein Reisebudget und die geschätzten Kosten für verschiedene Kategorien ein.")

# Eingabe des Budgets
budget = float(input("Wie hoch ist dein gesamtes Budget für die Reise (in CHF)? "))

# Eingabe der Kosten in verschiedenen Kategorien
transport_kosten = float(input("Geschätzte Kosten für Transport (in CHF): "))
unterkunft_kosten = float(input("Geschätzte Kosten für Unterkunft (in CHF): "))
verpflegung_kosten = float(input("Geschätzte Kosten für Verpflegung (in CHF): "))

# Berechnung der Gesamtkosten
gesamtkosten = transport_kosten + unterkunft_kosten + verpflegung_kosten

# Ausgabe der Gesamtkosten und des Ergebnisses
print("\nDeine gesamten Reisekosten betragen:", gesamtkosten, "CHF")

if gesamtkosten <= budget:
    print("Gute Nachrichten! Du bleibst innerhalb deines Budgets.")
else:
    print("Achtung! Deine Reise übersteigt das Budget um", gesamtkosten - budget, "CHF.")

print("Vielen Dank, dass du den Reisebudget-Rechner benutzt hast!")
