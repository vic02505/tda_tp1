def obtener_coeficiente_de_batallas(batallas_planificadas: list[tuple[int,int]]) -> int:
    coeficiente = 0
    suma_parcial = 0

    for batalla in batallas_planificadas:
        suma_parcial += batalla[0]
        coeficiente += batalla[1]*suma_parcial

    return coeficiente


def planificar_batallas(batallas_a_planificar: list[tuple[int,int]]) -> int:
    batallas_ordenadas = sorted(batallas_a_planificar, key=lambda x: x[0]/x[1])

    coef = obtener_coeficiente_de_batallas(batallas_ordenadas)

    return coef

