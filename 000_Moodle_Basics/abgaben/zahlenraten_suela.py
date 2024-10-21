import random
geheimzahl = random.randint(1, 100)

versuche = 0

print("Ich habe eine Zahl zwischen 1 und 100 gewählt, finde sie heraus.")

print("Gib eine Zahl zwischen 1 und 100 ein: ")

while True:
    try:
        tipp = int(input())

        versuche += 1

        if tipp < geheimzahl:
            print("Die Zahl ist höher, versuche es noch einmal:")
        elif tipp > geheimzahl:
            print("Die Zahl ist tiefer, versuche es noch einmal")
        else:
            print(f"Glückwunsch, du hast die Zahl {geheimzahl} erraten")
            break

    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")