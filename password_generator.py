import itertools
import random

# Lista de palabras base
palabras_base = ["seguridad", "criptografia", "password", "hashing"]

# Lista de símbolos especiales
simbolos = ['@', '#', '$', '%', '&', '!', '*', '+']

# Generar combinaciones simples (con y sin símbolos)
def generar_combinaciones(palabras, max_longitud=16):
    combinaciones = []
    
    # Crear todas las permutaciones posibles entre 2 y 4 palabras
    for r in range(2, len(palabras) + 1):
        for combinacion in itertools.permutations(palabras, r):
            # Combinar las palabras y agregarla a la lista
            contraseña = ''.join(combinacion)
            if len(contraseña) <= max_longitud:
                combinaciones.append(contraseña)
            
            # Agregar un símbolo al azar en una posición aleatoria
            if len(contraseña) + 1 <= max_longitud:
                for simbolo in simbolos:
                    pos = random.randint(0, len(contraseña))
                    contraseña_simbolo = contraseña[:pos] + simbolo + contraseña[pos:]
                    combinaciones.append(contraseña_simbolo)
    
    return combinaciones

# Generar combinaciones con cambios de mayúsculas y minúsculas
def cambiar_mayusculas(contraseñas):
    combinaciones_mayus = []
    for contraseña in contraseñas:
        # Cambiar aleatoriamente mayúsculas y minúsculas en la contraseña
        combinacion = ''.join(random.choice([c.lower(), c.upper()]) for c in contraseña)
        combinaciones_mayus.append(combinacion)
    return combinaciones_mayus

# Generar el diccionario de contraseñas
contraseñas_generadas = generar_combinaciones(palabras_base)
contraseñas_con_mayus = cambiar_mayusculas(contraseñas_generadas)

# Unir todas las combinaciones en una lista final y eliminar duplicados
diccionario_final = list(set(contraseñas_generadas + contraseñas_con_mayus))

# Mostrar las primeras 10 contraseñas generadas para ejemplo
for i, contraseña in enumerate(diccionario_final[:10]):
    print(f"Contraseña {i+1}: {contraseña}")

# Guardar en un archivo de texto si lo deseas
with open("diccionario_contraseñas.txt", "w") as f:
    for contraseña in diccionario_final:
        f.write(contraseña + "\n")

print(f"Se generaron {len(diccionario_final)} contraseñas en el diccionario.")
