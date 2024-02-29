def magia_numerica(lista):
    # Copia la lista para no modificar la original
    lista_copiada = lista.copy()
    
    # Elimina los elementos duplicados
    lista_sin_duplicados = list(set(lista_copiada))
    
    # Ordena la lista de mayor a menor
    lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
    
    # Elimina todos los números impares
    lista_pares = [num for num in lista_ordenada if num % 2 == 0]
    
    # Suma todos los números que quedan
    suma_total = sum(lista_pares)
    
    # Coloca la suma como el primer elemento de la lista
    lista_final = [suma_total] + lista_pares
    
    return lista_final

# Ejemplo de uso
lista_original = [3, 7, 2, 8, 5, 2, 9, 8, 6, 3]
resultado = magia_numerica(lista_original)
print(resultado)
