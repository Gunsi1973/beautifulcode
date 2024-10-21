# Wie viel ist das Budget?
budget = float(input("Was ist dein Budget für die Reise?: "))
# Verschiedene Kategorien: Transport, Unterkunft, Verpflegung
transport = float(input("Wie viel Geld möchtest du für den transport ausgeben?: "))
unterkunft = float(input("Wie viel Geld möchtest du für deine Unterkunft ausgeben?: "))
verpflegung = float(input("Wie viel Geld möchtest du für die Verpflegung ausgeben?: "))

Kosten = (transport + unterkunft + verpflegung)

if Kosten > budget:
    print("Deine Reise liegt nicht im Budget.")
else:
    print("Deine Reise liegt im Budget.")
