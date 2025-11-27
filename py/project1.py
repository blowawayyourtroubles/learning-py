# ═══════════════════════════════════════════════════════════════════
# ! 📚 COLECCIÓN DE EJERCICIOS PYTHON - ORGANIZADOS POR DIFICULTAD
# ═══════════════════════════════════════════════════════════════════
# * Archivo de práctica con ejercicios desde principiante hasta intermedio
# * Cada sección está comentada para poder ejecutar ejercicios individualmente
# ═══════════════════════════════════════════════════════════════════


# ╔═══════════════════════════════════════════════════════════════════╗
# ║                    NIVEL 1: PRINCIPIANTE                          ║
# ║                 Fundamentos Básicos de Python                     ║
# ╚═══════════════════════════════════════════════════════════════════╝


# ─────────────────────────────────────────────────────────────────────
# * 1.1 VARIABLES Y TIPOS DE DATOS BÁSICOS
# ─────────────────────────────────────────────────────────────────────

# ? Ejercicio: Variables numéricas simples
# x = 7
# y = 20
# z = 2
# print(y / z)  # División básica

# ? Ejercicio: Operaciones aritméticas básicas
# a = 3.5 - 1.5
# print(a)

# ? Ejercicio: Múltiples asignaciones en una línea
# x = 7; y = 20; z = 2
# c = 0
# c = x - z
# c = c + 1
# print(c)


# ─────────────────────────────────────────────────────────────────────
# * 1.2 VERIFICACIÓN DE TIPOS DE DATOS
# ─────────────────────────────────────────────────────────────────────

# ? Ejercicio: Identificar tipo de dato con type()
# num1 = 5
# num2 = 54
# which_type = type(num1)
# 
# if which_type == float:
#     print(f"The number {num1} is a float.")
# else:
#     print(f"The number {num1} is an int.")


# ─────────────────────────────────────────────────────────────────────
# * 1.3 STRINGS - MANIPULACIÓN BÁSICA
# ─────────────────────────────────────────────────────────────────────

# ? Ejercicio: Concatenación simple con +
# name = "German "
# lastName = "Gibbs"
# print(name + lastName)

# ? Ejercicio: Concatenación con operador +=
# firstName = "German "
# firstName += "Gibbs Florian"
# print(firstName)

# ? Ejercicio: Escape de caracteres en strings
# print('hello, "friend"')        # Comillas dobles dentro de simples
# print("hello, \"friend\"")      # Escape con backslash

# ? Ejercicio: Método replace() para modificar strings
# oracion = " Programming is fun "
# print(f"Replace(): '{oracion.replace('fun', 'cool')}'")


# ─────────────────────────────────────────────────────────────────────
# * 1.4 INPUT DEL USUARIO - BÁSICO
# ─────────────────────────────────────────────────────────────────────

# ? Ejercicio: Input con conversión de tipo
# name = input("What's your name? ")
# age = int(input("How old are you? "))
# print(f"Hello {name}, next year you will be {age + 1} years old.")

# ! IMPORTANTE: Input avanzado con encadenamiento de métodos
# * Prompt the user for their name using two functions chained
# inputQuestion = input("What's your name? ").strip().title()

# * Different ways to greet the user:
# print(f"Hello, {inputQuestion}")                    # F-string (RECOMENDADO)
# print("Hello, " + inputQuestion)                  # Concatenación con +
# print("Hello,", inputQuestion)                    # Comma-separated (añade espacio automático)
# print("Hello, ", inputQuestion, end="")           # Sin salto de línea al final


# ╔═══════════════════════════════════════════════════════════════════╗
# ║                NIVEL 2: PRINCIPIANTE-INTERMEDIO                   ║
# ║                    Control de Flujo Básico                        ║
# ╚═══════════════════════════════════════════════════════════════════╝


# ─────────────────────────────────────────────────────────────────────
# * 2.1 CONDICIONALES SIMPLES (IF/ELSE)
# ─────────────────────────────────────────────────────────────────────

# ? Ejercicio: Comparación de números
# numero = 32
# numero_entero = int(numero)
# 
# if numero_entero > 50:
#     print(f"{numero_entero} es grande")
# else:
#     print(f"Tu {numero} es muy pequeño")

# ? Ejercicio: Comparación entre dos valores
# val1 = 8
# val2 = 32
# 
# if val1 >= val2:
#     print(f"El {val1} es mayor que {val2}")
# else:
#     print(f"El {val2} es mayor")


# ─────────────────────────────────────────────────────────────────────
# * 2.2 OPERADORES LÓGICOS Y DE COMPARACIÓN
# ─────────────────────────────────────────────────────────────────────

# ? Ejercicio: Operadores de comparación (==, >, >=)
# first_user = 23
# second_user = 26

# are_equal = first_user == second_user
# is_greater = first_user > second_user
# is_greater_equal = first_user >= second_user


