class MagiaNumerica:
    def __init__(self, lista):
        self.lista = lista.copy()

    def eliminar_duplicados(self):
        self.lista = list(set(self.lista))

    def ordenar_decreciente(self):
        self.lista.sort(reverse=True)

    def eliminar_impares(self):
        self.lista = [num for num in self.lista if num % 2 == 0]

    def sumar_elementos(self):
        return sum(self.lista)

    def obtener_resultado(self):
        self.eliminar_duplicados()
        self.ordenar_decreciente()
        self.eliminar_impares()
        suma_total = self.sumar_elementos()
        lista_final = [suma_total] + self.lista
        return lista_final


def main():
    lista_original = [3, 7, 2, 8, 5, 2, 9, 8, 6, 3]
    magia = MagiaNumerica(lista_original)
    resultado = magia.obtener_resultado()
    print(resultado)


if __name__ == "__main__":
    main()
