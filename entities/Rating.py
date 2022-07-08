class Rating:
    foundKeywords: [str]
    keywordPoints: int
    maxKeywordPoints: int
    similarityScore: float = 0.0
    similarityPoints: int = 0
    maxSimilaityPoints: int

    def __init__(self, maxKeywordPoints: int, maxSimilaityPoints: int):
        self.maxKeywordPoints = maxKeywordPoints
        self.maxSimilaityPoints = maxSimilaityPoints

