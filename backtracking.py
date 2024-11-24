def tsp_programacion_dinamica(distancias):
    n = len(distancias)
    memo = {}
    camino = {}

def Pdinamica(ciudad_actual, ciudades_visitadas):
        
        if ciudades_visitadas == (1 << n) - 1:
            return distancias[ciudad_actual][0]
        if (ciudad_actual, ciudades_visitadas) in memo:
            return memo[(ciudad_actual, ciudades_visitadas)]
        min_distancia = float('inf')
        siguiente_ciudad_optima = -1
        for siguiente_ciudad in range(n):
            if not (ciudades_visitadas & (1 << siguiente_ciudad)):
                nueva_distancia = distancias[ciudad_actual][siguiente_ciudad] + Pdinamica(siguiente_ciudad, ciudades_visitadas | (1 << siguiente_ciudad))
                if nueva_distancia < min_distancia:
                    min_distancia = nueva_distancia
                    siguiente_ciudad_optima = siguiente_ciudad
        memo[(ciudad_actual, ciudades_visitadas)] = min_distancia
        camino[(ciudad_actual, ciudades_visitadas)] = siguiente_ciudad_optima
        return min_distancia
    distancia_minima = Pdinamica(0, 1)

    ruta_optima = []
    ciudades_visitadas = 1
    ciudad_actual = 0
    for _ in range(n - 1):
        ruta_optima.append(ciudad_actual)
        ciudad_actual = camino[(ciudad_actual, ciudades_visitadas)]
        ciudades_visitadas |= (1 << ciudad_actual)
    ruta_optima.append(ciudad_actual)  
    ruta_optima.append(0)  

    return distancia_minima, ruta_optima

def ingresar_distancias(n):
    distancias = []
    print("Ingresa las distancias entre las ciudades (si no hay conexión, ingresa una distancia alta):")
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(0)  
            else:
                distancia = float(input(f"Distancia de la ciudad {i} a la ciudad {j}: "))
                fila.append(distancia)
        distancias.append(fila)
    return distancias

n = int(input("Ingrese el número de ciudades: "))
distancias = ingresar_distancias(n)

distancia, ruta = tsp_programacion_dinamica(distancias)
print("Distancia mínima para recorrer todas las ciudades y volver a la ciudad de origen:", distancia)
print("Ruta óptima:", ruta)
