def insertar_ordenado(lista_ordenada, numero):
    """
    Inserta 'numero' en la posición correcta de 'lista_ordenada'
    para mantener el orden ascendente.
    """
    if not lista_ordenada:
        lista_ordenada.append(numero)
        return
    
    for i in range(len(lista_ordenada)):
        if lista_ordenada[i] >= numero:
            lista_ordenada.insert(i, numero)
            return
    
    # Si es mayor que todos, va al final
    lista_ordenada.append(numero)


def ordenar_con_insercion(numeros):
    """
    Crea una lista ordenada insertando uno por uno los números
    de la lista original.
    """
    ordenada = []
    for num in numeros:
        insertar_ordenado(ordenada, num)
    return ordenada


def main():
    print("=== NumberSorter - Ordenador por inserción ===\n")
    
    while True:
        entrada = input("Ingresa números separados por coma (o 'salir'): ").strip()
        
        if entrada.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if not entrada:
            print("Entrada vacía. Intenta de nuevo.\n")
            continue
        
        try:
            # Convertir entrada a lista de enteros
            numeros = [int(x.strip()) for x in entrada.split(',')]
            
            print("\nNúmeros ingresados (desordenados):")
            print(numeros)
            
            # Ordenar usando inserción
            lista_ordenada = ordenar_con_insercion(numeros)
            
            print("\nLista ordenada (por inserción):")
            print(lista_ordenada)
            
            # Mostrar también la versión de Python para comparación
            print("\n(Para comparación - sorted de Python):")
            print(sorted(numeros))
            
        except ValueError:
            print("Error: Ingresa solo números enteros separados por comas.\n")
        except Exception as e:
            print(f"Error inesperado: {e}\n")


if __name__ == "__main__":
    main()
