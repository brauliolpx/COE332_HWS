import names

name_of_pep = []
individuals = [] 
i = 0

while True: 
    name_of_pep.append(names.get_full_name())
    if (len(name_of_pep[i]) == 9):
        individuals.append(name_of_pep[i])
    if (len(individuals) == 5):
        break 
    i += 1

print (individuals)


 

 



