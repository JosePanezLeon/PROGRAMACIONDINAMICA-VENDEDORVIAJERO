import itertools

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

def calcular_distancia(ruta, distancias):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancias[ruta[i]][ruta[i + 1]]
    distancia_total += distancias[ruta[-1]][ruta[0]] 
    return distancia_total

def tsp_fuerza_bruta(distancias):
    n = len(distancias)
    ciudades = list(range(n))
    ruta_optima = None
    distancia_minima = float('inf')
    
    for ruta in itertools.permutations(ciudades[1:]):  
        ruta_completa = [0] + list(ruta)
        distancia_ruta = calcular_distancia(ruta_completa, distancias)
        if distancia_ruta < distancia_minima:
            distancia_minima = distancia_ruta
            ruta_optima = ruta_completa
    
    return ruta_optima, distancia_minima

n = int(input("Ingrese el número de ciudades: "))
distancias = ingresar_distancias(n)

ruta, distancia = tsp_fuerza_bruta(distancias)
print("Ruta óptima:", ruta)
print("Distancia mínima:", distancia)