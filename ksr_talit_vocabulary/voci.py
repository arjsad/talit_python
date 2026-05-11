class WordPair:
    """A word and its translation."""

    def __init__(self, word1, word2):
        """Creates a new pair from two strings."""
        self.word1 = word1
        self.word2 = word2

    def reversed(self):
        """Returns a copy of the pair in the reverse direction."""
        return WordPair(self.word2, self.word1)


class VocabularyUnit:
    """A unit of WordPairs that belong together."""

    def __init__(self, word_pairs):
        """Creates a new unit from a list of WordPairs."""
        self.word_pairs = word_pairs


class ConsoleLearner:
    """Asks all WordPairs of a VocabularyUnit in the console."""

    def learn(self, unit):
        """Asks each WordPair of the given unit in the terminal."""
        for pair in unit.word_pairs:
            answer = input(f"Translate {pair.word1}: ")
            if answer == pair.word2:
                print("correct")
            else:
                print(f"incorrect (richtig: {pair.word2})")
            input("Enter für nächste Vokabel...")
            print("\033c", end="")


unit = VocabularyUnit([
    WordPair('Baum', 'tree'),
    WordPair('Blume', 'flower'),
    WordPair('Fisch', 'fish'),
])
learner = ConsoleLearner()
learner.learn(unit)
