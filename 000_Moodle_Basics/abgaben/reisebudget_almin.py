Kosten_liste = []
Kosten_summe = 0
Budget = float(input("Gebe dein Budget ein: "))

#Ich habe es so gemacht, dass ich nicht für jede Kategorie einen eigenen "input()" machen muss.
while True:

    Kosten = input("Gebe die kosten der einzelnen Kategorien ein, wenn du fertig bist, gebe \"ende\" ein: ")

    if Kosten == "ende":
        break

    else:
        Kosten_float = float(Kosten)
        Kosten_liste.append(Kosten_float)



for i in Kosten_liste:
    Kosten_summe += i


Resultat = Budget - Kosten_summe

if Kosten_summe > Budget:
    print(f"Dein Budget reicht nicht für deine Reise, die Reise kosten überschreiten dein Budget um {round(Resultat) * -1} CHF.")
else:
    print(f"Deine Reise passt in dein Budget, dir sind noch {round(Resultat)} CHF übrig geblieben.")
