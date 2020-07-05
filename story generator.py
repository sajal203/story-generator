# -*- coding: utf-8 -*-
import random
from time import sleep

mainchar=(input('main character: '))
rivalchar=(input("rival's name: "))
activity=(input('daily activity (e.g: watching tv) :- '))
posadj=(input('positive adjective(e.g. funny etc.):- '))
negadj= input('negative adjective(e.g. carless etc.):- ')

word1 =['question','code','comment']
word2=['penguins','programmer jokes','text generation']
word3=['C#','C++','python','javascript']
word4=['liked','disliked','reported','deleted']

sentence=['yesterday, while browsing check to learn and','activity', ',', 'mainchar', 'noticed that', 
          'rivalchar', 'posted a new', 'word1', 'about', 'word2', '. He', 'word4', 'and challanged him to a', 
          'word3', 'battle. Theen he posted his own', 'posadj', ' ', 'word1', ', but', 'rivalchar', 'retaliated with his', 
          'negadj', ' ', 'word1', 'about', 'word2', '.']

for item in sentence: 
    if item == 'activity': sentence[sentence.index(item)] = activity
    elif item == 'mainchar': sentence[sentence.index(item)] = mainchar
    elif item == 'rivalchar': sentence[sentence.index(item)] = rivalchar
    elif item == 'posadj': sentence[sentence.index(item)] = posadj
    elif item == 'negadj': sentence[sentence.index(item)] = negadj
    
    elif item == 'word1':
        index = sentence.index(item)
        sentence[index] = random.choice(word1)
    elif item == 'word2' : sentence[sentence.index(item)] = random.choice(word2)
    elif item == 'word3' : sentence[sentence.index(item)] = random.choice(word3)
    elif item == 'word4' : sentence[sentence.index(item)] = random.choice(word4)
    
    else:continue
    
story = " ".join(item for item in sentence)
sleep(1)
print(story)
