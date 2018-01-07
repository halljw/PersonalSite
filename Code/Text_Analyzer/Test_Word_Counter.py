#!/usr/bin/env python

from Word_Counter import *

def test_word_counter():
  """
  >>> wc = Word_Counter()
  >>> sent = "Once upon a midnight dreary while I pondered weak and weary "
  >>> sent += "over many a quaint and curious volume of forgotten lore"
  >>> for word in sent.split(): wc.count(word)
  >>> wc.get_count("Once")
  1
  >>> wc.get_count("a")
  2
  >>> wc.get_count("Lenore")
  0
  """

def test_sort_words():
  """
  >>> wc = Word_Counter()
  >>> sent = "And I was like baby baby baby oh "
  >>> sent += "Like baby baby baby oh "
  >>> sent += "I though you'd always be mine mine "
  >>> for word in sent.split(): wc.count(word)
  >>> wc.sort_words(['I', 'baby', 'always', 'yes'])
  ['baby', 'I', 'always', 'yes']
  """

if __name__=='__main__':
  import doctest
  doctest.testmod()
