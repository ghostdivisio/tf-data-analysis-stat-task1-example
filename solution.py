import pandas as pd
import numpy as np


chat_id = 1326113898 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #lmbd = np.mean(x) / 48
    #return lmbd # Ваш ответ
    total_lamps = np.sum(x)
    lambda_ = total_lamps / (len(x) * 48)
    return lambda_
