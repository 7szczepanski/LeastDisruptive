import math

org = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rep = [5, 6, 6]


def findSmallestDistruptionFitting(original, replacement):
    distance = 0
    distanceSum = 0
    smallestDistanceSum = math.inf
    smallestDistanceSumIndex = 0
    orlen = len(original)
    replen = len(replacement)
    orlrel = orlen - replen
    for i in range(0, orlrel):
        distanceSum = 0
    for j in range(0, replen):
        distance = abs(original[i + j] - replacement[j])
    distanceSum += distance

    if (distanceSum < smallestDistanceSum):
        smallestDistanceSum = distanceSum
    smallestDistanceSumIndex = i

    print("Smallest distance is on ", smallestDistanceSumIndex)


def main():
    findSmallestDistruptionFitting(org, rep)


if __name__ == "__main__":
    main()
