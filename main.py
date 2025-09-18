import sys
from pruebas.archivos_de_la_catedra import correr_pruebas
from algoritmo.greedy import  planificar_batallas
from lector_de_archivos.parser_de_batallas import leer_batallas
from utils.printer import imprimir_solucion
from utils.graficos import generar_grafico

MODO_NORMAL = "1"
MODO_DE_TESTS = "2"
ARCHIVOS = "archivos/"

def main():
    modo_de_ejecucion = sys.argv[1]
    nombre_archivo = None

    if modo_de_ejecucion == MODO_NORMAL:
        # generar_grafico()
        nombre_archivo = sys.argv[2]

    if modo_de_ejecucion == MODO_NORMAL:
        batallas_a_planificar = leer_batallas(ARCHIVOS+nombre_archivo)
        batallas_planificadas, coeficiente_de_batallas = planificar_batallas(batallas_a_planificar)
        imprimir_solucion(nombre_archivo, batallas_planificadas, coeficiente_de_batallas)

    elif modo_de_ejecucion == MODO_DE_TESTS:
        correr_pruebas()
    else:
        raise RuntimeError("El tipo de ejecución proporcionado es inválido")


if __name__ == "__main__":
    main()