# if are_equal == True:{
#      print(f"the {first_user} is greater or equal than the {second_user}.")
# } 
# else: {
#      print("The numbers are not equal.")
#  }


# ? Ejercicio: Operador lógico AND
# firstCase = True
# secondCase = True
# print((firstCase and secondCase))  # Retorna True porque ambos son True

# ? Ejercicio: Operador lógico OR
# condition1 = False
# condition2 = True
# print((condition2 or condition1))  # Retorna True si al menos uno es True


# ─────────────────────────────────────────────────────────────────────
# * 2.3 OPERADOR TERNARIO (CONDITIONAL EXPRESSION)
# ─────────────────────────────────────────────────────────────────────

# ? Ejercicio: Verificar si un número es par o impar
# n = 4
# res = "Even" if n % 2 == 0 else "Odd"
# print(res)

# ? Ejercicio: Función con operador ternario
# def esMayorDeEdad(edad):
#     return True if edad > 18 else False
# 
# miEdad = 17
# print(esMayorDeEdad(miEdad))


# ╔═══════════════════════════════════════════════════════════════════╗
# ║                      NIVEL 3: INTERMEDIO                          ║
# ║              Bucles y Estructuras de Datos                        ║
# ╚═══════════════════════════════════════════════════════════════════╝


# ─────────────────────────────────────────────────────────────────────
# * 3.1 BUCLES FOR CON LISTAS
# ─────────────────────────────────────────────────────────────────────

# ? Ejercicio: Iterar sobre una lista de nombres
# nombres = ["Anna", "Tom", "Karinna"]
# 
# for nombre in nombres:
#     print(f"¡Hola! {nombre}")


# ─────────────────────────────────────────────────────────────────────
# * 3.2 FUNCIONES CONDICIONALES AVANZADAS
# ─────────────────────────────────────────────────────────────────────

# ? Ejercicio: Conversor de formato 24h a 12h
# * Esta función convierte hora en formato 24h a 12h con AM/PM
# def converted_to_12hr(time_24hr_str):
#     time_24hr_str = "14"
#     minute_str = "55"
#     
#     hour_int = 14
#     converted_hour = 0
#     suffix = ""
#     
#     if hour_int == 0:  # ! Regla de medianoche: 00:xx se convierte en 12:xx AM
#         converted_hour = 12
#         suffix = "AM"
#     
#     elif hour_int >= 13:  # * Tarde: Resta 12 para formato 12h
#         converted_hour = hour_int - 12
#         suffix = "PM"
#     
#     elif hour_int == 12:  # ! Mediodía: Se mantiene como 12
#         converted_hour = 12
#         suffix = "PM"
#     
#     else:  # * Mañana: Se mantiene igual
#         converted_hour = hour_int
#         suffix = "AM"
#     
#     return f"{converted_hour}:{minute_str} {suffix}"


# ╔═══════════════════════════════════════════════════════════════════╗
# ║                  NIVEL 4: PROYECTOS COMPLETOS                     ║
# ║              Aplicaciones Interactivas Funcionales                ║
# ╚═══════════════════════════════════════════════════════════════════╝


# ─────────────────────────────────────────────────────────────────────
# ! 4.1 PROYECTO: JUEGO MAD LIBS
# ─────────────────────────────────────────────────────────────────────
# * Juego interactivo que genera historias personalizadas

# print("--- ¡Bienvenido al juego Mad Libs! Dame los ingredientes para la historia. ---\n")
# 
# # * Solicitar inputs al usuario
# color = input("1. Dame un color: ")
# nombre = input("2. Dame un nombre de una celebridad: ")
# adjetivo = input("3. Dame un adjetivo: ")
# numero = input("4. Dame un número (entero): ")
# lugar = input("5. Dame un lugar (tu ciudad): ")
# 
# # * Usar f-string para crear la historia con las variables
# historia_final = f"""
# --- ¡TU HISTORIA! ---
# El {adjetivo} {color} {nombre} estaba en {lugar}.
# De repente, apareció un gigante muy {adjetivo}.
# El gigante le preguntó a {nombre}: "¿Sabes dónde están mis {numero} manzanas?"
# """
# 
# print(historia_final)


# ─────────────────────────────────────────────────────────────────────
# ! 4.2 PROYECTO: CALCULADORA BÁSICA
# ─────────────────────────────────────────────────────────────────────
# * Calculadora de 4 operaciones con validación de división por cero

# operador = input("Elija la operación deseada (+, -, *, /): ")
# num1 = float(input("Dame un número: "))
# num2 = float(input("Dame otro número: "))
# 
# if operador == "+":
#     print(f"Resultado: {num1 + num2}")
# 
# elif operador == "-":
#     print(f"Resultado: {num1 - num2}")
# 
# elif operador == "*":
#     print(f"Resultado: {num1 * num2}")
# 
# elif operador == "/":
#     if num2 != 0:  # ! IMPORTANTE: Validar división por cero
#         print(f"Resultado: {num1 / num2}")
#     else:
#         print("Error: No se puede dividir entre cero")
# 
# else:
#     print("Error: Operador no conocido. Utilice +, -, * o /")


