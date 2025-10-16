#Equipo Castores
#A01564721 - Pablo Talamantes
#A01564754 - Oscar Chavez

#Parte 1
palabra = ["El ingeniero estudia Python.","La carrera es desafiante.", "Python es fundamental en IA."] 
nombre_archivo  = "documento.txt"
with open(nombre_archivo, 'w') as archivo: #escribe los textos al archivo
    for a in palabra:
        archivo.write(a + '\n')

palabra_clave = input("Ingrese palabra clave: ").strip().lower() #no confunde el codigo si pone Python o python 

with open(nombre_archivo, 'r') as archivo:
    for linea in archivo:
        # Verificar si la palabra clave está en la línea (sin distinguir mayúsculas/minúsculas)
        if palabra_clave in linea.lower():
            print(f"Línea encontrada: {linea.strip()}")

            # Preguntar si desea continuar
            continuar = input("¿Desea continuar buscando? (s/n): ").strip().lower() #no confunde si ingresa N o n
            if continuar == 'n':
                print("Búsqueda terminada por el usuario.")
                break
    else:
        # Este bloque se ejecuta si el ciclo for termina sin usar 'break'
        print("Búsqueda terminada. No hay más coincidencias.")