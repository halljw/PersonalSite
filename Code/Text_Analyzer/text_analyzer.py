#!/usr/bin/env python

import sys, os, re, io
from Word_Counter import *
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk

def get_text():
  """
  Returns text of file specified upon progrom execution
  Prints error message and quits if file is not found
  """
  if len(sys.argv) != 2:
    print("[-] usage: %s 'play.txt'" % __file__)
    exit()

  title = sys.argv[1]
  if not os.path.isfile('Texts/' + title):
    print("[-] file not found: '%s'" % title)
    exit()

  with io.open('Texts/' + title, mode='r', encoding='utf-8-sig') as f:
    text = f.read()
  return text

def tokenize(text):
  """
  Takes string of text and returns list comprising word-tokenized text
  Text is formatted to retain only initial capitalizations:
    i.e., OTHELLO --> Othello
  """
  if isinstance(text, str):
    print("[-] error in method 'tokenize(text): text must be type 'str'")
    exit()
  
  tokens = word_tokenize(text)
  tokens = [token[0] + token[1:].lower() for token in tokens]
  return tokens

def extract_names(text):
  """
  Uses the Stanford Named Entity Recognizer to extract named entities from the text
  Returns list of named entities found
  """
  tokens = tokenize(text)
  results = set()
  pos_tags = pos_tag(tokens)
  named_entities = []
  ne_parse = ne_chunk(pos_tags, binary=True)
  named_entities = []
  for tree in ne_parse.subtrees():
    if tree.label() == 'NE':
      named_entities.append(tree)
  for ne in named_entities:
    for n in ne[0:]:
      results.add(n[0])
  return results

def raw_word_count(text):
  """
  Returns a vocabulary and Word_Counter object containing raw word counts contained
    in the text file with given title
  """
  tokens = tokenize(text)
  wc = Word_Counter()
  vocab = set()
  total_words = len(tokens)
  for token in tokens:
    wc.count(token)
    vocab.add(token)
  return total_words, vocab, wc

if __name__=='__main__':
  text = get_text()
  names = extract_names(text)
  total_words, vocab, wc = raw_word_count(text)
  sorted_vocab = wc.sort_words(vocab)
  sorted_names = wc.sort_words(names)
  for name in sorted_names:
    print("%s: %d %f" % (name, wc.get_count(name), wc.get_count(name)/(1.0 * total_words)))

  #for word in sorted_vocab:
  #  print("%s: %d" % (word, wc.get_count(word)))
