# text_adventure.py

print("Willkommen zum Abenteuer im Schloss der Entscheidungen!")
print("Du befindest dich im ersten Raum des Schlosses. Vor dir siehst du zwei Türen: eine linke und eine rechte.")

# Erste Entscheidung
wahl = input("Möchtest du durch die linke Tür (L) oder die rechte Tür (R) gehen? ").strip().upper()

if wahl == "L":
    print("Du betrittst den linken Raum und siehst ein Fenster, das zum Garten hinausführt.")
    wahl2 = input("Möchtest du durch das Fenster klettern (F) oder weiter durch den Raum gehen (W)? ").strip().upper()
    
    if wahl2 == "F":
        print("Du kletterst aus dem Fenster und landest sicher im Garten. Du hast das Abenteuer erfolgreich beendet!")
    elif wahl2 == "W":
        print("Du gehst weiter durch den Raum und findest eine versteckte Tür zur Schatzkammer. Du hast gewonnen!")
    else:
        print("Ungültige Eingabe. Das Abenteuer endet hier.")

elif wahl == "R":
    print("Du betrittst den rechten Raum, der düster und unheimlich wirkt.")
    wahl2 = input("Möchtest du weiter in die Dunkelheit gehen (D) oder den Raum verlassen (V)? ").strip().upper()
    
    if wahl2 == "D":
        print("Du gehst weiter in die Dunkelheit, und plötzlich geht das Licht an. Ein grimmiger Wächter erscheint und fordert dich auf, umzukehren. Das Abenteuer endet hier.")
    elif wahl2 == "V":
        print("Du verlässt den Raum und entscheidest dich, das Schloss zu verlassen. Das Abenteuer endet hier.")
    else:
        print("Ungültige Eingabe. Das Abenteuer endet hier.")

else:
    print("Ungültige Eingabe. Das Abenteuer endet hier.")

print("Danke fürs Spielen!")
