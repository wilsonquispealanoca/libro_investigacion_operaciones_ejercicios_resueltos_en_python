import pulp
import matplotlib.pyplot as plt
import numpy as np

modelo = pulp.LpProblem("Sillas_sillones", pulp.LpMaximize)

x = pulp.LpVariable("Sillas", lowBound=0)
y = pulp.LpVariable("Sillones", lowBound=0)

modelo += 20*x + 35*y

modelo += 2*x + 4*y <= 32
modelo += x >= 4
modelo += y >= 2

modelo.solve()
x_opt = pulp.value(x)
y_opt = pulp.value(y)
z_opt = pulp.value(modelo.objective)

p1 = [0, 8]
p2 = [16, 0]

plt.figure(figsize=(8, 5), layout='constrained')

plt.plot(p2, p1, marker="o", color = "green", label = "2x + 4y <= 21 (R1)")
plt.axvline(4, color="red", label="x >= 4 (R2)")
plt.axhline(2, color="blue", label = "y >= 2 (R3)")
plt.plot(x_opt, y_opt, marker="o", markersize=14, color="orange", label=f"Z = {z_opt}")

x_vertices = [4, 4, x_opt]
y_vertices = [2, 6, y_opt]

plt.fill(x_vertices, y_vertices, color="green", alpha=0.3)
plt.annotate(
        f"Máximo beneficio {z_opt}\nFabricar {x_opt} sillas y {y_opt} sillones",
        xy = (x_opt, y_opt),
        xytext=(x_opt, y_opt + 1),
        arrowprops=dict(arrowstyle="->")
    )

plt.grid(linestyle="--", alpha = 0.3)
plt.xticks(np.arange(0, 20, 2))
plt.yticks(np.arange(0, 11, 2))
plt.legend()
plt.title("Ejercicio 9: Fabricación de sillas y sillones")
plt.xlabel("Tiempo de trabajo sillas")
plt.ylabel("Tiempo de trabajo sillones")
plt.show()