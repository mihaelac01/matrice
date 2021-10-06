matrice=[[38,56,19,97,6],
[21,37,84,14,58],
[3,67,53,42,18],
[44,27,54,4,73],
[36,6,16,1,72]]

s=[]
for a in range(len(matrice)):
    s.append(sum(matrice[a]))
print('Suma elementelor pe fiecare linie:',s)

suma=[]
coloana=[]
for k in range(len(matrice[0])):
    for rand in matrice:
        coloana.append(rand[k])
        suma.append(sum(coloana))
print("Suma elementelor pe fiecare coloana:",suma)

diagonala_principala=[]
for a in range(len(matrice)):
    for k in range(len(matrice[0])):
        if a==k:
            diagonala_principala.append(matrice[a][k])
print("diagonala principala:",diagonala_principala)

diagonala_secundara=[]
for a in range(len(matrice)):
    for k in range(len(matrice[0])):
        n=5
        if a+k==n-1:
            diagonala_secundara.append(matrice[a][k])
print("diagonala secundara:", diagonala_secundara)



