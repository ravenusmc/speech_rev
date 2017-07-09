
#This function will get all the words out of the text document and into a list 
def get_words():
  words =[]
  with open('gettysburg.txt','r') as text:
      for line in text:
          for word in line.split():
             words.append(word)
  return words

#This function will get the word counts of each specific word. 
def get_word_count(words):
  word_and_count = {}
  len_count = 0
  while len_count < len(words):
    word_count = 0
    current_word = words[len_count]
    for word in words:
      if (current_word == word and current_word != 'and' and current_word != 'the' and current_word != 'The'and current_word !=
      'on' and current_word != 'of' and current_word != 'But' and current_word != 'from' and current_word != 'any'
      and current_word != 'nor' and current_word != 'this' and current_word != 'is' and current_word != 'by' and current_word != 'it'
      and current_word != 'take' and current_word != 'that' and current_word != 'but' and current_word != 'for'
      and current_word != 'these' and current_word != 'can' and current_word != 'or' and current_word != 'are'
      and current_word != 'did' and current_word != 'who' and current_word != 'say' and current_word != 'It'
      and current_word != 'rather' and current_word != 'in' and current_word != 'thus' and current_word != 'as'
      and current_word != 'do' and current_word != 'so' and current_word != 'will' and current_word != 'a'
      and current_word != 'not' and current_word != 'here' and current_word != 'whether' and current_word != 'Now' 
      and current_word != 'altogether' and current_word != 'which' and current_word != 'to' and current_word != 'met'
      and current_word != 'what' and current_word != 'those'):
        word_count += 1
        word_and_count[current_word] = word_count


    len_count += 1 
  print(word_and_count)

#This is the main function that will run the program. 
def main():
  words = get_words()
  get_word_count(words)
  # print(words)


#Here I call the main function to run the program. 
main()

{'measure': 1, 'from': 2, 'consecrate': 1, 'who': 3, 'ago': 1, 'not': 5, 'remember': 1, 'forth': 1, 'advanced': 1, 'add': 1, 'brave': 1, 'lives': 1, 'God': 1, 'equal': 1, 'that': 13, 'before': 1, 'We': 2, 'note': 1, 'work': 1, 'are': 3, 'by': 1, 'what': 2, 'we': 8, 'vain': 1, 'Four': 1, 'endure': 1, 'far': 2, 'poor': 1, 'consecrated': 1, 'continent': 1, 'seven': 1, 'task': 1, 'proper': 1, 'above': 1, 'a': 7, 'on': 2, 'nation': 5, 'larger': 1, 'living': 2, 'be': 2, 'detract': 1, 'conceived': 2, 'hallow': 1, 'place': 1, 'as': 1, 'rather': 2, 'met': 1, 'whether': 1, 'forget': 1, 'Liberty': 1, 'nobly': 1, 'so': 3, 'to': 8, 'ground': 1, 'come': 1, 'The': 2, 'civil': 1, 'new': 2, 'they': 3, 'created': 1, 'these': 2, 'altogether': 1, 'shall': 3, 'testing': 1, 'fought': 1, 'last': 1, 'world': 1, 'final': 1, 'of': 5, 'but': 1, 'score': 1, 'it': 2, 'under': 1, 'men': 2, 'fitting': 1, 'battle': 1, 'will': 1, 'freedom': 1, 'portion': 1, 'their': 1, 'full': 1, 'increased': 1, 'have': 5, 'resolve': 1, 'devotion': 2, 'dead': 3, 'earth': 1, 'war': 2, 'power': 1, 'here': 8, 'Now': 1, 'should': 1, 'never': 1, 'It': 3, 'perish': 1, 'brought': 1, 'government': 1, 'unfinished': 1, 'highly': 1, 'proposition': 1, 'dedicated': 4, 'say': 1, 'or': 2, 'people': 3, 'cause': 1, 'which': 2, 'little': 1, 'our': 2, 'live': 1, 'long': 2, 'this': 4, 'is': 3, 'dedicate': 2, 'resting': 1, 'years': 1, 'remaining': 1, 'fathers': 1, 'can': 5, 'take': 1, 'those': 1, 'might': 1, 'thus': 1, 'But': 1, 'in': 4, 'for': 5, 'all': 1, 'field': 2, 'us': 3, 'died': 1, 'engaged': 1, 'do': 1, 'any': 1, 'great': 3, 'did': 1, 'struggled': 1, 'birth': 1, 'gave': 2, 'nor': 1, 'honored': 1, 'sense': 1}


