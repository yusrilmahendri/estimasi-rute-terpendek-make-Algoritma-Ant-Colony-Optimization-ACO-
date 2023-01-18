import random
import sys


class AntColonyOptimizationTSP:

    def __init__(self, parameters, start):
        self.params = parameters
        self.start = start

    def getDistance(self, pairedCities):
        rets = []
        for i in pairedCities:
            for j in range(len(self.params['matriks'])):
                for k in range(len(self.params['matriks'][j])):
                    if i[0] == j and i[1] == k:
                        rets.append(self.params['matriks'][j][k])
        return rets

    def getNextCitites(self, probNextCities, r):
        tmp = 0
        for i in range(len(probNextCities)):
            if sum(probNextCities) != 0:
                tmp = tmp + (probNextCities[i] / sum(probNextCities))
            else:
                tmp = 0
            if r < tmp:
                i
                break
        return i

    def getPairedCityName(self, tabuList):
        rets = []
        for i in tabuList:
            for j in range(len(self.params['cityNames'])):
                if i == j:
                    rets.append(self.params['cityNames'][j])
        return rets

    def getProbNextCities(self, distancePaired, feromon):
        ret = []
        for distance in distancePaired:
            if distance == 0:
                val = 0
            else:
                val = (1 / distance) * feromon
            ret.append(val)
        return ret

    def ACOTSProblem(self):
        tabuList = []
        # feromon = 1 / len(self.params['matriks'])
        feromon = 0.1
        finalDistances = []
        allDistances = []
        finalResult = []
        bestSolutions = []
        for iter in range(self.params['maxIter']):
            # print('interasi ke-', iter)
            for i in range(self.params['antSize']):
                if self.start:
                    nextCity = self.start[0]
                else:
                    nextCity = random.randint(
                        0, len(self.params['matriks']) - 1)
                tabuList.append([nextCity])
            # print(tabuList)
            #tabuList = []

            temp = []
            city = []
            pairedCity = []
            matriks = self.params['matriks']
            for i in range(len(matriks)-1):
                # print('kota', i)
                for j in range(len(tabuList)):
                    r = random.uniform(0, 1)
                    # print(tabuList[j])
                    for cityID in range(len(matriks)):
                        for k in tabuList[j]:
                            temp.append(k)
                            temp.append(cityID)
                        if temp.count(cityID) == len(tabuList[j]):
                            city.append(tabuList[j][-1])
                            city.append(cityID)
                        else:
                            city.append(cityID)
                            city.append(cityID)
                        pairedCity.append(city)
                        temp = []
                        city = []
                    pairedDistances = self.getDistance(pairedCity)
                    pairedCity = []
                    probNextCities = self.getProbNextCities(
                        pairedDistances, feromon)
                    nextCities = self.getNextCitites(probNextCities, r)
                    tabuList[j].append(nextCities)
            # print(tabuList)
            # print()
            for k in range(len(tabuList)):
                # print(tabuList[k])
                for l in range(len(tabuList[k]) - 1):
                    # print(tabuList[k][l], tabuList[k][l + 1])
                    city.append(tabuList[k][l])
                    city.append(tabuList[k][l+1])
                    pairedCity.append(city)
                    city = []
                pairedCity.append([tabuList[k][-1], tabuList[k][0]])
                pairedDistances = self.getDistance(pairedCity)
                name = self.getPairedCityName(tabuList[k])

                finalDistances.append([name, pairedDistances])
                allDistances.append(sum(pairedDistances))
                pairedCity = []
            minIndex = allDistances.index(min(allDistances))
            finalResult.append(finalDistances[minIndex])
            bestSolutions.append(min(allDistances))

            finalDistances = []
            allDistances = []
            tabuList = []
        shortestRoutes = finalResult[bestSolutions.index(min(bestSolutions))]
        print('rute terpendek menempuh antar kota:')
        for i in shortestRoutes[0]:
            print(i)
        print(shortestRoutes[0][0])
        print("%.2f" % sum(shortestRoutes[1]), 'kilometer')


matriks = [[0, 4.1, 4.2, 4.1, 2.6, 5.2],
           [4.1, 0, 6.3, 5.8, 4.3, 2.3],
           [4.2, 6.3, 0, 1.1, 8.8, 6.1],
           [4.1, 5.8, 1.1, 0, 7.5, 6.7],
           [2.6, 4.3, 8.8, 7.5, 0, 1.9],
           [5.2, 2.3, 6.1, 6.7, 1.9, 0]]

cityNames = [
    "kos (Jotawang)", "Keraton", "Gedung Kuning", "Kota Gede", "Taman Siswa", "Maliboro"
]

parameters = {
    'Q': 100,
    'rho': 0.6,
    'antSize': 10,
    'matriks': matriks,
    'maxIter': 30,
    'cityNames': cityNames
}

aco = AntColonyOptimizationTSP(parameters, start=[0])
aco.ACOTSProblem()
# print(aco.params)
