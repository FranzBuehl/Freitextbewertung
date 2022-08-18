class RatingScheme:
    pointsPerKeyword: int
    maxPointsKeywords: int
    pointsForSimilarity: {}

    def __init__(self, pointsPerKeyword, maxPointsKeywords, pointsForSimilarity):
        self.pointsPerKeyword = pointsPerKeyword
        self.maxPointsKeywords = maxPointsKeywords
        self.pointsForSimilarity = pointsForSimilarity


