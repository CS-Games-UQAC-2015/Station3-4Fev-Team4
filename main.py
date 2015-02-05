import sys


listCases = []
number = 0

#Parse the input file
with open(sys.argv[1],'r') as file:
    listCases = file.readlines()
    number = int(listCases.pop(0))
    
for i in range(0,number):
    splitted = listCases[i].split('/')
    pq = int(splitted[0]) / float(splitted[1]) #pq is the variable representing P/Q
    #print(pq)
    
    #Mon idée est que nous devrions construire l'arbre à l'envers. On trouve ses parents immédiats:
    #Si elle est P/Q > 0.5, elle a nécessasirement un parent 1 et un parent P/Q - (1 - P/Q)
    #Si elle est P/Q < 0.5, elle a nécessairement un parent 0 et un parent P/Q + P/Q
    #On veut des parents aux extrêmes
    

    