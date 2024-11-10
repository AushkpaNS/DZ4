# 4. Копирование предыдущего хода оппонента. Первый ход случайным образом.
import numpy as np
def copy_opponent_agent(observation, configuration):
    if observation.step > 0:
        result = observation.lastOpponentAction # если это не первый ход, то возвращается предыдущее действие оппонента
    else:
        result = np.random.randint(0, 3) # если это первый ход, то случайное решение
    return result
