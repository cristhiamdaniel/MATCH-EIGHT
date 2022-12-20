import sys

def convertList(l):
    return list(map(int, l))

def findPairs(arr, sum):
    pairs = []
    numbers_viewed = {}
    for num in arr:
        missing_number = sum - num
        if missing_number in numbers_viewed:
            pairs.append((num, missing_number))
        else:
            numbers_viewed[num] = True
    return pairs

def readFile(name):
    file = open(name, 'r')
    lines = file.readlines()
    lines = [x.strip() for x in lines]
    file.close()
    return lines

def main():
    if len(sys.argv) == 3:
        l = sys.argv[1].split(',')
        target = int(sys.argv[2])
        l = convertList(l)
        result = findPairs(l, target)

        for x in list:
            print(x)

    elif len(sys.argv) == 2:

        name = sys.argv[1]
        tex = readFile(name)

        for i in range(len(tex)):
            lista = tex[i].split()
            num = lista[0]

            listaNum = num.split(',')
            target = lista[1]
            l = convertList(listaNum)
            target = int(target)
            result = findPairs(l, target)

            for x in list:
                print(x)
    else:
        print("Los datos ingresados son incorrectos")


if __name__ == '__main__':
    main()