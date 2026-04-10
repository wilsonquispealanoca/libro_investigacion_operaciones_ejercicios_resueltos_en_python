"""
En una fábrica se dispone de 80 Kg de acero y 120 Kg de aluminio para fabricar bicicletas de montaña y
de paseo que se venderán a 200 Bs y 250 Bs respectivamente. Para fabricar una bicicleta de montaña son
necesarios 1 Kg de acero y 3 Kg de aluminio y para fabricar una de paseo 2 Kg cada uno de los metales.

a) Determina la función objetivo y las restricciones
b) Calcule cuantas bicicletas de cada tipo se tienen que fabricar para obtener el máximo beneficio.
"""

import pulp
import matplotlib.pyplot as plt
import numpy as np

model = pulp.LpProblem("Fabricacion_bicicletas", pulp.LpMaximize)

x = pulp.LpVariable("bicicletas_montaña", lowBound = 0)
y = pulp.LpVariable("bicicletas_de_paseo", lowBound = 0)

# Objective
model += 200*x + 250*y, "Objective function"

# Constraints
model += x + 2*y <= 80, "Constraint 1"

model += 3*x + 2*y <= 120, "Constraint 2"

# Solve
model.solve()

# Result
print(pulp.value(model.objective))

# Extract optimize values
x_opt = pulp.value(x)
y_opt = pulp.value(y)
z_opt = pulp.value(model.objective)

# x + 2y = 80
p1 = [0, 40]
p2 = [80, 0]

# 3x +2y = 120
q1 = [0, 60]
q2 = [40, 0]

# Sol optimize
plt.plot(x_opt, y_opt, marker = "o", markersize = 14, color="red", label=f"Z: {z_opt:.0f}")

# first linear ecuation
plt.plot(p2, p1, color="green", label="x + 2y <= 80 (R1)")
# Second linear ecuation
plt.plot(q2, q1, color="orange", label="3x + 2y <= 120 (R2)")
# First No negative ecuation
plt.axvline(0, color="red", label="x >=0 (R3)")
# Second No negative ecuation
plt.axhline(0, color="blue", label="y >=0 (R4)")
# Result note
plt.annotate(
    text=f"Máximo beneficio: {z_opt}\nFabricar\n{x_opt} bicicletas de montaña\n{y_opt} bicicletas de paseo",
    xy=(x_opt, y_opt),
    xytext=(x_opt + 10, y_opt + 2),
    textcoords='data',
    arrowprops=dict(arrowstyle="->")
    )

# --- Feasible Region Shading ---
# Define the coordinates for each vertex of the feasible region (x, y)
# We list them in order to "trace" the polygon correctly.
vertices_x = [0, 0, x_opt, 40] # [x = 0, x = 0, x = 20, y = 40]
vertices_y = [0, 40, y_opt, 0] # [y = 0, y = 40, y = 30, y = 0]

# Fill the polygon defined by the vertices
plt.fill(vertices_x, vertices_y, color='limegreen', alpha=0.3, label='Región Factible')

plt.xticks(np.arange(0,100, 10))
plt.yticks(np.arange(0,80, 10))
plt.legend()
plt.grid(alpha = 0.2, linestyle="--")
plt.title("Ejercicio 10: Método Gráfico: Fabricación de Bicicletas", fontsize=13)
plt.xlabel("Bicicletas de montaña (x)")
plt.ylabel("Bicicletas de paseo (y)")
plt.show()