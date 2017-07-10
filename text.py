# import pandas as pd 

#This function will get all the words out of the text document and into a list 
def get_words(text_files):
  words =[]
  with open(text_files,'r') as text:
      for line in text:
          for word in line.split():
             words.append(word)
  return words

#This function will get the word counts of each specific word. 
def get_word_count(words):
  word_and_count = {}
  len_count = 0
  #looping through the list
  while len_count < len(words):
    word_count = 0
    #I assign the current_word to the current position of the word_count counter 
    current_word = words[len_count].lower()
    #I then loop through the words again seeing is certain conditions are met. 
    for word in words:
      #Here I purge out words that I really do not care for. They are words that are common in the English language and 
      #Are needed basically to hold the language together. Thus, they are going to appear quite frequently. 
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
      and current_word != 'what' and current_word != 'those' and current_word != 'always' and current_word != 'So'
      and current_word != 'Again' and current_word != 'And' and current_word != 'As' and current_word != 'Go' 
      and current_word != 'well' and current_word != 'have' and current_word != 'has' and current_word != 'all'
      and current_word != 'must'):
        word_count += 1
        word_and_count[current_word] = word_count
    len_count += 1 
  #Turning the dictionary into a Dataframe so that it will be easier to work with.
  #Keeping this here for future reference. 
  #word_and_count = pd.DataFrame(list(word_and_count.items()), columns=['Word', 'Count'])
  return word_and_count

#This function is needed to sort out the specific words from their dictionaries into two seperate list. The first 
#list will hold the word, the second list will hold the counts for each word. I don't really think that this could 
#have been done in the get_word_count_function because I would still need seperate lists for each text file. 
def sort_words(text_dict_list):
  #Setting up a counter variable
  count = 0
  #creating all of the list that will hold the values from the dictionary. Each text file has to have two list. One 
  #to hold the words and the second to hold the values. 
  getty_word = []
  getty_count = []
  dream_word = []
  dream_count = []
  military_word = []
  military_count = []
  #This while loop will go through each of the dictionaries that the text_dict_list contains. 
  while count < len(text_dict_list):
    if count == 0:
      for key,value in text_dict_list[count].items():
        if value > 2:
          getty_word.append(key)
          getty_count.append(value)
    if count == 1:
      for key,value in text_dict_list[count].items():
        if value > 10:
          dream_word.append(key)
          dream_count.append(value)
    if count == 2:
      for key,value in text_dict_list[count].items():
        if value > 8:
          military_word.append(key)
          military_count.append(value)
    count += 1 
  
  return getty_word, getty_count, dream_word, dream_count, military_word, military_count



#This is the main function that will run the program. 
def main_text():
  #Creating a list to hold all of the text documents
  text_files = ['gettysburg.txt', 'dream.txt', 'military.txt']
  #Setting a counter to 0 which I will use in the while loop below
  count = 0
  #This while loop will continue to loop through the length of the text_files list. The goal is to have 
  #only one set of above functions to get me back different values series for each of the text documents.
  while count < len(text_files):
    if count == 0:
      document = text_files[count]
      words = get_words(document)
      getty_word_and_count = get_word_count(words)
    elif count == 1:
      document = text_files[count]
      words = get_words(document)
      dream_word_and_count = get_word_count(words)
    elif count == 2:
      document = text_files[count]
      words = get_words(document)
      military_word_and_count = get_word_count(words)
    count += 1

  #Here I place the dictionaries that I have into a list which will be used to pass all the dictionaries 
  #into a function.
  text_dict_list = [getty_word_and_count, dream_word_and_count, military_word_and_count]
  #The sort words function will get the specific count of words and their counts in two seperate list 
  #for use with Pandas. 
  getty_word, getty_count, dream_word, dream_count, military_word, military_count = sort_words(text_dict_list)
  return getty_word, getty_count, dream_word, dream_count, military_word, military_count 


  # print(getty_word)
  # print(getty_count)
  # print(dream_word)
  # print(dream_count)
  # print(military_word)
  # print(military_count)

#Here I call the main function to run the program. 
main_text()


#SCRAP CODE 
#print(getty_word_and_count)
#print(getty_word_and_count.iloc[3][0]) #This gets word
#print(getty_word_and_count.iloc[3][1]) #This gets the number of times the word is repeated




