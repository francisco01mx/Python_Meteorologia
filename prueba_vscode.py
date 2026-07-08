import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("VS Code usando Python correctamente")
print("Python:", sys.version)
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)

dias = [1, 2, 3, 4, 5]
temperatura = [32, 34, 35, 33, 36]

plt.figure(figsize=(8, 5))
plt.plot(dias, temperatura, marker="o")
plt.title("Prueba desde VS Code")
plt.xlabel("Día")
plt.ylabel("Temperatura °C")
plt.grid(True)
plt.show()