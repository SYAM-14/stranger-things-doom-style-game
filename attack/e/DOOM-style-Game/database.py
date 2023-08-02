import json

data = {}


def loadScores():
    try:
        with open('data.json', 'r') as f:
            global data
            data = json.load(f)
    except BaseException:
        print('Error loading data.json')


def saveScores():
    with open('data.json', 'w') as f:
        json.dump(data, f)


def addScore(name, score):
    if name in data:
        oldScore = data[name]
        if score > oldScore:
            data[name] = score
    else:
        data[name] = score
    data['current'] = name
    saveScores()


def getScores():
    return data


def sortScores():
    filtered = {k: v for k, v in data.items() if k != 'current'}
    return {
        k: v for k,
        v in sorted(
            filtered.items(),
            key=lambda item: item[1],
            reverse=True)}
