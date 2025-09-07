from lector_de_archivos.resultados_esperados import obtener_resultados_esperados
from lector_de_archivos.parser_de_batallas import leer_batallas
from algoritmo.greedy import planificar_batallas

def correr_pruebas():

    resultados_esperados = obtener_resultados_esperados("archivos/resultados_esperados.txt")
    tests = ["10.txt", "50.txt", "100.txt", "1000.txt",
             "5000.txt", "10000.txt", "100000.txt"]

    for test in tests:
        batallas = leer_batallas("archivos/"+ test)
        coef = planificar_batallas(batallas)
        if coef != resultados_esperados[test]:
            print(f"{test}: FALLO")
        else:
            print(f"{test}: OK")