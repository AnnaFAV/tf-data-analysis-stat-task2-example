import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 502755420 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
      t = 77/2
    s_mean = np.mean(s)
    s_std = np.std(s, ddof=1)
    scale = 1/2
    z = st.norm.ppf((1 + p)/2)
    interval = z * s_std/np.sqrt(len(x))
    lower = 2 * s_mean/t**2 - scale * interval
    upper = 2 * s_mean/t**2 + scale * interval
    return (lower, upper)

p = 0.95
x = np.array([30, 35, 25, 28, 32])
results = solution(p, x)
