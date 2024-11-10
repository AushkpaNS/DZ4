# 11. Если предыдущий раунд был выигрышным или ничейным, то повторяет то же действие, иначе меняет решение на случайное, отличающееся от предыдущего хода. Первый ход случайным образом.
import numpy as np
import math

my_last_action = 0

def check_result(move1, move2):
    delta = (
        move2 - move1
        if (move1 + move2) % 2 == 0
        else move1 - move2
    )
    return 0 if delta == 0 else math.copysign(1, delta)

def confirmation_agent(observation, configuration):
    global my_last_action
    if observation.step > 0:
        if check_result(my_last_action, observation.lastOpponentAction) >= 0:
            result = my_last_action
        else:
            actions = {0, 1, 2}
            missing_actions = list(actions.difference({my_last_action})) # список значений, которые не использовались на предыдущем ходе
            result = int(np.random.choice(missing_actions)) # выбор случайным образом из значений, которые не использовались на предыдущем ходе
    else:
        result = np.random.randint(0, 3) # если это первый ход, то случайное решение
    my_last_action = result
    return result
