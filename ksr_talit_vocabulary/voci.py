class WordPair:
    """A word and its translation."""
    def __init__(self, word1, word2):
        """Creates a new pair from two strings."""
        self.word1 = word1   # All objects of class WordPair share the same attributes
        self.word2 = word2   # but not necessarily the same contents.
 
    def reversed(self):       # All objects of class WordPair share the same methods
        """Returns a copy of the pair in the reverse direction."""
        return WordPair(self.word2, self.word1)
 
tree = WordPair('Baum', 'tree')  # Calls __init__, we are passing only two arguments, the self argument is implicit.
 
print(f'{tree.word1} translates to {tree.word2}')  # Attributes can be accessed using dot-notation.
