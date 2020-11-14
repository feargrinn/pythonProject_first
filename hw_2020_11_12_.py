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
for element in (range(1000000)):
    if long_list[element] == -1:
        break
time_end = time.time()
time_liniowe = time_end - time_start
print("czas przeszukiwania liniowego listy: " + str(time_liniowe) + "\n")


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