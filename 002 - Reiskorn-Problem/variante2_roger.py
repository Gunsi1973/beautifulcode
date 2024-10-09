# Berechnung der Gesamtanzahl der Reiskörner
total_sum = 0

for square in range(64):
    grains_of_rice = 2**square  # Verdoppelung pro Feld
    total_sum += grains_of_rice
    print(f"Square {square+1:2}. = {grains_of_rice:>27,} grains of rice, "
          f"for a total of {total_sum:>28,} grains of rice")

# Berechnung des Gesamtgewichts in Tonnen
weight = total_sum * 0.029 / 1000 / 1000  # Umrechnung in Tonnen
print("\nIf one grain of rice weighs 0.029 grams, the total weight of all grains is "
      f"{weight:,.0f} tons")