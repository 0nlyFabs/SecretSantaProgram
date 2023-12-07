#The complex part, here we will take the list and assign each person in the list to someone else. They cannot have their own name
#possible issues that may happen are people with the same name, i.e. Sam and Sam, in this case we need to specify something to distinguish them, i.e Sam A and Sam B

import random

def random_assignment(list):

    secretsantanameslist = list
    len_santa = len(secretsantanameslist)

    i = 0

    blocked_names = []
    
    print('There are', len_santa, 'names in the list')

    while i < len_santa:
        while True:
            ran_var = random.randint(0, len_santa-1)
            if i != ran_var and ran_var not in blocked_names:
                blocked_names.append(ran_var)
                print(secretsantanameslist[i], 'will get', secretsantanameslist[ran_var], 'a gift for Secret Santa') 
                break  
        i+=1

    print('Thanks for playing!')