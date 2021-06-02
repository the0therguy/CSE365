import json
import re


def read_file():
    with open('data.txt', 'r') as file:
        a = file.readlines()
    return a


def find_occurrences(value):
    with open('data.txt', 'r') as file:
        a = file.readlines()

    occurrences = 0
    for i in a:
        if i.replace('\n', '') == value:
            occurrences = occurrences + 1
        else:
            pass
    return occurrences


def training():
    count = 0
    a = read_file()
    attribute = []
    class_name = []
    for i in a:
        attribute.append(i.split()[0])
        class_name.append(i.split()[1])
        count = count + 1
    all_possible_combinations = []
    for i in list(set(attribute)):
        for j in list(set(class_name)):
            all_possible_combinations.append(i + " " + j)
    occurrences = {}
    class_occurance = {}
    for i in all_possible_combinations:
        o = find_occurrences(i)
        occurrences[i] = o
    # print(occurrences)

    for i in list(set(class_name)):
        class_occurance[i] = class_name.count(i)

    likelihood = {}
    for i in occurrences.keys():
        for j in class_occurance.keys():
            if j in i:
                likelihood[i + "/" + j] = occurrences[i] / class_occurance[j]

    with open('likelihood.json', 'w') as file:
        l = json.dumps(likelihood)
        file.write(l)

    prior = {}
    for i in class_occurance.keys():
        prior[i + "/" + str(count)] = class_occurance[i] / count
    with open('prior.json', 'w') as file:
        p = json.dumps(prior)
        file.write(p)

    print("training complete")


def test(s):
    with open('likelihood.json', 'r') as file:
        likelihood = json.load(file)
    with open('prior.json', 'r') as file:
        prior = json.load(file)

    l_value = {}
    for i in likelihood.keys():
        if s in i:
            l_value[i] = likelihood[i]

    val = {}
    for i in l_value.keys():
        for j in prior.keys():
            if re.sub('/.*', '', i.replace(s + " ", '')) == j.replace('/25', ''):
                val[re.sub('/.*', '', i)] = l_value[i] * prior[j]

    print()
    sorted_values = {}
    for i in sorted(val.values()):
        for j in val.keys():
            if val[j] == i:
                sorted_values[j] = val[j]

    print(list(sorted_values.keys())[1])


def menu():
    print("1. Train data")
    print()
    print("2. Test Dataset")
    print()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        training()
    else:
        print()
        a = input("test value: ")
        test(a)


if __name__ == '__main__':
    menu()