#* Calculator


# ─────────────────────────────────────────────────────────────────────
# ! 4.3 PROYECTO: SISTEMA DE ENTRADA CON VALIDACIÓN
# ─────────────────────────────────────────────────────────────────────
# * Captura edad y monto con conversión de tipos y formato

# # * El usuario debe escribir valores numéricos que se convierten automáticamente
# age = int(input("Ingresa tu edad: "))
# total_amount = float(input("Ingresa el total de la compra: "))
# 
# # * Mostrar con formato profesional (2 decimales para dinero)
# print(f"Edad: {age} años, Total: ${total_amount:.2f}")

# ─────────────────────────────────────────────────────────────────────
# * 3.1 CREAR FUNCIONES
# ─────────────────────────────────────────────────────────────────────

def hello(inputName):{
     print("Hello,", inputName)
}
     
name = input("What's your name? ")
hello(name)   


# TODO 


# ╔═══════════════════════════════════════════════════════════════════╗
# ║                  PROYECTOS EN DESARROLLO                          ║
# ║                    (Pendientes de Completar)                      ║
# ╚═══════════════════════════════════════════════════════════════════╝


# ─────────────────────────────────────────────────────────────────────
# TODO: PROYECTO INCOMPLETO - SELECTOR DE GÉNERO MUSICAL
# ─────────────────────────────────────────────────────────────────────
# * Sistema para verificar si un género musical está en la lista

# likesMusic = input("Choose your favorite genre: ")
# 
# def checkMusicGenre(music):
#     """
#     * Verifica si el género musical ingresado está en la lista
#     ? Parámetros: music (str) - Género a verificar
#     ! Retorna: bool - True si existe, False si no
#     """
#     musicGenres = ["rock", "salsa", "hip-hop", "merengue", "metal"]
#     return music.lower() in musicGenres
# 
# result = checkMusicGenre(likesMusic)
# if result:
#     print(f"✅ ¡{likesMusic} es un gran género!")
# else:
#     print(f"❌ {likesMusic} no está en nuestra lista")


# ═══════════════════════════════════════════════════════════════════
# * 📊 RESUMEN DE CONCEPTOS PRACTICADOS
# ═══════════════════════════════════════════════════════════════════
# 
# ! CONCEPTOS FUNDAMENTALES CUBIERTOS:
# ✅ Variables y tipos de datos (int, float, str, bool)
# ✅ Operadores aritméticos (+, -, *, /, //)
# ✅ Operadores de comparación (==, >, <, >=, <=, !=)
# ✅ Operadores lógicos (and, or, not)
# ✅ Condicionales (if, elif, else)
# ✅ Operador ternario (expresiones condicionales)
# ✅ Bucles for
# ✅ Listas y iteración
# ✅ Funciones básicas y con parámetros
# ✅ Input del usuario con conversión de tipos
# ✅ Manipulación de strings (strip, title, capitalize, replace)
# ✅ F-strings para formateo
# ✅ Encadenamiento de métodos (method chaining)
# ✅ Validación de datos (división por cero)
# 
# ? PROYECTOS COMPLETADOS:
# 1. ✅ Juego Mad Libs interactivo
# 2. ✅ Calculadora de 4 operaciones
# 3. ✅ Sistema de conversión de tiempo 24h → 12h
# 4. ✅ Validadores de edad y valores
# 
# TODO: PRÓXIMOS PASOS:
# - Agregar manejo de excepciones (try/except)
# - Implementar bucles while
# - Crear funciones con múltiples parámetros
# - Trabajar con diccionarios
# - Implementar programación orientada a objetos básica
# 
# ═══════════════════════════════════════════════════════════════════


# ╔═══════════════════════════════════════════════════════════════════╗
# ║                      NOTAS DEL DESARROLLADOR                      ║
# ╚═══════════════════════════════════════════════════════════════════╝
# 
# * ESTRUCTURA DEL ARCHIVO:
# - Código organizado por niveles de dificultad (1-4)
# - Comentarios usando Better Comments extension
# - Ejercicios comentados para evitar ejecución simultánea
# 
# ! CÓMO USAR ESTE ARCHIVO:
# 1. Descomenta el bloque de código que quieras ejecutar
# 2. Ejecuta el archivo con: python nombre_archivo.py
# 3. Vuelve a comentar después de practicar
# 
# ? LEYENDA DE COMENTARIOS (Better Comments):
# * Información importante o explicaciones
# ! Alertas, advertencias o puntos críticos
# ? Preguntas o aclaraciones sobre el código
# TODO: Tareas pendientes o código por completar
# 
# ═══════════════════════════════════════════════════════════════════