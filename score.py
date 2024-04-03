class Score:
    def __init__(self):
        self.__score = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def add_one(self):
        self.__score += 1
        return self.__score

    def reset_score(self):
        self.__score = 0

    def get_score(self):
        return self.__score
