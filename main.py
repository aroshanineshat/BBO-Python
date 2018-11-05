import numpy as np
import scipy as sp


def Cost_Function(x):
    xSize = x.shape
    populationsize = xSize[0]
    populationdime = xSize[1]

    temp = np.zeros( populationsize)

    for popu in np.arange (0, populationsize):
        Cost = 0
        for costi in np.arange (0, populationdime - 1):
            Temp1 = x[popu, costi]
            Temp2 = x[popu, costi + 1]
            Cost = Cost + 100 * (Temp2 - Temp1**2)**2 + (Temp1 - 1)**2
        temp[popu] = Cost

    return temp


def Data_Sort (Cost, x):
    sortarg = Cost.argsort()
    SortedCost = Cost[sortarg]
    SortedPop  = x[sortarg]
    return SortedCost, SortedPop


def bbo_program():
    GenerationLimit = 2500
    PopulationSize = 200
    PopulationParameters=3
    MutationProbability=0.002
    NumberofElites = 2

    ElitePopulations = np.zeros((NumberofElites, PopulationParameters))
    EliteCosts = np.zeros((NumberofElites, 1))

    MinimumCosts = []

    MinimumRange = np.array([-20.048])
    MaximumRange = np.array([20.048])

    CurrentGen = 0
    x = np.random.uniform (MinimumRange, MaximumRange, (PopulationSize, PopulationParameters))
    Cost = Cost_Function(x)
    Cost, x = Data_Sort(Cost, x)
    MinimumCosts.append(Cost[0])

    print("Generation " + str(CurrentGen) + " minimum Cost: " + str(MinimumCosts[-1]))
    z = np.zeros((PopulationSize, PopulationParameters))
    mu = (PopulationSize - np.arange(0, PopulationSize)) / (PopulationSize + 1); # emigration
    lambdas = 1 - mu


    while CurrentGen < GenerationLimit:
        CurrentGen = CurrentGen + 1
        ElitePopulations[0:NumberofElites,:] = x[0:NumberofElites,:]
        EliteCosts[0:NumberofElites,:] = Cost[0:NumberofElites].reshape (NumberofElites , 1)

        for k in np.arange (0, PopulationSize):
            for j in np.arange (0, PopulationParameters):
                if (np.random.uniform(0, 1) < lambdas[k]):
                    RndNum = np.random.uniform(0, 1) * np.sum(mu)
                    Select = mu[0]
                    SelectInd = 0
                    while (RndNum > Select and SelectInd < PopulationSize) :
                        SelectInd = SelectInd + 1
                        Select = Select + mu [SelectInd]
                    z[k, j] = x[SelectInd, j]
                else:
                    z[k, j] = x[k, j]

        for k in np.arange (0, PopulationSize):
            for PInd in np.arange (0, PopulationParameters):
                if np.random.uniform(0, 1) < MutationProbability:
                    z[k, PInd] = np.random.uniform (MinimumRange, MaximumRange)

        x = z
        Cost = Cost_Function(x)
        Cost, x = Data_Sort(Cost, x)

        x[-NumberofElites:, :] = ElitePopulations[0:NumberofElites, :]
        Cost[-NumberofElites:] = np.squeeze(EliteCosts [0:NumberofElites, :])

        Cost, x = Data_Sort(Cost, x)
        MinimumCosts.append(Cost[0])

        print("Generation " + str(CurrentGen) + " minimum Cost: " + str(MinimumCosts[-1]))
    print("Best Cost: " + str(MinimumRange[-1]))
if __name__ == "__main__":
    bbo_program()