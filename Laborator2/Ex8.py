import numpy as np

def pair_max(a: np.array, b: np.array) -> np.array:
    """
    Determină, pentru fiecare poziție, maximele dintre doi vectori np.array.
    Afișează eroare dacă vectorii nu sunt de aceeași lungime.

    Parameters
    ----------
    a : np.array
        Vector cu numere.
    b : np.array 
        Vector cu numere.

    Returns
    -------
    np.array
        Vector cu valorile maxime dintre a și b pentru fiecare poziție.
        
    """
    assert a.size == b.size
    return np.maximum(a, b)

if __name__ == "__main__":
    a = np.array([3, 7, 9, 13, -10, 200, 3])
    b = np.array([4, 5, -9, 100, 300, 230, 1])
    print(pair_max(a, b))