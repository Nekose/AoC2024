class Card(object):
    def __init__(self,value: str,day2 = False) -> None:
        if day2:
            self.facevalues = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
        else:
            self.facevalues = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        self.face = value
        if value.isnumeric():
            self.value = int(value)
        else:
            self.value = self.facevalues[value]

    def __eq__(self, other: "Card") -> bool:
        if self.value == other:
            return True
        else:
            return False

    def __ne__(self, other: "Card") -> bool:
        if self.value != other:
            return True
        else:
            return False

    def __lt__(self, other: "Card") -> bool:
        if self.value < other:
            return True
        else:
            return False

    def __gt__(self, other: "Card") -> bool:
        if self.value > other:
            return True
        else:
            return False

    def __repr__(self):
        return self.face

    def __hash__(self):
        return hash(self.face)


