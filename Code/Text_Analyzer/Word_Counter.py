#!/usr/bin/env python

class Word_Counter:
  """
  Trie-type data structure for storing/counting words in a text
  """

  def __init__(self):
    self.root = {}
    self.words = []

  def get_count(self, word):
    """
    Returns count for word stored in trie
    """
    branch = self.root
    if len(word) == 0:
      if '__COUNT__' in branch:
        return branch['__COUNT__']
      else:
        return 0
    else:
      if word[0] in branch:
        return branch[word[0]].get_count(word[1:])
      else:
        return 0

  def count(self, word):
    """
    Increment word's value in trie. If not in trie, add initial value of 1.
    """
    branch = self.root
    if len(word) == 0:
      if '__COUNT__' in branch:
        branch['__COUNT__'] += 1
      else:
        branch['__COUNT__'] = 1
    else:
      if word[0] in branch:
        branch[word[0]].count(word[1:])
      else:
        branch[word[0]] = Word_Counter()
        branch[word[0]].count(word[1:])

  def sort_words(self, words):
    """
    Takes a list of words and returns the list sorted by counts
    Sort conducted by merge-sort
    """
    return sorted(words, key=self.get_count, reverse=True)
