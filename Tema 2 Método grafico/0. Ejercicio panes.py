import pulp
import matplotlib.pyplot as plt

# Definimos si la función objetivo es Max O Min
modelo = pulp.LpProblem("Modelo_panes", pulp.LpMaximize)

#Definimos las variables de decision y además especificamos que no deben tomar valores negativos
m = pulp.LpVariable("Marraqueta", lowBound=0)
b = pulp.LpVariable("Bizcocho", lowBound=0)

# Función objetivo Max Z = m + b
modelo += m + b, "Función objetivo"

# Restricción 1
modelo += m + 2*b <= 10, "R1"

# Resolver el problema
modelo.solve()

# Extraemos los valores optimos
m_opt = pulp.value(m)
b_opt = pulp.value(b)
z_opt = pulp.value(modelo.objective)

# Respondemos a la pregunta ¿Cuál es la cantidad máxima de panes que debemos comprar con solo 10 Bs?
print(f"Debemos comprar {m_opt} marraquetas y {b_opt} bizcochos para traer la mayor cantidad de panes posible.")

# Gráfica
# Restricción 1
# m + 2b = 10 -> m = 0, b = 5
p2 = [0, 5]

# m + 2b = 10 -> m = 10, b = 0
p1 = [10, 0]

# Recta R1
plt.plot(p1, p2, label="m + 2b <= 10 (R1)")

# Restricción No negatividad 1
plt.axvline(0, color="red", label="m => 0 (R2)")
# Restricción No negatividad 2
plt.axhline(0, color="green", label="b => 0 (R3)")

# Definimos la región factible
plt.fill_between(p1, p2, alpha=0.3, color="deepskyblue", label="Región Factible")

# Punto óptimo
plt.plot(m_opt, b_opt, marker="o", markersize=14, label="Punto óptimo")

# Nota de la solución
plt.annotate(f"Z = {z_opt:.0f}\nDebemos comprar\n{m_opt:.0f} marraquetas y {b_opt:.0f} bizcochos",
             xy = (m_opt, b_opt),
             xytext=(10, 40),
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"),
             bbox = dict(boxstyle="round", fc="white")
             )

plt.xticks([x for x in range(0, 15)])
plt.yticks([x for x in range(0, 9)])
plt.xlabel("Marraqueta")
plt.ylabel("Bizcocho")
plt.title("Gráfico para maximizar la cantidad de panes")
plt.grid(alpha=0.3)
plt.legend()
plt.show()