# Generador de Contraseñas Seguras

Este programa genera una lista de contraseñas utilizando palabras clave y símbolos aleatorios. Además, incluye variaciones en mayúsculas y minúsculas para aumentar la seguridad. Puede ser útil para generar diccionarios personalizados de contraseñas o simplemente para obtener contraseñas únicas y seguras.

### Funcionalidades

-**Generación de contraseñas basadas en una lista de palabras clave.
-**Incorporación de símbolos especiales en ubicaciones aleatorias dentro de la contraseña.
-**Cambio de mayúsculas y minúsculas de manera aleatoria para aumentar la diversidad de contraseñas.
-**Opciones personalizables, como la longitud máxima de las contraseñas generadas.
-**Exportación de contraseñas a un archivo de texto (diccionario_contraseñas.txt).

### Ejemplo de Uso

Al ejecutar el programa, se generará una lista de contraseñas basadas en combinaciones de las siguientes palabras clave:

-**seguridad
-**criptografia
-**password
-**hashing

Las contraseñas también pueden contener los siguientes símbolos especiales: @, #, $, %, &, !, *, +.

Aquí un ejemplo de las primeras contraseñas generadas:

Contraseña 1: hashingCriptografia
Contraseña 2: criptografia%password
Contraseña 3: seguridadPassword
Contraseña 4: password#Criptografia

# ¿Cómo Funciona?
-**Generación de Combinaciones: Se generan permutaciones de las palabras clave, asegurándose de que no superen la longitud máxima permitida (16 caracteres por defecto).
-**Incorporación de Símbolos: Se añaden símbolos aleatorios a las contraseñas generadas.
-**Mayúsculas y Minúsculas: Cada contraseña es transformada aleatoriamente para mezclar mayúsculas y minúsculas.
-**Exportación: Todas las contraseñas generadas se guardan en el archivo diccionario_contraseñas.txt sin duplicados.

# Requisitos

Este programa no requiere la instalación de ninguna librería adicional. Solo necesitas tener instalado Python 3.x.

# Uso

Puedes ejecutar el programa con el siguiente comando:


-**python generador_contraseñas.py

El programa generará una lista de contraseñas que se guardarán en un archivo llamado diccionario_contraseñas.txt.

-**Personalización

Si deseas cambiar la lista de palabras clave o los símbolos utilizados, solo necesitas editar las siguientes variables dentro del código:

-**Lista de palabras clave: Modifica la variable palabras_base.
-**Símbolos especiales: Modifica la variable simbolos.
-**Longitud máxima de las contraseñas: Cambia el valor de max_longitud dentro de la función generar_combinaciones.

# Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el programa o deseas corregir algún error, no dudes en hacer un fork del proyecto y enviar un pull request.

