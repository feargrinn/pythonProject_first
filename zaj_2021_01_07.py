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