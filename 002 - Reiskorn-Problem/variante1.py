total_reiskörner = 0
reiskörner = 1  # Start mit einem Reiskorn auf dem ersten Feld
gewicht_pro_reiskorn = 0.029  # Gewicht eines einzelnen Reiskorns in Gramm
gesamtgewicht = 0

for feld in range(1, 65):  # 64 Felder
    total_reiskörner += reiskörner
    gesamtgewicht += reiskörner * gewicht_pro_reiskorn
    print(f"Feld {feld}: {reiskörner} Reiskörner")  # Optional: Ausgabe für jedes Feld
    reiskörner *= 2  # Verdoppele die Anzahl für das nächste Feld

print("Gesamtanzahl der Reiskörner:", total_reiskörner)
print("Gesamtgewicht der Reiskörner in Gramm:", gesamtgewicht)