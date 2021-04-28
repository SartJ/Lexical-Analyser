# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 06:01:09 2021

@author: sartaj
"""

import re

list_of_inputs = []
with open('input.txt', 'r') as file:
    list_of_inputs = file.readlines()

# print(list_of_inputs)


# List of Java Access modifiers:-
a_mods = ['public', 'private', 'protected', '', 'default']

# List of Java Non-Access modifiers:-
na_mods = ['final', 'static', 'abstract', 'transient', 'synchronized', 'volatile', '']

# List of Return Types:-
reTypes = ['char','byte','short','int','long','boolean','float','double', 'void']


def splat(word):
    return [char for char in word]

def returnTypeFinder(m):
    
    for i in reTypes:
        x = m.find(i)
        if x >-1:
            return i
    
method_lines = []
# print("Here are all the methods:")
for words in list_of_inputs:
    word_list = words.split()
    last_word = word_list[len(word_list)-1]
    chars = splat(last_word)
    
    if chars[len(chars)-1] == ')' or ((chars[len(chars)-1]=='{') and chars[len(chars)-2]==')'):
        # print(words)
        method_lines.append(words)
# print(method_lines)



print("Methods:")
for i in method_lines:
    txt = i
    
    ret_typ = returnTypeFinder(txt)
    # (char|byte|void|double|float|boolean|long|int|short)*
    x = re.search(r"\b(?!main\b)\w+\(((char|byte|void|double|float|boolean|long|int|short) \w+, (char|byte|void|double|float|boolean|long|int|short) \w+)*\)*", txt)
    if x != None:
        print(x.group(0) + ", return type: "+ ret_typ)
