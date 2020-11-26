# testy

txt_file = None
try:
    division_result = int(input('dzielna: ')) / int(input('dzielnik: '))
    txt_file = open('plik.txt', 'w')
    txt_file.write('wynik dzielenia: ')

    txt_file.write(str(division_result))
    txt_file.close()
except (IOError, ZeroDivisionError) as e:
    print(e)
    if txt_file:
        txt_file.close()



try:
    with open('plik.txt', 'w') as txt_file:
        txt_file.write('wynik dzielenia: ')
        division_result = int(input('dzielna: ')) / int(input('dzielnik: '))
        txt_file.write(str(division_result))
        txt_file.close()
except (IOError, ZeroDivisionError) as e:
    print(e)

# zad 7
# proszę na dowolnej funkcji przetestować parametry pozycyjne, z nazwami, *args i **kwargs. Sprawdzić w jakiej kolejności mogą być ustawiane. Czy można bez błędu wywołać poniższą funkcję bez wprowadzania w niej zmian.

def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name,last_name,age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)
# nie wypisuje bledow

# testowanie
def person_print(name, last_name, *others, age, **key_others):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name,last_name,age)
    others_str = ' '
    key_others_str = ' '
    for arg in others:
        others_str += arg + ' '
    for value in key_others.values():
        key_others_str += value + ' '
    print(formatted_data)
    print(others_str)
    print(key_others_str)

person_print('imie','nazwisko', 15,'jan', pesel=999999,  imie2='karol', age=44)

# zad 8
# Proszę otworzyć plik i zapisać do niego dowolne dane, a następnie bez zamykania go spróbować odczytać jego zawartość.


txtfile = open('plik.txt','w+')
txtfile.write('some text \n:)\n')
txtfile.seek(0)
print(txtfile.read())
txtfile.close()


# zad 9
# Za pomocą with open( ) proszę odczytać zawartość jednego pliku i zapisać w drugim. Proszę uwzględnić obsługę wyjątków.

try:
    with open('plik.txt','r+') as txtfile:
        txtfile2=open('plik2.txt','w+')
        txtfile2.write(txtfile.read())
        txtfile2.close()
except (IOError) as e:
    print(e)
