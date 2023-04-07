import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 502755420 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    times = 77
    n = len(х)
    s = np.mean(х)
    t_alpha_2 = t.ppf(1 - alpha / 2, n - 1)
    lambda_ = 1
    scale = s / lambda_
    ci_half_width = t_alpha_2 * scale * np.sqrt((2 * (n - 1)) / (n * (n - 2)))
    a = 2 * s / (times ** 2)
    lbda = 1 / scale
    left = a - expon.ppf(1 - alpha / 2, scale=1 / lbda) * ci_half_width
    right = a + expon.ppf(1 - alpha / 2, scale=1 / lbda) * ci_half_width
    return (left, right)
