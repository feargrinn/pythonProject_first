# Zadanie 3
# Wykorzystując pętle, break i else (else użyte w połączeniu z break) proszę napisać program, w którym użytkownik w przeciągu skończonej liczby prób ma odgadnąć ustawione wcześniej słowo. W przypadku, kiedy mu się uda program ma wypisać gratulacje, a jeśli skończy się liczba prób to poinformować o przegranej.

slowo = "chmurka"
for x in (range(10)):
    print("pozostalo ",(10-x)," prob.")
    slowo_uzytkownika = input("odgadnij slowo: ")
    if slowo_uzytkownika == slowo:
        print("udalo sie :) poprawna odpowiedz to " + slowo + ".")
        break
    else:
        if x == 9:
            print("skonczyla sie liczba prob :(")
            break
        print("nie udalo sie :( sprobuj ponownie.")

###########################################################################
slowo = "chmurka"
for x in range(3):
    slowo_uzytkownika = input("odgadnij slowo: ")
    if slowo_uzytkownika == slowo:
        print("udalo sie")
        break
else:
    print("skonczyla sie liczba prob")




# Zadanie 4
# Proszę sprawdzić czas potrzebny na przeszukanie poniższej listy pod kątem -1. Proszę zastosować wszystkie sposoby przeszukania, które przyjdą do głowy.
#
# from random import randint
# long_list = [randint(0, 3000) for element in range(1000000)]

from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]
import time

# przeszukiwanie liniowe
time_start = time.time()
for element in range(1000000):
    if long_list[element] == -1:
        break
time_end = time.time()
time_total = time_end - time_start
print("czas przeszukiwania liniowego listy: " + str(time_total) + "\n")

# przeszukiwanie binarne
long_list.sort()

def bin_search(lista, start, end, szukany):
    if end >= start:
        middle = (start + end)//2
        if lista[middle] == szukany:
            return middle
        elif lista[middle] > szukany:
            return bin_search(lista, start, middle - 1, szukany)
        else:
            return bin_search(lista, middle + 1, end, szukany)
    else:
        return -1

time_start = time.time()
result = bin_search(long_list, 0, 1000000-1, -1)
time_end = time.time()
time_total = time_end - time_start
print("czas przeszukiwania binarnego listy: " + str(time_total) + "\n")

# long_list = [randint(0, 3000) for element in range(1000000)]
# time_start = time.time()
# long_list.sort()
# result = bin_search(long_list, 0, 1000000-1, -1)
# time_end = time.time()
# time_total = time_end - time_start
# print("czas przeszukiwania binarnego listy z wliczonym czasem sortowania listy: " + str(time_total) + "\n")

# jump search
long_list.sort()
import math
def jump_search(lista, dlugosc, szukany):
    skok = math.isqrt(dlugosc)
    start = 0
    end = skok
    while lista[end] < szukany:
        start += skok
        end += skok
        if start >= dlugosc:
            return -1
    while lista[start] < szukany:
        start += 1
        if start >= end:
            return -1
        elif lista[start] == szukany:
            return start
    return -1

time_start = time.time()
result = jump_search(long_list, 1000000, -1)
time_end = time.time()
time_total = time_end - time_start
print("czas przeszukiwania listy metoda jump search: " + str(time_total) + "\n")


# Zadanie 5.1
# Za pomocą list comprehension proszę stworzyć listę z pierwszych liter imion w liście ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa'].

lista_imion = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
lista_pierwszych_liter = [element[0] for element in lista_imion]
print(lista_pierwszych_liter)

# Zadanie 5.2
# Za pomocą list comprehension proszę stworzyć listę o długości 5, której każdy element  będzie listą zawierającą 4 losowe liczby całkowite z przedziału od 1 do 10.

from random import randint
lista5 = [[randint(1,10) for x in range(4)] for element in range(5)]
print(lista5)

# Zadanie 6
# Proszę tak skopiować poniższy słownik, żeby di['four'][0] = 'cztery' nie powodowało zmiany w kopii.
#
# di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}

di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
di_copy = di.copy()
di_backup = dict(di)
import copy
di_deepcopy = copy.deepcopy(di)
print("slowniki przed: ")
print(di)
di['four'][0] = 'cztery'
print("slowniki po: ")
print("di: ",di)
print("di_copy: ",di_copy)
print("di_backup: ",di_backup)
print("di_deepcopy: ",di_deepcopy)