import os
from os import listdir
from os.path import join

from dictionary import Dictionary, DictionaryUtil

DICTIONNATIES_FOLDER = 'dictionaries'
dirs = [d for d in listdir(DICTIONNATIES_FOLDER) if os.path.isdir(join(DICTIONNATIES_FOLDER, d))]
dictionaries = []

for dir in dirs:
    print(f'Merge {dir} ...')
    path = join('dictionaries', dir)
    dictionary = Dictionary()
    dictionary.load(path)
    dictionaries.append(dictionary)

dictionary = DictionaryUtil.merge(dictionaries)
dictionary.save('dictionary')
print('Finish')
