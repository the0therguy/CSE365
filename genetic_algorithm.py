import numpy as np

"""
f(x)=2a^2+3b-38
"""
n = 10
chromosome = np.random.randint(0, 15, (n, 2))
print("chromosomes:", chromosome)
epoch = 0

while epoch < 1:
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

    # Selection using roulette wheel and calculating cumulative probability

    # cumulative_sum = np.cumsum(prob)
    # print("cumulative sum:", cumulative_sum)

    # generating random numbers in the range 0-1
    random_number = np.random.random((chromosome.shape[0]))
    # print("random number: ", random_number)

    # making new matrix of chromosome for calculating purpose
    # chromosome_2 = np.zeros((chromosome.shape[0], 2))
    #
    # for i in range(random_number.shape[0]):
    #     for j in range(chromosome.shape[0]):
    #         if random_number[i] < cumulative_sum[j]:
    #             chromosome_2[i, :] = chromosome[j, :]
    #             break
    #
    # chromosome = chromosome_2
    # print("Chromosome after update: ", chromosome)

    # crossover
    r = [np.random.random() for i in range(n)]
    # print("Random values: ", r)

    # crossover rate
    pc = 0.50
    flag = random_number < pc
    # print("Flagged values: ", flag)

    # determine the cross chromosome
    cross_chromosome = chromosome[[(i != False) for i in flag]]
    # print("Cross chromosome: ", cross_chromosome)
    len_cross_chromosome = len(cross_chromosome)
    print("len_cross_chromosome", len_cross_chromosome)

    # calculating the cross values
    cross_values = np.random.randint(1, 3, len_cross_chromosome)
    print("Cross values: ", cross_values)

    cpy_chromosome = np.zeros(cross_chromosome.shape)
    # print(cpy_chromosome)

    # perfroming the cross-over

    # copying`the chromosome values for calculations
    for i in range(cross_chromosome.shape[0]):
        cpy_chromosome[i, :] = cross_chromosome[i, :]

    if len_cross_chromosome == 1:
        cross_chromosome = cross_chromosome
    else:
        for i in range(len_cross_chromosome):
            c_val = cross_values[i]

            if i == len_cross_chromosome - 1:
                cross_chromosome[i, c_val:] = cpy_chromosome[0, c_val:]
            else:
                cross_chromosome[i, c_val:] = cpy_chromosome[i + 1, c_val:]

    # print("crossover chromosome: ", cross_chromosome)

    index_chromosome = 0
    index_new_chromosome = 0
    for i in flag:
        if i == True:
            chromosome[index_chromosome, :] = cross_chromosome[index_new_chromosome, :]
            index_new_chromosome = index_new_chromosome + 1
        index_chromosome = index_chromosome + 1

    print("New chromosome: ", chromosome)

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

    print("Chromosome after mutation: ", chromosome)
    epoch = epoch + 1
