import random

# A = Apuesta usada
# M = Monto de entrada
# S = Numero maximo de simulaciones
def juego_simulacion(A, M, S):

    def juego (A, M):
        while True:
            M=M-A
            NumDado = random.randint(1, 6)
            if (NumDado % 2 == 0):
                M=M+(A*2)
            if M <= -100:
                return [M,0]
            if M >= 500:
                return [M,1]

    def resumen_resultados (L):
        for Aux in L:
            if Aux[1] == 1:
                T = "Ganó"
            else:
                T = "Perdió"
            print (str(Aux[0]) + " | " + T)

    def calculo (L):
        V=0
        D=0
        MF=0
        for Aux in L:
            MF=MF+Aux[0]
            if Aux[1] == 0:
                D=D+1
            else:
                V=V+1
        print("No. de Victorias = " + str(V))
        print("No. de Derrotas  = " + str(D))
        print("Monto final  = " + str(MF))
        
    
    Res = []
    i = 0
    while True:
        i=i+1
        Res.append(juego(A, M))
        if i == S:
            break
    resumen_resultados(Res)
    calculo(Res)

juego_simulacion(100,0,50)
