# restaurants = [[1,4,1,40,10],[2,8,0,50,5],
# [3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],
# veganFriendly = 1, maxPrice = 50, maxDistance = 10

#restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]
class Solution:
    def filterRestaurants(self, restaurants,
                          veganFriendly, maxPrice, maxDistance):


        outputList = []
        veganFriendlyCount  = 0
        if veganFriendly == 1:
            for index in range(len(restaurants)):
                if restaurants[index][2] == 1:
                    veganFriendlyCount += 1
                    outputList.append(in)
        elif veganFriendly == 0:
            outputList.append(len(restaurants))

        if maxPrice:
            maxPriceCount = 0
            for index in range(len(restaurants)):
                if restaurants[index][3] >= maxPrice:
                    maxPriceCount += 1
                    outputList.append(restaurants[index][0])

        if maxDistance:
            maxDistanceCount = 0
            for index in range(len(restaurants)):
                if restaurants[index][4] <= maxDistance:
                    maxDistanceCount += 1
            outputList.append(maxDistanceCount)
        return outputList


if __name__ == '__main__':
    s = Solution()
    restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5],
                   [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]
                   ]
    veganFriendly = 0
    maxPrice = 50
    maxDistance = 10
    veganList = s.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance)

    print(veganList)