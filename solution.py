import pandas as pd
import numpy as np


chat_id = 1326113898 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    b=list(range(len(x)))
    c=[]
    for x1, x2 in zip(x, b):
        c.append(x1*x2)
        d=sum(c)/sum(x)
    return d
