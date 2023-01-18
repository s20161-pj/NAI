#Bulding a ChatBot with Deep NLP

#Importing the libraries
import numpy as np
import tensorflow as tf
import re
import time

#Importing the dataset
lines = open('movie_lines.txt', encoding ='utf-8', errors = 'ignore').read().split('\n')
conversations = open('movie_conversations.txt', encoding ='utf-8', errors = 'ignore').read().split('\n')

#Creating a dictionary taht maps each line and its id
id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]
        
#Creating a list of all of the conversations
conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ","")
    conversations_ids.append(_conversation.split(','))

#Getting separately the questions and the answers
questions = []
answers = []
for conversation in conversations_ids:
        for i in range(len(conversation)-1):
            questions.append(id2line[conversation[i]])
            answers.append(id2line[conversation[i+1]])
            