"""input: a formula in -CNF with variables
Guess an initial assignment ,
uniformly at random
Repeat times:
If the formula is satisfied by the actual
assignment: stop and accept
Let be some clause not being satisfied by
the actual assignment
Pick one of the literals in the clause
at random and flip its value
in the current assignment"""
import random

def openArchive():
    # abrir archivo
    archivo = open("K-SAT.txt", "r")

    # leer el contenido del archivo
    legend = archivo.read()

    renglones = legend.split("\n")

    instructions = renglones[0].split(" ")

    opciones = []
    for x in range (0, int(instructions[2])):
        temp = bool(random.getrandbits(1))
        opciones.append(temp)
    clauses = []
    for x in range(1, int(instructions[3])+1):
        temp= [int(i) for i in renglones[x].split(" ")]
        temp.remove(0)
        clauses.append(temp)
    return opciones, clauses



opciones, clauses = openArchive()
comprobacion = []
for claus in clauses:
    rounds = 0
    while rounds <3*len(opciones):
        temp = []
        for i in range(0,len(claus)):
            if claus[i] < 0:
                temp.append(not opciones[(claus[i]*-1)-1])
            else:
                temp.append(opciones[claus[i]-1])
        if  True in temp:
            rounds = 3*len(opciones)
        else:
           x = random.randint(0,2)
           if claus[x] < 0:
               opciones[(claus[x]*-1)-1] = not opciones[(claus[x]*-1)-1]
           else:
               opciones[claus[x] - 1] = not opciones[claus[x] - 1]
        rounds +=1
    comprobacion.append(temp)

answer = True
for x in comprobacion:
    if True not in x:
        answer = False
if answer:
    print("A valid sequence for the %d variables is:" % len(opciones))
    print(opciones)
else:
    print("No valid sequence found")
