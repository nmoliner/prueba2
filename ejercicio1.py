import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def galaxia(self):
        if self.x > 0:
            if self.y > 0:
                if self.z > 0:
                    return "Vía Láctea"
                else:
                    return "Galaxia de Andrómeda"
            else:
                return "Galaxia del Triángulo"
        else:
            if self.y > 0:
                if self.z > 0:
                    return "Galaxia del Sombrero"
                else:
                    return "Galaxia del Remolino"
            else:
                return "Galaxia enana de Sagitario"
    
    def distancia(self, otra_estrella):
        distancia_x = (otra_estrella.x - self.x) ** 2
        distancia_y = (otra_estrella.y - self.y) ** 2
        distancia_z = (otra_estrella.z - self.z) ** 2
        distancia_total = math.sqrt(distancia_x + distancia_y + distancia_z)
        return distancia_total

# Ejemplo de uso
estrella1 = Estrella(1, 2, 3)
estrella2 = Estrella(4, 5, 6)
print("Estrella 1:", estrella1)
print("Estrella 2:", estrella2)
print("Galaxia de la Estrella 1:", estrella1.galaxia())
print("Distancia entre Estrella 1 y Estrella 2:", estrella1.distancia(estrella2))



# Crear las estrellas
estrella_A = Estrella(2, 3, 1)
estrella_B = Estrella(4, 4, 4)
estrella_C = Estrella(-3, -1, 0)

# Imprimir las estrellas por pantalla
print("Coordenadas de las estrellas:")
print("Estrella A:", estrella_A)
print("Estrella B:", estrella_B)
print("Estrella C:", estrella_C)

# Determinar en qué galaxias podrían estar las estrellas
print("\nGalaxias en las que podrían estar las estrellas:")
print("Estrella A:", estrella_A.galaxia())
print("Estrella B:", estrella_B.galaxia())
print("Estrella C:", estrella_C.galaxia())

# Calcular y mostrar la distancia entre las estrellas A y B, y entre B y C
distancia_AB = estrella_A.distancia(estrella_B)
distancia_BC = estrella_B.distancia(estrella_C)
print("\nDistancias entre las estrellas:")
print("Distancia entre A y B:", distancia_AB)
print("Distancia entre B y C:", distancia_BC)


# Calcular la distancia de cada estrella al origen
distancia_origen_A = estrella_A.distancia(Estrella())
distancia_origen_B = estrella_B.distancia(Estrella())
distancia_origen_C = estrella_C.distancia(Estrella())

# Encontrar qué estrella está más lejos del origen
estrella_mas_lejos = max([(distancia_origen_A, 'A'), (distancia_origen_B, 'B'), (distancia_origen_C, 'C')])

print("\nEstrella más lejana al origen:", estrella_mas_lejos[1])
