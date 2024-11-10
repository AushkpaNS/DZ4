# 6. Первый раунд случайный, далее по кругу
import numpy as np
my_last_action = 0
def circle_agent(observation, configuration):
    global my_last_action
    if observation.step > 0:
        result = (my_last_action + 1) % 3 # если это не первый ход, то возвращается предыдущее действие оппонента
    else:
        result = np.random.randint(0, 3) # если это первый ход, то случайное решение
    my_last_action = result
    return result
