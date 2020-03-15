import numpy as np

def indices(a:np.array, b:np.array) -> tuple:
    """
    Identifică o pereche de indici i, j pentru care a[i][j] > b[i][j].

    Parameters
    ----------
    a : np.array, b : np.array
        Cele două matrici ale căror elemente se vor compara.

    Returns
    -------
    tuple:
        O pereche de indici (dacă există una). Altfel, None.

    """
    assert np.array(a).shape == np.array(b).shape
    idx = np.where((np.array(a) > np.array(b)) == True)
    if idx[0].size == 0 and idx[1].size == 0:
        return None
    else:
        return idx[0][0], idx[1][0]

if __name__ == "__main__":
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]

    b = [[13, 14, 15],
         [16, 17, 18],
         [19, 2, 21],
         [22, 23, 24]]

    print(indices(a, b))