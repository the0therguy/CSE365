import numpy as np
import random



def fitness_score():
    global populations, best, binary
    n = 4
    best = -100000
    binary = []
    chromosome = np.random.randint(0, 15, (n, 2))

    # print(binary)
    # print(chromosome[0][])
    # print("chromosomes:", chromosome)
    objective = abs(38 - 2 * (chromosome[:, 0] ** 2) - 3 * chromosome[:, 1])
    # print("fitness object:", objective)

    # selection of fittest chromosome
    fitness = 1 / (1 + objective)

    # print("fitness object: ", fitness)

    # calculating the fittest chromosome
    total = fitness.sum()
    # print("total:", total)

    # calculating the probability of each chromosome
    populations = fitness / total
    # print(prob)
    objective, chromosome = zip(*sorted(zip(objective, chromosome)))
    best = objective[0]

    print(objective, chromosome)
    for i in chromosome:

        a = bin(i[0]).replace("0b", "")
        x = a[::-1]  # this reverses an array
        while len(x) < 8:
            x += '0'
        a = x[::-1]
        b = bin(i[1]).replace("0b", "")
        x = b[::-1]  # this reverses an array
        while len(x) < 8:
            x += '0'
        b = x[::-1]
        binary.append(a)
        binary.append(b)
    binary = tuple(binary)
    print(binary)


def selectparent():
    global parents
    # global populations , parents
    parents = binary[0:2]
    # print(type(parents))
    # print(parents)


def crossover():
    global parents

    cross_point = random.randint(0, 7)
    parents = parents + tuple([(parents[0][0:cross_point + 1] + parents[1][cross_point + 1:8])])
    parents = parents + tuple([(parents[1][0:cross_point + 1] + parents[0][cross_point + 1:8])])

    print(parents)


def mutation():
    global chromosome, parents
    mute = random.randint(0, 49)
    if mute == 20:
        x = random.randint(0, 3)
        y = random.randint(0, 5)

        (parents[x][y]) = 1 - parents[x][y]

    chromosome = parents
    print(chromosome)


if __name__ == '__main__':

    for i in range(10):
        fitness_score()
        selectparent()
        crossover()
        mutation()
    print("best score :")
    print(best)
    print("sequence........")
    print(binary[0])
