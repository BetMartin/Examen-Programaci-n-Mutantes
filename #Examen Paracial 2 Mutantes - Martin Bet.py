#Examen Paracial 2 Mutantes - Martin Betsabé

#Indicar el procedimiento para iniciar 
print("A continuación se le pedirá que ingrese 6 secuencias de 6 bases nitrogenadas (A,T,C,G).")

#Función para Validar que se ingresen 6 bases nitrogendas
def ValidarBases(lista):
    if (len(lista)==6):
        baseValida=0
        for i in range(0,len(lista)):
            if lista[i].upper()=="A" or lista[i].upper()=="C"or lista[i].upper()=="G"or lista[i].upper()=="T":
                baseValida = baseValida+1
            else:
                break
        if baseValida==6:
            return True
        else:
            print ("Debe ingresar solo bases nitrogenadas (A,T,C o G)")
            return False
    else:
        print("Debe ingresar 6 bases nitrogendas")
        return False

#Función para mostrar matriz ingresada
def MostrarADN(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

#Analizar si existen secuencia de 4 bases iguales consecutivas Horizontal
def esMutanteHorizonal(matriz):
    CantSecuenciaIguales=0
    for i in range(0,6):
        for j in range(0,3):
            basesIguales = True
            baseParaComparar=matriz[i][j]
            for k in range(1,4):
                if baseParaComparar!=matriz[i][j+k]:
                    basesIguales=False
                    break
            if basesIguales==True:
                CantSecuenciaIguales= CantSecuenciaIguales+1
    return CantSecuenciaIguales

#Analizar si existen secuencia de 4 bases iguales consecutivas Vertical
def esMutanteVertical(matriz):
    CantSecuenciaIguales=0
    for i in range(0,6):
        for j in range(0,3):
            basesIguales = True
            baseParaComparar=matriz[j][i]
            for k in range(1,4):
                if baseParaComparar!=matriz[j+k][i]:
                    basesIguales=False
                    break
            if basesIguales==True:
                CantSecuenciaIguales= CantSecuenciaIguales+1
    return CantSecuenciaIguales

#Analizar si existen secuencia de 4 bases iguales consecutivas en Diagonal Abajo
def esMutanteDiagonalAbajo(matriz):
    CantSecuenciaIguales=0
    for i in range(0,3):
        for j in range(0,3):
            basesIguales = True
            baseParaComparar=matriz[j][i]
            for k in range(1,4):
                if baseParaComparar!=matriz[j+k][i+k]:
                    basesIguales=False
                    break
            if basesIguales==True:
                CantSecuenciaIguales= CantSecuenciaIguales+1
    return CantSecuenciaIguales

#Analizar si existen secuencia de 4 bases iguales consecutivas en Diagonal Arriba
def esMutanteDiagonalArriba(matriz):
    CantSecuenciaIguales=0
    for i in range(0,3):
        for j in range(3,6):
            basesIguales = True
            baseParaComparar=matriz[j][i]
            for k in range(1,4):
                if baseParaComparar!=matriz[j-k][i+k]:
                    basesIguales=False
                    break
            if basesIguales==True:
                CantSecuenciaIguales= CantSecuenciaIguales+1
    return CantSecuenciaIguales

#Main
#Crear y solicitar completar la lista de 6 aminoácidos
ListaSecuenciaAminoacido=[]
for i in range(0,6):
    continuar=True
    while continuar == True:
        SecuenciaAminoacido=[]
        print("Secuencia",(i+1),":")
        listaIngresada=input()
        if (ValidarBases(listaIngresada)==True):
            continuar=False
            for i in range(0,len(listaIngresada)):
                SecuenciaAminoacido.append(listaIngresada[i].upper())
            ListaSecuenciaAminoacido.append(SecuenciaAminoacido)
            break
        else:
            continue    

#Mostrar el ADN Ingresado
print("Secuencia de ADN Ingresada: ")
MostrarADN(ListaSecuenciaAminoacido)

#Evaluar si es mutante y dar una respuesta
if (esMutanteHorizonal(ListaSecuenciaAminoacido) + esMutanteVertical(ListaSecuenciaAminoacido) +esMutanteDiagonalAbajo(ListaSecuenciaAminoacido) + esMutanteDiagonalArriba(ListaSecuenciaAminoacido)>1):
    print("ES MUTANTE")
else:
    print("NO ES MUTANTE")

