import matplotlib.pyplot as plt

# Berechnung der Reiskörner pro Feld
grains_per_square = [2**square for square in range(64)]
squares = list(range(1, 65))  # Feldnummern 1 bis 64

# Erstellen des Diagramms ohne logarithmische Skalierung
plt.figure(figsize=(10, 6))
plt.plot(squares, grains_per_square, marker='o', color='b', linestyle='-', linewidth=1, markersize=4)

# Beschriftung und Titel
plt.xlabel("Square Number")
plt.ylabel("Number of Grains of Rice")
plt.title("Exponential Growth of Rice Grains on a Chessboard")
plt.grid(True)

# Diagramm anzeigen
plt.show()
