# Given a phrase, count the occurrences of each word in that phrase.

# For the purposes of this exercise you can expect that a word will always be one of:

# A number composed of one or more ASCII digits (ie "0" or "1234") OR
# A simple word composed of one or more ASCII letters (ie "a" or "they") OR
# A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")
# When counting words you can assume the following rules:

# The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
# The count is unordered; the tests will ignore how words and counts are ordered
# Other than the apostrophe in a contraction all forms of punctuation are ignored
# The words can be separated by any form of whitespace (ie "\t", "\n", " ")

# That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled

# phrase= "That's the password "
# end = 0
# start= 0
# for letter in phrase:
#   end = end + 1
#   if letter == " ":
#     word = phrase[start:end]
#     print(word)
#     start=end    

phrase= "That's the password"
length= len(phrase)

def wordcount(sentence):
  return len(sentence)
