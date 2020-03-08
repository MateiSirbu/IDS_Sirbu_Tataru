import numpy as np

def getFreqInfreq(x: np.array) -> tuple:
    """
    Determină cel mai frecvent și cel mai puțin frecvent element dintr-un numpy.array.

    Parameters
    ----------
    x : np.array
        Vectorul analizat.

    Returns
    -------
    tuple
        Tuplu de două valori: cel mai frecvent și cel mai puțin frecvent element.

    """
    xUnique, counts = np.unique(x, return_counts=True)
    countsDescIndices = np.argsort(-counts)
    return xUnique[countsDescIndices[0]], xUnique[countsDescIndices[-1]]

if __name__ == "__main__":
    x = np.array([-4, 3, 5, 3, 2, 1, -3, -4, 2, -4])
    freq, infreq = getFreqInfreq(x)
    print("Most frequent item: ", freq)
    print("Most infrequent item: ", infreq)