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
    randomLines = np.random.randint(0, n - 1, size=10)
    randomColumns = np.random.randint(0, m - 1, size=10)
    randomCoords = randomLines, randomColumns
    mat[randomCoords] = np.nan

def findNaN(mat: np.array) -> tuple:
    """
    Determină coordonatele la care se află valori NaN.

    Parameters
    ----------
    mat : np.array
        Matricea cu valori NaN care va fi analizată.

    Returns
    -------
    tuple
        Tuplu cu două np.array care conțin liniile, respectiv coloanele
        la care se găsesc valori NaN.

    """
    args = np.argwhere(np.isnan(mat))
    """ TODO: extract lines and columns from np.argwhere """
    lines = [arg[0] for arg in args]
    columns = [arg[1] for arg in args]
    return np.unique(lines), np.unique(columns)
    

if __name__ == "__main__":
    mat = np.genfromtxt('iris.data', delimiter=',')
    mat = np.delete(mat, -1, axis=1)
    randomlySetNaN(mat)
    lines, columns = findNaN(mat)
    print("LINES   : ", lines)
    print("COLUMNS : ", columns)