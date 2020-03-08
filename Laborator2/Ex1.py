import numpy as np

def getUnique(x: np.array) -> np.array:
    """Determină elementele unice dintr-un numpy.array, în ordine descrescătoare.

    Parameters
    ----------
    x : np.array
        Vectorul analizat. 
  
    Returns
    -------
    np.array
        Elementele unice din vectorul analizat, sortate descrescător. 

    """
    result = np.unique(x)
    result = np.sort(result)[::-1]
    return result

if __name__ == "__main__":
    x = np.array([-4, 3, 5, 3, 2, 1, -3, -4, 2, -4])
    result = getUnique(x)
    print("Result: ", result)
    