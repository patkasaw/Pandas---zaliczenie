#Zadanie 1:

import numpy as np
import pandas as pd

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog',
        'dog'],
        'name': ['Daisy', 'Bella', 'Noodle', 'Charlie', 'Max', 'Molly', 'Draco', 'Kenzo',
        'Milo', 'Cooper'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

animals = pd.DataFrame(data, index = labels)
print(animals)
animals.info()

#Zadanie 2: 

#a) pierwsze 3 wiersze
print(animals[0:3])

#b) kolumny 'animal' i 'age'
print(animals['animal'])
print(animals['age'])

#c) dane z wierszy 3, 4 i 8, zawarte w kolumnach 'visits' i 'priority'
print(animals.loc[['d', 'e', 'i'], ['visits', 'priority']])

#d) wiersze, w których liczba wizyt jest większa niż 2,
mask = animals['visits'] > 2
print(animals[mask])

#e) wiersze, w których zwierzęciem jest kot i ma mniej niż 4 lata
mask = animals['animal'] = 'cat' and animals['age'] < 4
print(animals[mask])

#f) wiersze, w których wiek zwierzęcia mieści się w przedziale od 2 do 4 lat (włącznie).
mask = (animals['age'] >= 2) & (animals['age'] <= 4)
print(animals[mask])

#Zadanie 3:
#a) dodaj do niej wiersz o indeksie 'k', zawierający informacje o nowym zwierzęciu – psie, wabiącym 
#się Buddy, w wieku 5.5 roku, któy odwiedził gabinet 2 razy w zwykłym trybie

animals.loc['k'] = {'animal': 'dog',
        'name': 'Buddy',
        'age': 5.5,
        'visits': 2,
        'priority': 'no'}

#b) dodaj do niej kolumnę 'price', zawierającą wartość 10 dla pacjentów zwykłych i 20 dla pacjentów priorytetowych
animals['price'] = np.where(animals['priority'] == 'yes', 20, 10)


#c) dodaj do niej kolumnę 'total', zawierajacą całkowity koszt wszystkich wizyt,
animals['total'] = animals['visits'] * animals['price']


#d) usuń z niej kolumnę 'priority'
animals.drop('priority', axis=1, inplace=True)

#e) zmień nazwę kolumny 'animal' na 'species',
animals = animals.rename(columns = {'animal' : 'species'})
print(animals)

#Zadanie 4
#a) przywróć ramce danych domyślny indeks całkowity, sprawiając jednocześnie, by nie została dodana
#nowa kolumna z wcześniejszymi wartościami indeksu
animals.reset_index(drop=True)
print(animals)

#b) utwórz indeks z kolumny 'name'
animals.set_index('name', inplace = True)
print(animals)

#c) usuń z ramki danych wiersz, zawierający informacje o psie, wabiącym się Max
animals.drop('Max', inplace = True)
print(animals)

#d) przywróć ramce danych domyślny indeks całkowity, sprawiając jednocześnie, by z istniejącego
#indeksu uczynić kolumnę danych w ramce
animals.reset_index(inplace = True)
print(animals)

#Zadanie 5:
#a) zamień w kolumnie 'species' ciągi znaków na pisane samymi wielkimi literam
animals['species'] = animals['species'].str.upper()
print(animals)

#b) zapisz tę ramkę danych do pliku CSV o nazwie 'animals.csv' – spraw, by nie zawierał on niejawnych
#(numerycznych) indeksów wierszy
animals.to_csv('animals.csv', index = False)

#c) odpowiednim poleceniem systemu operacyjnego wyświetl zawartość utworzonego pliku
animals = pd.read_csv('animals.csv')
print(animals)
