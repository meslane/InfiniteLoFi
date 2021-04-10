import random

def getNGram(data, i, n):
    out = []
    for j in range(i, i + n):
        if (j < len(data)):
            out.append(data[j])

    return out

def markov(data, n, outputLength):
    dataDict = {}

    for i in range(len(data)):
        gram = tuple(getNGram(data, i, n))
        #print(gram)

        if gram not in dataDict:
            dataDict[gram] = []

        dataDict[gram].append(tuple(getNGram(data, i + n, n)))

    output = []

    output.append(random.choice(list(dataDict.keys())))

    for i in range(outputLength):
        try:
            output.append(dataDict[output[-1]][random.randint(0,len(dataDict[output[-1]]) - 1)])
        except KeyError:
            output.append(random.choice(list(dataDict.keys())))

    out = [item for t in output for item in t]

    return out

def testMarkov(filename):
    out = " "

    with open(filename) as f:
        text = f.read().split()

    return out.join(markov(text,1,500000))
    
#print(testMarkov('ssb.txt'))