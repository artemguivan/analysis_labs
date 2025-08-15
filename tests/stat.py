import numpy as np

def pearson_corr(x: np.array, y: np.array) -> float:
    x_mean = x.mean()
    y_mean = y.mean()
    prod_sum = sum([(x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(x, y)])
    prod_sqrt_sum_x = np.sqrt(sum([(x_i - x_mean)**2 for x_i in x]))
    prod_sqrt_sum_y = np.sqrt(sum([(y_i - y_mean)**2 for y_i in y]))
    corr = prod_sum / ( prod_sqrt_sum_y * prod_sqrt_sum_x)
    return corr

assert np.allclose(pearson_corr(np.array([1, 2, 3]), np.array([1, 2, 3])), 1.0) 
