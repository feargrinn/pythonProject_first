import re

bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''

#########################################################

# search, findall, finditer

pattern_1 = re.compile('Niebieski')
# result_1 = pattern_1.findall(bridge_of_death)
# result_2 = pattern_1.search(bridge_of_death)
result_3 = pattern_1.finditer(bridge_of_death)

# print(type(result_1))
# for substring in result_1:
#     print(substring)
#
# print(type(result_2))
# print(result_2)
#
# print(type(result_3))
# for substring in result_3:
#     print(substring.start(), substring.end(), substring.group(), substring.span()[0], substring.span()[-1])

for count, substring in enumerate(result_3, 1):
    print("Dopasowanie {}: {}".format(count, substring.span()))

# <class 'callable_iterator'>
# <re.Match object; span=(34, 43), match='Niebieski'>
# <re.Match object; span=(192, 201), match='Niebieski'>

#########################################################

# print(bridge_of_death)

pattern_1 = re.compile('-Jaki', re.IGNORECASE)
result_0 = pattern_1.match(bridge_of_death)
print(result_0)
# match returned: None

pattern_1 = re.compile('\n-Jaki', re.IGNORECASE)
result_0 = pattern_1.match(bridge_of_death)
print(result_0)

pattern_1 = re.compile('Niebieski.', re.IGNORECASE)
result_0 = pattern_1.finditer(bridge_of_death)
for substring in result_0:
    print(substring)

pattern_1 = re.compile('Niebieski.$', re.MULTILINE)
result_0 = pattern_1.finditer(bridge_of_death)
for substring in result_0:
    print(substring)

#########################################################

var_name = input('podaj nazwe: ')
pattern_var = re.compile(r'^[a-z_][a-z_A-Z0-9]*$')
result_var = pattern_var.search(var_name)
if result_var:
    result_word = result_var.group()
    if re.match(r'_+$', result_word):
        print('niby moze ale nie probuj')
    else:
        print('input moze byc nazwa zmiennej'.format(result_word))
else:
    print('input nie moze byc nazwa zmiennej'.format(var_name))

#########################################################

# zadanie
# znajdz wszystkie wyrazy ktore skladaja sie z przynajmniej 4 znakow
pattern_four = re.compile(r'/b/w/w/w/w+/b')