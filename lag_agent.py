# 5. Выбор варианта, побеждающего предыдущий ход оппонента. Первый ход случайным образом.
import numpy as np
def lag_agent(observation, configuration):
    if observation.step > 0:
        result = (observation.lastOpponentAction + 1) % 3 # если это не первый ход, то возвращается предыдущее действие оппонента
    else:
        result = np.random.randint(0, 3) # если это первый ход, то случайное решение
    return result
