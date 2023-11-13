# Examen Parcial 2 - Mutantes
- Nombre y Apellido: Martin, Betsabé
- Legajo: 811192
- Email: betsabemartin@gmail.com

## Aspectos solicitados en el proyecto Mutantes
El presente programa permite detectar secuencias de ADN de Mutantes de los que no lo son. Teniendo en cuenta que:
- La secunecia de ADN contiene 6 secuencias de 6 Bases Nitrogenadas cada una (A, T, C y G).
- El ingreso de las secuencias se realizan por fila, siendo ingresadas por el usuario.
- Los casos mutantes son aquellos que presentan mas de dos secuencias de Bases nitrogenadas iguales consecutivas, presentadas de modo Horizontal, vertical u oblicuo.

## Solución propuesta
Para la resolución del mismo se propone el desarrollo del siguiente proceso:
1. Solicitud de ingreso de la secuencia de ADN, ingresando 6 string de 6 caracteres
2. Validación de la secuencia ingresada. Para se creó la siguiente fucnión:

    ``` 
    def ValidarBases(lista) 
    ```

    **NOTA:** Valida que el String ingresado contenga 6 caracteres y que esos caracteres correspondan solo a bases nitrogenadas (A, T, C o G)
3. Construcción de una matriz con los datos ingresados. Para mostrar por pantalla la secuencia de ADN ingresada se desarrolló la siguente función:

    ```
    def MostrarADN(matriz)
    ```

4. Seguidamente se procedió a realizar un recorrido por la matriz para buscar secuencia de 4 bases nitrogenadas consecutivas iguales. Para ello se crearon 4 funciones:
    ```
    #Analizar si existen secuencia de 4 bases iguales consecutivas Horizontal
    def esMutanteHorizonal(matriz):

    #Analizar si existen secuencia de 4 bases iguales consecutivas Vertical
    def esMutanteVertical(matriz):

    #Analizar si existen secuencia de 4 bases iguales consecutivas en Diagonal Abajo
    def esMutanteDiagonalAbajo(matriz):

    #Analizar si existen secuencia de 4 bases iguales consecutivas en Diagonal Arriba
    def esMutanteDiagonalArriba(matriz):
    ```
5. Finalmente se corrobora que existan las condiciones solicitadas para definir si es mutante o no. Y se retorna el resultado mediante el siguiente condicional:
    ```
    if (esMutanteHorizonal(ListaSecuenciaAminoacido) + esMutanteVertical(ListaSecuenciaAminoacido) +esMutanteDiagonalAbajo(ListaSecuenciaAminoacido) + esMutanteDiagonalArriba(ListaSecuenciaAminoacido)>1):
        print("ES MUTANTE")
    else:
        print("NO ES MUTANTE")
    ```
## Comenzando
Se puede acceder desde el **GitHub CLI** ingresando clonando el repositario, una vez intalado se puede correr en el ambiente local

```
gh repo clone BetMartin/Examen-Programacion-Mutantes
```
De otro modo, puedes acceder a desde el siguiente [enlace](https://github.com/BetMartin/Examen-Programacion-Mutantes.git) y descargarlo y ejecutarlo.

## Casos de Prueba
### Ejemplo 1

    A continuación se le pedirá que ingrese 6 secuencias de 6 bases nitrogenadas (A,T,C,G).
    Secuencia 1 :
    ttgcga
    Secuencia 2 :
    aagtgc
    Secuencia 3 :
    ttattt
    Secuencia 4 :
    agatgg
    Secuencia 5 :
    gcgtca
    Secuencia 6 :
    tcactg
    Secuencia de ADN Ingresada:
    T T G C G A
    A A G T G C
    T T A T T T
    A G A T G G
    G C G T C A
    T C A C T G
    NO ES MUTANTE

### Ejemplo 2
    A continuación se le pedirá que ingrese 6 secuencias de 6 bases nitrogenadas (A,T,C,G).
    Secuencia 1 :
    atgcaa
    Secuencia 2 :
    cagtgc
    Secuencia 3 :
    ttatat
    Secuencia 4 :
    agaacg
    Secuencia 5 :
    gtcccc
    Secuencia 6 :
    tcactg
    Secuencia de ADN Ingresada:
    A T G C A A
    C A G T G C
    T T A T A T
    A G A A C G
    G T C C C C
    T C A C T G
    ES MUTANTE

