import itertools
import math

open("possibilities.txt", "w").close()
slovar = open("E:\ZmagovanjeAneja\slovar.txt", "r", encoding='utf-8')
besede = []
for i in slovar:
    besede.append(str(i).replace("\n", ""))


def generate(list, word_length):
    yield from itertools.permutations(list, word_length)

def generate_possibilities(letters: str):
    possibilities_list = []
    length = len(letters)
    total_possibilities = sum(math.factorial(length) // math.factorial(length - i) for i in range(3, length + 1))
    print(f"There are `{total_possibilities}` possibilities")
    #with open("wordlist.txt", "r") as f:
    #    global seznam_besed
    #    seznam_besed = f.read().splitlines()

    for i in range(3, length + 1):
        for j in generate(letters, i):
            word = "".join(j)
            possibilities_list.append(word) #! ig da to converta use tuple u en list povn stringou
            #with open("possibilities.txt", "a") as f:
            #    f.write("".join(j) + "\n")

    return possibilities_list
pos = generate_possibilities("kist")
result_2 = list(set(pos).difference(besede))
result_3 = list(set(pos).difference(result_2))
print(result_3)
