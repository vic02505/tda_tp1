import csv

def leer_batallas(path_del_archivo: str) -> list[tuple[int, int]]:
    datos_de_batallas = []

    with open(path_del_archivo, mode="r", newline="") as archivo_a_procesar:
        reader = csv.reader(archivo_a_procesar)
        next(reader)
        for linea in reader:
            if linea:
                tiempo, peso = map(int, linea)
                datos_de_batallas.append((tiempo, peso))

    return datos_de_batallas

