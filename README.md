# tda_tp1
Repositorio del primer trabajo práctico de la materia Teoría de Algoritmos

[Consigna](https://algoritmos-rw.github.io/tda_bg/tps/2025_2/tp1/)

# Análisis de la consigna

## 1. Problema
- Tenemos un conjunto de **batallas** $i = 1, ..., n$.
- Cada batalla tiene:
  - **Tiempo de duración** $t_i$ (no se pueden hacer batallas en paralelo, todas se hacen secuencialmente).
  - **Peso o importancia** $b_i$ (cuán relevante es la victoria en esa batalla).
- Hay que organizar las batallas en un **orden secuencial** que minimice la **suma ponderada de los tiempos de finalización**:

$$
\text{Costo total} = \sum_{i=1}^{n} b_i F_i
$$

donde $F_i$ es el **momento en que termina la batalla $i$**.

---

## 2. Cálculo de los tiempos de finalización
- Si la batalla $j$ es la primera en ejecutarse:

$$
F_j = t_j
$$

- Si la batalla $j$ sigue a la batalla $i$:

$$
F_j = F_i + t_j
$$

- De manera general, si tenemos un orden
$\pi = [\pi_1, \pi_2, \pi_3, ..., \pi_n]$

$$
F_{\pi_1} = t_{\pi_1}, \quad F_{\pi_2} = t_{\pi_1} + t_{\pi_2}, \quad \dots, \quad F_{\pi_k} = \sum_{j=1}^{k} t_{\pi_j}
$$

Esto significa que el **impacto de cada batalla depende de las anteriores**, ya que se acumulan los tiempos.

---

## 3. Función objetivo
La función objetivo a minimizar es:

$$
\sum_{i=1}^{n} b_i F_i
$$

- Queremos **ganar primero las batallas importantes y rápidas** para que las victorias más importantes lleguen antes.
- Es una **suma ponderada de tiempos de finalización**.

---

## 4. Tipo de problema
- Este problema es un **problema de scheduling de un solo recurso** (un ejército que puede atacar solo una batalla a la vez).

---

## 5. Datos clave
- **Input:** Listado de batallas $(t_i, b_i)$
- **Output:** Orden de las batallas que minimiza $\sum b_i F_i$
- **Restricciones:**
  - No se pueden dividir o paralelizar batallas.
  - Todas deben completarse.

---

## 6. Ideas para el algoritmo (sin implementar)
- Calcular una **prioridad para cada batalla** (por ejemplo $t_i / b_i$).
- Ordenar las batallas según esa prioridad.
- Procesarlas secuencialmente en ese orden.
- Sumar los tiempos de finalización para calcular la función objetivo.

# Análisis de complejidad

```python
# O(n)
def obtener_coeficiente_de_batallas(batallas_planificadas: list[tuple[int,int]]) -> int:

    coeficiente = 0     # O(1)
    suma_parcial = 0    # O(1)

    for batalla in batallas_planificadas: # O(n)
        suma_parcial += batalla[0]  # O(1)
        coeficiente += batalla[1]*suma_parcial # O(1)

    return coeficiente


def planificar_batallas(batallas_a_planificar: list[tuple[int,int]]) -> int:

    planificacion = [] # O(1)
    # O(n log n) por usar sorted
    batallas_a_planificar_aux = sorted(batallas_a_planificar, key=lambda x: x[0]/x[1])

    for batalla in batallas_a_planificar_aux: # O(n)
        planificacion.append(batalla)

    coef = obtener_coeficiente_de_batallas(planificacion) # O(n)

    return coef

'''
  1. obtener_coeficiente_de_batallas:
      O(n)

  2. planificar_batallas:
      O(n log n) + O(n) + O(n) = O(n log n) + 2 O(n) = O(n log n) pues crece más rápido que O(n)

  ====>  Algoritmo greedy : O(n log n)
'''
```

# Justificación del algoritmo
Como mencionamos anteriormente, estamos frente a un problema de Scheduling donde buscamos desarrollar la mayor cantidad de batallas importantes. Es decir, minimizar la suma ponderada de los tiempos de finalización. 

$$
\sum_{i=1}^{n} b_i F_i
$$

Para ello lo que planteamos fue:
- Decidir en qué orden ejecutar las batallas
- según el orden de importancia y tiempo de duración

$$
t_i / b_i
$$

Entonces, de esta forma nos garantizamos que la batalla que dure menos tiempo y sea más importante va a suceder primero.

## ¿Por qué $t/b$?
Haciendo el análisis de dos batallas:
  - $t_i,b_i$
  - $t_j,b_j$

Queremos decidir cuál va antes...

### Caso 1: $i$ antes que $j$
$$
C_{i→j}​=b_i​(T+t_i​)+b_j​(T+t_i​+t_j​)
$$
### Caso 2: $j$ antes que $i$

$$
C_{j→i​}=b_j​(T+t_j​)+b_i​(T+t_j​+t_i​)
$$

### Calculo diferencia de costos
$$
C_{i→j} -  C_{j→i​} = ?
$$
Desarrollo cada costo:
$$
C_{i→j}​=b_i​(T+t_i​)+b_j​(T+t_i​+t_j​) \\

C_{i→j}​=b_i T+ b_i t_i +b_j​ T+b_j t_i​+ bj t_j​

$$


$$
C_{j→i​}=b_j​(T+t_j​)+b_i​(T+t_j​+t_i​)\\
C_{j→i​}=b_j​ T+b_j t_j+b_i T+ b_i t_j​+ b_i t_i​
$$

Ahora si calculo: $C_{i→j} -  C_{j→i​}$. Resto m.a.m.
$$

C_{i→j}​=b_i T+ b_i t_i +b_j​ T+b_j t_i​+ bj t_j​ \\
C_{j→i​}=b_i​ T+b_i t_i+b_j T+ b_j t_j​+ b_i t_ij \\
------------------\\
C_{i→j} -  C_{j→i​} = b_j t_i - b_i t_j
$$

Entonces:
- Si $b_j t_i > b_i t_j$ ; $C_{i→j} > C_{j→i​}$ el costo de $i$ esté antes que $j$ es mayor, por lo que conviene que $j$ vaya antes que $i$
- $C_{i→j} > C_{j→i​}$ es equivalente:
$$
b_j t_i > b_i t_j \\
t_i > b_i t_j / b_j \\
t_i / b_i > t_j / b_j
$$

Por lo tanto, para minimizar la sumatoria del costo total de todas las batallas, el orden que esté $t/b$ debe ser creciente.

## Variabilidad de $t_i$, $b_i$
El algoritmo planteado tiene una complejidad de $O(n * log n)$.

Las variables $t_i$, $b_i$ afectan únicamente al orden final de las batallas, pero no afectan la cantidad de operaciones realizadas.

- Tenemos $n$ batallas y hacemos operaciones con cada una.
- La operación de ordenar con ``sorted`` tiene complejidad $O(n * log n)$
- La operación de calcular el cociente $t_i/b_i$ es $O(1)$ por cada batalla, lo que en total es $O(n)$.
- Por lo tanto, el paso de cálculo de la prioridad y el ordenamiento conjunto sigue siendo $O(n * log n)$.
- Finalmente, calcular el coeficiente de batallas planificadas es $O(n)$ , y en este punto los valores de $t_i$, $b_i$ ya han sido considerados al ordenar la lista.

Entonces:
- La variabilidad de $t_i$, $b_i$ no afecta la complejidad temporal del algoritmo.
- Lo que si cambia es el resultado final del coeficiente, es decir, el orden óptimo de las batallas.