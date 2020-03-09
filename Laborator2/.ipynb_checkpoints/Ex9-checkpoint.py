import numpy as np

def randomlySetNaN(mat: np.array) -> np.array:
    """
    Setează valori NaN pe 10 poziții aleatoare.

    Parameters
    ----------
    mat : np.array
        Matricea care va fi modificată.

    Returns
    -------
    np.array
        Matricea inițială cu valorile modificate.
        
    """
    n, m = mat.shape
    randomLines = np.random.random_integers(0, n - 1, size=10)
    randomColumns = np.random.random_integers(0, m - 2, size=10)
    randomCoords = randomLines, randomColumns
    mat[randomCoords] = np.nan

def findNaN(mat: np.array) -> tuple(np.array, np.array):
    """
    Determină coordonatele la care se află valori NaN.

    Parameters
    ----------
    mat : np.array
        Matricea cu valori NaN care va fi analizată.

    Returns
    -------
    tuple(np.array, np.array)
        Tuplu cu două np.arrays care conțin liniile, respectiv coloanele
        la care se găsesc valori NaN.

    """
    np.argwhere(np.isnan(mat))
    """ TODO: extract lines and columns from np.argwhere """
    

if __name__ == "__main__":
    mat = np.genfromtxt('iris.data', delimiter=',', dtype=np.unicode)
    randomlySetNaN(mat)
    print(mat)