from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"(name={self.name}, score={self.score})"

    def __str__(self):
        return f"(name={self.name}, score={self.score})"


def sort_players():
    players = [ Player("louis", 67),
                Player("ricky", 41),
                Player("dave", 92) ]

    print(sorted(players, key=cmp_to_key(lambda l, r: r.score - l.score)))
