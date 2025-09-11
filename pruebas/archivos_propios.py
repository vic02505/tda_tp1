from lector_de_archivos.resultados_esperados import obtener_resultados_esperados
from lector_de_archivos.parser_de_batallas import leer_batallas
from algoritmo.greedy import planificar_batallas

def correr_pruebas_propias():

    resultados_esperados = obtener_resultados_esperados("archivos/resultados_esperados_propios.txt")
    tests = ["prueba1.txt", "prueba2.txt", "prueba3.txt"]

    print("\n######## Pruebas propias ########")
    for test in tests:
        batallas = leer_batallas("archivos/"+ test)
        coef = planificar_batallas(batallas)
        if coef != resultados_esperados[test]:
            print(f"{test}: FALLO")
        else:
            print(f"{test}: OK")