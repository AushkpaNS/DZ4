# 10. Выбирает вариант, проигрывающий предыдущему ходу оппонента. Первый ход случайным образом.
import numpy as np
def givup_agent(observation, configuration):
    if observation.step > 0:
        result = (observation.lastOpponentAction + 2) % 3 # если это не первый ход, то возвращается предыдущее действие оппонента
    else:
        result = np.random.randint(0, 3) # если это первый ход, то случайное решение
    return result
