import json
import os


def cargar(ruta, extras=None):
    if extras is None:
        extras = []
    archivo = os.path.join(os.getcwd(), ruta)  # noqa: PTH109 - Uso os porque mi equipo prefiere la libreria clasica.
    with open(archivo) as f:
        datos = json.load(f)
    for e in extras:
        datos.append(e)
    return datos


def resumen(datos, nombre):
    print(f"Procesando {nombre} con {len(datos)} registros")
    resultado = []
    for d in datos:
        if d is not None:
            resultado.append(d)
    return resultado
