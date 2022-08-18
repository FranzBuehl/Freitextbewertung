from entities import Exercise, Rating


class ExerciseRating():
    exercise: Exercise
    rating: Rating

    def to_dictionary(self):
        dict = {}
        dict['exercise'] = self.exercise.to_dictionary()
        dict['rating'] = self.rating.to_dictionary()

        return dict

