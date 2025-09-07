
def obtener_resultados_esperados(path_de_archivo_de_resultados: str) -> dict:

    resultados_esperados = {}
    with open(path_de_archivo_de_resultados, "r") as f:
        lineas = [line.strip() for line in f if line.strip()]

    for i in range(0, len(lineas), 2):
        nombre = lineas[i]
        valor = int(lineas[i + 1].split(":")[1].strip())
        resultados_esperados[nombre] = valor

    return resultados_esperados
