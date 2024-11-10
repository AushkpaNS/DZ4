# 9. Выбирается вариант, которого не было у игроков на предыдущем ходе. Первый ход случайным образом
import numpy as np
my_last_action = 0
def third_move_agent(observation, configuration):
    global my_last_action
    if observation.step > 0:
        actions = {0, 1, 2}
        missing_actions = list(actions.difference({my_last_action}).difference({observation.lastOpponentAction})) # список значений, которые не использовались на предыдущем ходе
        result = int(np.random.choice(missing_actions)) # выбор случайным образом из значений, которые не использовались на предыдущем ходе
    else:
        result = np.random.randint(0, 3) # если это первый ход, то случайное решение
    my_last_action = result
    return result
