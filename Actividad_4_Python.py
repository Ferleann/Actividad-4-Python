maxf = 3
maxc = 3

def impresion(a):
    print("Los valores de la matriz son:\n")
    for f in range(maxf):
        for c in range(maxc):
            print(a[f][c], end=" ")
        print("\n")
    print()

def captura_arreglo(a):
    for f in range(maxf):
        for c in range(maxc):
            print("Ingrese el valor para la posicion ["+str(f)+"]["+str(c)+"]: \n")
            a[f][c] = float(input())
    return a

def main():
    arreglo_bidimensional = [[0] * maxc for _ in range(maxf)]
    print("Captura de valores a una Matriz NxM\n\n")
    print("Arreglo Bidimensional\n")
    matriz_resultado = captura_arreglo(arreglo_bidimensional)
    impresion(matriz_resultado)

if __name__ == "__main__":
    main()
