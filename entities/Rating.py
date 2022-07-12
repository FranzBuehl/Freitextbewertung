class Rating:
    foundKeywords: [str]
    keywordPoints: int
    maxPointsKeyword: int
    similarityScore: float = 0.0
    similarityPoints: int = 0
    maxPointsSimilaity: int

    def __init__(self, maxPointsKeyword: int, maxPointsSimilaity: int):
        self.maxPointsKeyword = maxPointsKeyword
        self.maxPointsSimilaity = maxPointsSimilaity

