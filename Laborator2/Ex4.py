import numpy as np

def product(mat:np.array, compute_on_lines:bool) -> np.array:
    """
    Determină produsul elementelor de pe liniile unei matrice (compute_on_lines = True).
    Altfel, produsul elementelor de pe coloane.

    Parameters
    ----------
    mat : np.array
        Matricea analizată.

    Returns
    -------
    np.array
        Vectorul de produse.
    """
    return np.product(mat, int(compute_on_lines)) # False = 0, True = 1

if __name__ == "__main__":
    mat = [[1, 2, 3, 4],
           [1, -2, 3, -4],
           [3, 10, 3, 4]]
    compute_on_lines = False
    products = product(mat, compute_on_lines)
    print(products)