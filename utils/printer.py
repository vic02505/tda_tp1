from pprint import pprint

def imprimir_solucion(caso_de_prueba: str, batallas_planificadas: list[tuple[int,int]], coeficiente_de_batallas: int ):
    print("----------------------------------------------------------------------------------------------------------")
    print(f"Salida del caso de prueba {caso_de_prueba}")
    print(f"Coeficiente obtenido:{coeficiente_de_batallas}")
    print("Batallas planificadas:")
    pprint(batallas_planificadas)
    print("----------------------------------------------------------------------------------------------------------")

def imprimir_test(caso_de_prueba: str, coeficiente_obtenido: int, coeficiente_esperado: int):
    print("-------------------------------------------------------")
    print(f"Caso de prueba: {caso_de_prueba}")
    print(f"Coeficiente esperado: {coeficiente_esperado}")
    print(f"Coeficiente obtenido: {coeficiente_obtenido}")
    if coeficiente_esperado == coeficiente_obtenido:
        print("OK")
    else:
        print("Fallo")
    print("-------------------------------------------------------")