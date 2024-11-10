# 8. 10% - камень, 20% - бумага, 70% - ножницы
import numpy as np
def scew_rand_agent(observation, configuration):
    values = [0, 1, 2] # значения
    probabilities = [0.1, 0.2, 0.7] # вероятности
    return int(np.random.choice(values, p=probabilities))
