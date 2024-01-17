# %% [markdown]
# # Analizador de texto

# %% [markdown]
# # Este programa recibe una cadena de texto e informa la longitud ( cantidad de caracteres), minusculas, mayusculas y números contenidos, ademas debe ser capaz de:
# - Eliminar espacios en blanco 
# - convertir todo el texto en minusculas
# - convertir todo el texto en mayusculas
# - sustituir una o varias palabras

# %%
cadena = "   Tengo,   sueño   "
cadena_limpia = cadena.strip()

# %%

cadena.strip()

# %%
texto = input("Ingrese el texto")

# %%
texto

# %%
texto = "Hate you"
mayusculas = texto.upper()
minusculas = texto.lower()

# %%
print(mayusculas)

# %%
print(minusculas)

# %%
cadena = input("Ingrese el texto")
# Eliminar espacios en blanco
texto_sin_espacios = texto.replace(" ", "")

    # Convertir a mayúsculas y minúsculas
mayusculas = cadena.upper()
minusculas = cadena.lower()

    # Sustituir una palabra (ejemplo: sustituir "hola" por "adiós")
cadena_sustituida = cadena.replace("mala", "buena")



# %%
print(mayusculas)

# %%
cadena = input ("Ingrese una cadena")
palabra_reemplazo = input("Ingrese que palabra desea remplazar")
palabra = input("Ingrese la palabra de reemplazo")
cadena_f = cadena.replace(palabra_reemplazo,palabra)
print(cadena)
print(cadena_f)
#jhguiygi6fu7gt
cadena =cadena   
longitud = len(cadena)
print(longitud)
#fghh
cadena =cadena_f
longitud = len(cadena)
print(longitud)

#utgoi7tgo8
mayusculas = cadena.upper()
minusculas = cadena.lower()
print(mayusculas)
print(minusculas)
 

 #gujiuyi
cadena = cadena
cadena_limpia = cadena.strip()
cadena.strip()

# %%
cadena

# %%
cadena_f

# %%
cadena = input("Ingrese una cadena: ")
palabra_reemplazo = input("Ingrese la palabra que desea reemplazar: ")
palabra = input("Ingrese la palabra de reemplazo: ")

cadena_f = cadena.replace(palabra_reemplazo, palabra)

print("Cadena original:", cadena)
print("Cadena modificada:", cadena_f)

longitud_original = len(cadena)
print("Longitud de la cadena original:", longitud_original)

longitud_modificada = len(cadena_f)
print("Longitud de la cadena modificada:", longitud_modificada)

mayusculas = cadena_f.upper()
minusculas = cadena_f.lower()

print("Cadena en mayúsculas:", mayusculas)
print("Cadena en minúsculas:", minusculas)

cadena_limpia = cadena_f.strip()
print("Cadena limpia:", cadena_limpia)

# %%
def obtener_informacion(cadena):
    cantidad_total = len(cadena)
    cantidad_minusculas = sum(1 for char in cadena if char.islower())
    cantidad_mayusculas = sum(1 for char in cadena if char.isupper())
    cantidad_numericos = sum(1 for char in cadena if char.isdigit())

    print("Información:")
    print(f"Cadena de texto: {cadena}")
    print(f"Cantidad total de caracteres: {cantidad_total}")
    print(f"Cantidad de caracteres en minúscula: {cantidad_minusculas}")
    print(f"Cantidad de caracteres en mayúscula: {cantidad_mayusculas}")
    print(f"Cantidad de caracteres numéricos: {cantidad_numericos}")

def eliminar_espacios(cadena):
    return cadena.replace(" ", "")

def mostrar_menu():
    print("Convertir cadena a mayúsculas")

def mostrar_menu():
    print("Convertir cadena a minúsculas")

def sustituir_palabra(cadena):
    palabra_original = input("Ingrese la palabra original: ")
    palabra_nueva = input("Ingrese la palabra nueva: ")
    return cadena.replace(palabra_original, palabra_nueva)


def menu():
    cadena = input("Ingrese una cadena de texto: ")

    print("\n1. Mostrar información sobre la cadena")
    print("2. Eliminar espacios en blanco")
    print("3. Cadena en mayúsculas")
    print("4. Cadena en minúsculas")
    print("5. Sustituir palabra")
    print("6. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")

    if opcion == "1":
        obtener_informacion(cadena)
    elif opcion == "2":
        cadena_sin_espacios = eliminar_espacios(cadena)
        print(f"\nCadena sin espacios: {cadena_sin_espacios}")
    elif opcion == "3":
            if cadena:
                print("Cadena en mayúsculas:", cadena.upper())
    elif opcion == "4":
            if cadena:
                print("Cadena en minúsculas:", cadena.lower())
    elif opcion == "5":
            if cadena:
                cadena = sustituir_palabra(cadena)
                print("Cadena con palabra sustituida:", cadena)
    
    elif opcion == "6":
        print("¡Hasta luego!")

    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        menu()

menu()


