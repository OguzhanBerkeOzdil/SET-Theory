import os

def printSet(x):
    if x in globals():
        anySet = globals()[x]
        print("Your set is:\n", anySet)
    else:
        print("ERROR INVALID SET NAME")


def addSet(x):
    if x in globals():
        anySet = globals()[x]
        print("Your set is:\n", anySet)
        y = int(input("Enter the value that you want to add to the set\n"))
        anySet.add(y)
        print("Your new set is:\n", anySet)
    else:
        print("ERROR INVALID SET NAME")


def removeSet(x):
    if x in globals():
        anySet = globals()[x]
        print("Your set is:\n", anySet)
        y = int(input("Enter the value that you want to remove to the set\n"))
        anySet.remove(y)
        print("Your new set is:\n", anySet)
    else:
        print("ERROR INVALID SET NAME")


def cardinalitySet(x):
    x = input("Enter name of the set\n")
    if x in globals():
        anySet = set(globals()[x])
        print("Your set is:\n", anySet, "\nLenght of your set is ", len(anySet))
        n = int(len(anySet))
        print(pow(2, n))
    else:
        print("ERROR INVALID SET NAME")


def isEqualSet(x, y):
    if x and y in globals():
        anySet1 = globals()[x]
        anySet2 = globals()[y]
        print("First set is:\n", anySet1, "\nSecond set is:\n", anySet2)
        if anySet1 == anySet2:
            print("Sets are equal")
        else:
            print("Sets are not equal")
    else:
        print("ERROR INVALID SET NAME")


def power_set(A):
    length = len(A)
    l = [a for a in A]
    ps = set()

    for i in range(2 ** length):
        selector = f'{i:0{length}b}'
        subset = {l[j] for j, bit in enumerate(selector) if bit == '1'}
        ps.add(frozenset(subset))
    return ps


def cartesianSet(x, y):
    if x and y in globals():
        anySet1 = set(globals()[x])
        anySet2 = set(globals()[y])
        print("First set is:\n", anySet1, "\nSecond set is:\n", anySet2)
        res = [(a, b) for a in anySet1 for b in anySet2]
        print("Cartesian sets of first and second set are:\n", str(res))
    else:
        print("ERROR INVALID SET NAME")



def differenceSet(x,y ):
    if x and y in globals():
        anySet1 = set(globals()[x])
        anySet2 = set(globals()[y])
        print("First set is:\n", anySet1, "\nSecond set is:\n", anySet2)
        anySet3 = anySet1 - anySet2
        print("A - B:\n", anySet3)
    else:
        print("ERROR INVALID SET NAME")


def unionSet(x, y):
    if x and y in globals():
        anySet1 = set(globals()[x])
        anySet2 = set(globals()[y])
        print("First set is:\n", anySet1, "\nSecond set is:\n", anySet2)
        print('A U B = ', anySet1.union(anySet2))
    else:
        print("ERROR INVALID SET NAME")


def intersectionSet(x, y):
    if x and y in globals():
        anySet1 = set(globals()[x])
        anySet2 = set(globals()[y])
        print("First set is:\n", anySet1, "\nSecond set is:\n", anySet2)
        print('A n B = ', anySet1.intersection(anySet2))
    else:
        print("ERROR INVALID SET NAME")


def createFile():
    k = str([globals()[i] for i in globals() if isinstance(globals()[i], set)])

    with open('sets.txt', 'w') as f:
        f.write('')
        f.write(k)
        f.close()

    with open('sets.txt', 'r') as file:
        filedata = file.read()

    filedata = filedata.replace('}, ', '\n')
    filedata = filedata.replace('[', '')
    filedata = filedata.replace(']', '')
    filedata = filedata.replace('}', '')
    filedata = filedata.replace('{', '')

    with open('sets.txt', 'w') as file:
        file.write(filedata)


def one(oper):
    match oper:
        case "print":
            printSet(x)
        case "add":
            addSet(x)
        case "remove":
            removeSet(x)
        case "cardinal":
            cardinalitySet(x)
        case "power":
            if x in globals():
                anySet = set(globals()[x])
                print([set(s) for s in power_set(anySet)])
            else:
                print("ERROR INVALID SET NAME")
        case _:
            print("ERROR INVALID OPERATION NAME")


def two(oper):
    match oper:
        case "equal":
            isEqualSet(x, y)
        case "cartesian":
            cartesianSet(x, y)
        case "difference":
            differenceSet(x, y)
        case "union":
            unionSet(x, y)
        case "intersection":
            intersectionSet(x, y)
        case _:
            print("ERROR INVALID OPERATION NAME")


os.system("a.txt")
python_file = open("a.txt").read()
exec(python_file)


while(1):

    print("\n\n")
    print("If you want to see one element operation list  '1'")
    print("If you want to see two element operation list '2'")
    print("If you want to save the last looking of the sets in to sets.txt file enter '3'")
    print("If you want to close the program '4'")
    m = int(input())

    if m == 1:
        f = open("operations1.txt", "r")
        print(f.read())
        x, oper = input("...\n").split()
        one(oper)
    elif m == 2:
        f = open("operations2.txt", "r")
        print(f.read())
        x, y, oper = input("...\n").split()
        two(oper)
    elif m == 3:
        createFile()
        print("Please check the project folder.")
    elif m == 4:
        exit()
    else:
        print("ERROR")
