from pruebas.archivos_de_la_catedra import correr_pruebas_catedra
from pruebas.archivos_propios import correr_pruebas_propias
from pruebas.graficos import generar_grafico

def main():
    correr_pruebas_catedra()

    correr_pruebas_propias()

    # generar_grafico()

if __name__ == "__main__":
    main()