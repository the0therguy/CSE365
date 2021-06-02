import numpy as np
import random

"""
f(x)=2a^2+3b-38
"""


def f(a, b):
    return 2 * a * a + 3 * b - 38


def genetic_algorithm(chromosome):
    objective = abs(38 - 2 * (chromosome[:, 0] ** 2) - 3 * chromosome[:, 1])
    # print("fitness object:", objective)

    # selection of fittest chromosome
    fitness = 1 / (1 + objective)
    # print("fitness object: ", fitness)

    # calculating the fittest chromosome
    total = fitness.sum()
    # print("total:", total)

    # calculating the probability of each chromosome
    prob = fitness / total
    # print("probability: ", prob)
    chromosome = parrent_selection(chromosome)
    c_chromosome = []
    for i in range(n - 1):
        if i % 2 == 0:
            p, q = choose_function(chromosome[i], chromosome[i + 1])
            c_chromosome.append(p)
            c_chromosome.append(q)

    chromosome = np.array(c_chromosome)
    # print("chrossover:", chromosome)
    return mutation(chromosome)


def parrent_selection(chromosome):
    answer = 38 - 2 * (chromosome[:, 0] ** 2) - 3 * chromosome[:, 1]

    zipped_lists = zip(answer, chromosome.tolist())

    sorted_zipped_lists = sorted(zipped_lists)

    sorted_chromosome_by_answer = [element for _, element in sorted_zipped_lists]

    return np.array(sorted_chromosome_by_answer)


def choose_function(a, b):
    a1 = bin(a[0]).replace("0b", '')
    a2 = bin(b[0]).replace("0b", '')

    b1 = bin(a[1]).replace("0b", '')
    b2 = bin(b[1]).replace("0b", '')
    if len(a1) == 3:
        a1 = "0" + a1
        # print(a1)
    elif len(a1) == 2:
        a1 = "00" + a1
        # print(a1)
    elif len(a1) == 1:
        a1 = "000" + a1
        # print(a1)
    else:
        pass

    if len(a2) == 3:
        a2 = "0" + a2
        # print(a2)
    elif len(a2) == 2:
        a2 = "00" + a2
        # print(a2)
    elif len(a2) == 1:
        a2 = "000" + a2
        # print(a2)
    else:
        pass

    if len(b1) == 3:
        b1 = "0" + b1
        # print(a1)
    elif len(b1) == 2:
        b1 = "00" + b1
        # print(a1)
    elif len(b1) == 1:
        b1 = "000" + b1
        # print(a1)
    else:
        pass

    if len(b2) == 3:
        b2 = "0" + b2
        # print(a2)
    elif len(b2) == 2:
        b2 = "00" + b2
        # print(a2)
    elif len(b2) == 1:
        b2 = "000" + b2
        # print(a2)
    else:
        pass

    a1, a2 = crossover(a1, a2)
    b1, b2 = crossover(b1, b2)
    return [int(a1, 2), int(b1, 2)], [int(a2, 2), int(b2, 2)]


def crossover(a1, a2):
    number = random.randint(0, 4)
    new_a1 = a1.replace(a1[number:], a2[number:])
    new_a2 = a2.replace(a2[number:], a1[number:])
    return new_a1, new_a2


def mutation(chromosome):
    # calculating the total no of generations
    a, b = chromosome.shape[0], chromosome.shape[1]

    total_gen = a * b
    # print("Total generation:", total_gen)

    # mutation rate = pm
    pm = 0.1
    no_of_mutations = int(np.round(pm * total_gen))
    # print("No of Mutations:", no_of_mutations)

    # calculating the generation number
    gen_number = np.random.randint(0, total_gen - 1, no_of_mutations)
    # print("Generated random number: ", gen_number)

    # generating a random number which can replace the selected chromosome to be mutated
    replacing_number = np.random.randint(0, 15, no_of_mutations)
    # print("Number to be replaced: ", replacing_number)

    for i in range(no_of_mutations):
        a = gen_number[i]
        row = a // 2
        col = a % 2
        chromosome[row, col] = replacing_number[i]

    # print("Chromosome after mutation: ", chromosome)
    return chromosome


if __name__ == '__main__':
    n = 6
    chromosome = np.random.randint(0, 15, (n, 2))
    print("chromosomes:", chromosome)
    epoch = 0
    while epoch < 100:
        chromosome = genetic_algorithm(chromosome)

        for i in chromosome:
            x = f(i[0], i[1])
            if -10 < x < 10:
                print(f"iteration{epoch}: chromosome {i} and value {x}")
                break

            else:
                with open("gene_values.txt", "a") as file:
                    file.write(f"iteration{epoch}:  chromosome {i} and value {x}")
                    file.write("\n")
        epoch = epoch + 1
