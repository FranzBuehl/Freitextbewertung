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

    def to_dictionary(self):
         dict = {}
         dict['foundKeywords'] = self.foundKeywords
         dict['keywordPoints'] = self.keywordPoints
         dict['maxPointsKeyword'] = self.maxPointsKeyword
         dict['similarityScore'] = self.similarityScore
         dict['similarityPoints'] = self.similarityPoints
         dict['maxPointsSimilaity'] = self.maxPointsSimilaity

         return dict
