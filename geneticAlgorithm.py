import numpy as np
#import scipy as scp
#import matplotlib.pyplot as plt
#import itertools as itt


class Individual():
    
    def setAttributes(self, attributes):
        self.attributes = attributes
        
    def setFitness(self, fitness):
        self.fitness = fitness
        
    def __str__(self):
        return '{0:.3f}: {1:s}'.format(self.fitness, self.attributes.__str__())


class GeneticAlgorithm():
    
    def __init__(self):
        self.population = []
    
    def initPopulation(self, attributesPopulation, numAttributes, sizePopulation):
        for i in range(sizePopulation):
            iv = Individual()
            iv.setAttributes(np.random.permutation(attributesPopulation)[:numAttributes])
            self.population.append(iv)
            
    def setFitnessFunction(self, function):
        self.fitnessFunction = function
    
    def evaluateFitness(self):
        for iv in self.population:
            iv.setFitness(self.fitnessFunction(iv.attributes))
            
    def sortByFitness(self):
        self.population.sort(key=lambda iv: iv.fitness)
    
    def chooseParents(self):
        pass
    
    def crossover(self):
        pass
    
    def mutate(self):
        pass
    
    def makeChildren(self):
        pass
    
    def replaceParents(self):
        pass
    
    def __str__(self):       
        return '\n'.join([iv.__str__() for iv in self.population])
    
    
def fitFun(attributes):
    return np.sum(attributes)
    
    
if __name__ == '__main__':
    ga = GeneticAlgorithm()
    ga.initPopulation(range(1, 117 + 1), 3, 10)
    ga.setFitnessFunction(fitFun)
    ga.evaluateFitness()
    ga.sortByFitness()
    print(ga)