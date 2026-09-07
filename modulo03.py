import numpy as np

def norma(x,p):  # PASA LOS TESTS
    if p == 'inf':
        return max (abs (x))
    
    sumatoria = 0
    for i in range(0, len (x),1):
        sumatoria += np. abs (x[i]) ** p
        
    res = sumatoria ** (1/p)
    
    return res


def normaliza(X,p): # PASA LOS TESTS
    Y = []
    for i in range(0, len (X)) :
        vector_normalizado = X[i] /norma (X[i],p)
        Y.append (vector_normalizado)
    return Y


def normaExacta(A,p=[1,'inf']): # "No se pueden correr los tests" EN EL SERVER
    n,m = A.shape # n = cantidad de filas ; m = cantidad de columnas
    if p == 1:
        maximo = 0
        for j in range(0,m): # recorre las columnas
            sumatoria = 0
            for i in range(0,n): # recorre las filas
                sumatoria += abs(A[i,j])
            if sumatoria > maximo:
                maximo = sumatoria
        return maximo
    
    elif p == 'inf':
        maximo = 0
        for i in range(0,n): # recorre las filas
            sumatoria = 0
            for j in range(0,m): # recorre las columnas
                sumatoria += abs(A[i,j])
        if sumatoria > maximo:
            maximo = sumatoria
        return maximo


def normaMatMC(A,p,q,Np): # "La ejecución demoró más de lo permitido" EN EL SERVER
    m,n = A.shape
    maximo = 0
    x_res = []
    for i in range(0,Np) :
        vector_random = np.random.randn(n)
        x = vector_random/norma (vector_random,p)
        Ax = A@x
        vector_normalizado = norma (Ax, q)
        
        if vector_normalizado > maximo:
            maximo = vector_normalizado
            x_res = x
            
    return maximo, x_res


def condMC(A,p): # ERROR EN EL TEST POR LLAMAR A LA FUNCIÓN CON 3 VARIABLES DE ENTRADA EN VEZ DE DOS.
    norma_A = normaMatMC(A,p,p,10000)[0]
    norma_A_inv = normaMatMC(np.linalg.inv(A),p,p,10000)[0]  # SE PUEDE ENTREGAR CON "np.linalg.inv(A)"???
    return norma_A * norma_A_inv


def condExacto(A, p): # PASA LOS TESTS
    norma_A = normaExacta(A, p)
    norma_A_inv = normaExacta(np.linalg.inv(A), p)  # SE PUEDE ENTREGAR CON "np.linalg.inv(A)"??? 
    return norma_A * norma_A_inv