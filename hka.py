import pandas as pd
import numpy as np

def hka(dataIn):
    # Daten Mittelwertfrei machen
    data = dataIn.copy()
    avg = data.mean()
    for i in range(len(avg)):
        data.ix[:,i] = data.ix[:,i] - avg[i]

    matrix = data.as_matrix()
    U, s, V = np.linalg.svd(matrix)

    S = np.zeros(data.shape)
    S[:len(s), :len(s)] = np.diag(s)

    newData = np.matrix(U)*np.matrix(S)
    return (V, newData, s)
