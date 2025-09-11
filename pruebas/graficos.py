from algoritmo.greedy import planificar_batallas
from matplotlib import pyplot as plt
import scipy as sp
import numpy as np

from .util import time_algorithm

# Genera listas de batallas (b, t)
def generar_batallas(n):
    b = np.random.randint(1, 1000, n)
    t = np.random.randint(1, 1000, n)
    return list(zip(b, t))

# Le dice a time_algorithm cómo generar los argumentos para cada n
def get_args(n):
    return (generar_batallas(n),)

def generar_grafico():
    # Tamaños de entrada
    sizes = np.linspace(1_000, 100_000, 20).astype(int)

    # Medir tiempos usando util.py
    resultados = time_algorithm(planificar_batallas, sizes, get_args)

    x = np.array(list(resultados.keys()))
    y = np.array(list(resultados.values()))

    # Ajuste por cuadrados mínimos: complejidad esperada O(n log n)
    def modelo_nlogn(n, c1, c2):
        return c1 * n * np.log(n) + c2
    
    #comentar el anterior y descomentar alguno de estos para ajustar por otro modelo
    # # O(n)
    # def modelo_n(n, c1, c2):
    #     return c1 * n + c2

    # # O(n^2)
    # def modelo_n2(n, c1, c2):
    #     return c1 * n**2 + c2

    (c1, c2), _ = sp.optimize.curve_fit(modelo_nlogn, x, y)
    print(f"Ajuste encontrado: c1={c1}, c2={c2}")

    # c1 es la pendiente escalada del término n log(n). Indica cuánto “crece” el tiempo de ejecución en función del tamaño n. Es la constante que acompaña a la complejidad teórica O(n log n).

    # c2 es un desfase o tiempo base. Representa un tiempo inicial “fijo” que el algoritmo tarda independientemente del tamaño (por ejemplo, overhead de iniciar la función).

    # Calcular errores
    y_pred = modelo_nlogn(x, c1, c2)

    # y_pred[i] es el tiempo que la curva ajustada dice que debería tomar el algoritmo para x[i].
    # y[i] es el tiempo que realmente tomó el algoritmo.

    # Error cuadrático total (||Ax - b||^2)
    r = np.sum((y_pred - y)**2)
    print(f"Error cuadrático total: {r}")#notacion cientifica
    print(f"Error cuadrático total con decimales: {r:.20f}")#decimal con 20 decimales

    errores_abs = np.abs(y_pred - y)

    # Graficar tiempos vs curva ajustada
    plt.figure()
    plt.plot(x, y, "bo", label="Mediciones")
    plt.plot(x, y_pred, "r--", label="Ajuste $n \\log n$")
    plt.xlabel("Tamaño n")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de ejecución de planificar_batallas")
    plt.legend()
    plt.show()

    # Graficar error absoluto
    plt.figure()
    plt.plot(x, errores_abs, "g")
    plt.xlabel("Tamaño n")
    plt.ylabel("Error absoluto (s)")
    plt.title("Error del ajuste")
    plt.show()
