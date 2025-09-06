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
