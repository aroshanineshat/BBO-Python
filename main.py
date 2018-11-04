import numpy as np
import scipy as sp


def Cost_Function(x):
    temp = np.array([0])
    return temp


def bbo_program():
    GenerationLimit = 25000
    PopulationSize = 200
    PopulationParameters=50
    MutationProbability=0.004
    NumberofElites = 2

    MinimumRange = np.array([-2.048])
    MaximumRange = np.array([2.048])

    x = np.random.uniform (MinimumRange, MaximumRange, (PopulationSize, PopulationParameters))



if __name__ == "__main__":
    bbo_program()