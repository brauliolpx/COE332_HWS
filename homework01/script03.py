import names

name_of_pep = []
individuals = []
i = 0

for i in range (5):
    name_of_pep.append(names.get_full_name())
    length = len(name_of_pep[i]) - 1 
    print(name_of_pep[i] + ' ' +  str(length))


