import random

# A = Apuesta usada
# M = Monto de entrada
# S = Numero maximo de simulaciones
# R = Numero maximo de rondas por cada simulacion
def juego_simulacion(A, M, S):

    def juego(A, M):
        i = 0
        while True:
            M=M-A
            NumDado = random.randint(1, 6)
            if (NumDado % 2 == 0):
                M=M+(A*2)
            if (M <= -100 or M >= 500 or i == 200):
                return M

    def contador_resultados(L):
        Victorias=0
        Derrotas=0
        Total=0
        p=0
        while True:
            p= L.pop(0)
            if p <= -100:
                Derrotas=Derrotas+1
            if p >= 500:
                Victorias=Victorias+1
            if L == []:
                break
        Total = Victorias + Derrotas
        R = []
        PorcentajeV = 100 * (Victorias/Total)
        PorcentajeD = 100 * (Derrotas/Total)
        return [PorcentajeV, PorcentajeD]
    
    
    i=0
    lista_resultados=[]
    while True:
        i=i+1
        lista_resultados.append(juego(A,M))
        if i == S:
            break
    print(lista_resultados)
    resultado_porcentajes = contador_resultados(lista_resultados)
    print("% de Victorias = "+ str(resultado_porcentajes.pop(0)))
    print("% de Derrotas = "+ str(resultado_porcentajes.pop(0)))

print("para jugar inserte los siguientes valores:")
while True:
    print("Apuesta usada (minimo 5$):")
    Apuesta = int(input())
    if Apuesta >= 5:
        break
    else:
        print("ERROR: el minimo es 5$")
print("Monto inicial:")
MontoIni = int(input())
print("Numero maximo de simulaciones:")
MaxSim = int(input())
juego_simulacion(Apuesta,MontoIni,MaxSim)
