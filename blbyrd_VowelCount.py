# Brandon L. Byrd
# COMP 163/004
# May 3, 2022
#This assignement uses recursion to count words and vowels (including y under certian conditions) by using recursion.

vowels = 'aeiou' #will be used in line 39 to count y's

def recursiveSplit(inputStr): #basically .split(' ') but with recursion
  i = inputStr.find(' ')
  if i == -1:
    return [inputStr,]
  else:
    return [inputStr[:i],] + recursiveSplit(inputStr[i+1:])

def vowelCount(str,vowel): #fuction for counting each vowel (takes the string and the vowel in question as parameters) 
  if str == '':
    return 0
  if str[0].lower() in vowel:
    return 1 + vowelCount(str[1:],vowel)
  else:
     return vowelCount(str[1:],vowel)

def lastConsonant(word): #function to find the last consonant in a word 
  rstr = word[::-1]
  for letter in rstr:
    if ((not letter in vowels) and (letter != 'y')) and letter.isalpha():
      return (rstr.index(letter)+1) * -1

def lastVowel(word): #function to find the last vowel in a word
  rstr = word[::-1]
  for letter in rstr:
    if ((letter in vowels) and (letter != 'y')) and letter.isalpha():
      return (rstr.index(letter)+1) * -1

def sometimesY(thisList): #funtion to count y's based on certain conditions
  if thisList == []:
    return 0 #base case
  elif 'y' in thisList[0]: #word has a y?
    if not any(char in vowels for char in thisList[0]): #if there is no other vowel in the word
      return 1 + sometimesY(thisList[1:])
    elif thisList[0][-1] == 'y': #if y is the last letter in the word
      return 1 + sometimesY(thisList[1:])
    elif thisList[0][0] == 'y': #if y is the first letter in the word after the other cases are true, i will not count it. the rest won't execute because its not applicable
      return sometimesY(thisList[1:]) #onto the next word
    elif (thisList[0][lastConsonant(thisList[0])+1]) == 'y': #if y follows the last consonant
      return 1 + sometimesY(thisList[1:])
    elif (thisList[0][lastVowel(thisList[0])+1]) == 'y': #if y follows the last vowel
      return 1 + sometimesY(thisList[1:]) 
    else: #on to the next word
      return sometimesY(thisList[1:])
  else: #on to the next word
    return sometimesY(thisList[1:])

def wordCount(words): #function to count words
  wordCountList = words[:]
  if wordCountList == []:
    return 0
  else:
    return 1 + wordCount(wordCountList[1:])

passage = input("\nEnter your string here: ") #user input
wordList = recursiveSplit(passage) #splits the passage to be used for word count
passageWordCount = wordCount(wordList) #counts the words

print(f'\nYour word count: {passageWordCount}')
print(f"\nNumber of vowels: {vowelCount(passage,'a') + vowelCount(passage,'e') + vowelCount(passage,'i') + vowelCount(passage,'o') + vowelCount(passage,'u') + sometimesY(wordList)}") 
print(f"  Number of a's: {vowelCount(passage,'a')}")
print(f"  Number of e's: {vowelCount(passage,'e')}")
print(f"  Number of i's: {vowelCount(passage,'i')}")
print(f"  Number of o's: {vowelCount(passage,'o')}")
print(f"  Number of u's: {vowelCount(passage,'u')}")
print(f"  Number of y's (as vowels): {sometimesY(wordList)}\n")



