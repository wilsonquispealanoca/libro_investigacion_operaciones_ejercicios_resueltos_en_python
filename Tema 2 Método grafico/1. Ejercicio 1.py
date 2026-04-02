import pulp
import matplotlib.pyplot as plt
import numpy as np

# Definimos si la función objetivo es Max O Min
modelo = pulp.LpProblem("Problema_producto_A_y_B", pulp.LpMaximize)

#Definimos las variables de decision y además especificamos que no deben tomar valores negativos
a = pulp.LpVariable("Producto_A", lowBound=0)
b = pulp.LpVariable("Producto_B", lowBound=0)

# Función objetivo Max Z = 2a + 3b
modelo += 2*a + 3*b, "Funcion_objetivo"

# Restricción 1
modelo += a <= 10, "Restricción_1"

# Restricción 2
modelo += b <= 5, "Restricción_2"

# Restricción 3
modelo += a + b <= 12, "Restricción_3"

# Resolver el problema
modelo.solve()

# Mostrar resultados
print("Valor máximo: ", pulp.value(modelo.objective))

# Extraer valores óptimos
a_opt = pulp.value(a)
b_opt = pulp.value(b)
z_opt = pulp.value(modelo.objective)

# Gráfica
# Restricción_1: a = 10
plt.axvline(10, linestyle="--", color="orange", label="R1: a <= 10")

# Restricción_2: b = 5
plt.axhline(5, linestyle="--", label="R2: b <= 5")

# Restricciones de NO NEGATIVIDAD
plt.axvline(0, color="red", label="a >= 0")
plt.axhline(0, color="green", label="b >= 0")

# Restricción_3: a + b = 12
# a = 0, b = 12
P1 = [0, 12]
# a = 12, b = 0
P2 = [12, 0]

# Gráficamos la línea de la restricción
plt.plot(P1, P2, color='royalblue', linewidth=2.5, label="R3: x + y <= 12")

# Creamos un "suelo" o eje horizontal denso (500 puntos entre 0 y 15).
# Esto sirve para que la computadora evalúe las funciones en cada milímetro del gráfico.
a_vals = np.linspace(0, 15, 500)

# Definimos el "techo" real de la región factible.
# Como tenemos varias restricciones (b <= 5 y a + b <= 12), la región factible
# es el área que está por DEBAJO de AMBAS al mismo tiempo.
# np.minimum compara en cada punto cuál de las dos funciones es más baja (la más restrictiva).
limite_superior = np.minimum(5, 12 - a_vals)

# Rellenamos, pero limitando el eje X hasta la R1 (a=10)
plt.fill_between(a_vals, 0, limite_superior, 
                 where=(a_vals <= 10) & (limite_superior >= 0), 
                 alpha=0.3, color="deepskyblue", label="Región Factible")

# Graficamos un punto rojo en el punto optimo del problema
plt.plot(a_opt, b_opt, marker='o', markersize=14, color='red', 
         label=f'Solución Óptima: Z={z_opt}', zorder=10)

# Etiquetas para que se entienda mejor
plt.annotate(
    f'¡SOLUCIÓN ÓPTIMA!\n'
    f'Vender {a_opt:.0f} de A y {b_opt:.0f} de B\n'
    f'Z Máximo = {z_opt}',
    xy=(a_opt, b_opt),
    xytext=(20, 14),
    textcoords='offset points',
    fontsize=10,
    color='black',
    bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="red", lw=0.6),
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", color='red')
)

plt.title("Maximización de ganancia respecto a los productos")
plt.xlabel("Producto A")
plt.ylabel("Producto B")
plt.xticks([x for x in range(0, 16)])
plt.yticks(np.arange(0, 16, 1))
plt.grid(alpha=0.3)
plt.legend()
plt.show()
