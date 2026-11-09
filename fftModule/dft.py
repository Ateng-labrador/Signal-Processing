import cmath
import math

def widlet(N):
    """
    Function to making widle matriks
    """
    res = []
    for k in range(N):
        row = []
        for n in range(N):
            W = cmath.exp(-1j * 2 * cmath.pi * k * n / N)
            row.append(W)
        res.append(row)
    return res


def dct(x, type="two", ):
    res = []
    if type == "one":
        for k in range(len(x)):
            row = 0.0
            for n in range(len(x)):
                if n == 0 or n == len(x) - 1:
                    alpha = 0.5
                else:
                    alpha = 1
                op = (math.pi * k * n / len(x) - 1)
                row += alpha * x[n] * math.cos(op)
            res.append(row)
        return 2 * res
    elif type == "two":
        for k in range(len(x)):
            row = 0.0
            for n in range(len(x)):
                op = (math.pi * k * (2 * n + 1) / 2 * len(x))
                row += x[n] * math.cos(op)
            res.append(row)
        return 2 * res
    elif type == "tree":
        pass
    elif type == "four":
        pass
    else:
        return "Error yaa"
                

def dft(x):
    """
    Function to calculation Discrete Fourier Transform
    """
    widle_matriks = widlet(len(x))
    res = [0] * len(x)
    for k in range(len(x)):
        for n in range(len(widle_matriks[0])):
            res[k] += widle_matriks[k][n] * x[k] 
    return res


def dft2d(x, y):
    pass

