import math
import numpy as np
""" 
UKOL: Doplňte následující kód tak, aby 
1) smyčka iterovala od 1 do 20 včetně
2) vypsal aktuální i
3) pokud je aktuální i sudé, vypsal na dalším řádku "Sudé číslo"
4) pokud je aktuální i liché, vypsal na dalším řádku "Liché číslo"

K určení toho, zda je číslo sudé, potřebujete modulo operátor % - zbytek po 
celočíselném deleni. (zbytek = delenec % delitel) 

for i in range(20):
    if(i%2==0): print(i,"Sude cislo")
    else: print(i,"Liche cislo")

"""
"""
ÚKOL: 
1) Vytvořte matici A samých nul, která má 4 řádky a 3 sloupce.
2) Vytvořte náhodný vektor b o čtyřech prvcích.
3) Vytvořte vektor v obsahující 10 čísel rovnoměrně rozmístěných mezi 0 a 5 včetně.
b = np.random.rand(4)
print(b)

A = np.zeros((4,3))
print(A)

v = np.linspace(0,5,10)
print(v)
"""
"""
ÚKOL: 
1) Vytvořte náhodnou matici o rozměrech 5x5.
2) Do vektoru v uložte poslední řádek matice, vektor vytiskněte.
3) Do vektoru u uložte prvky na druhém řádku matice v prvním a posledním sloupci, vytiskněte.
h = np.random.rand(5,5)
print(h)

v = h[4,0:5] 
print(v)

u = h[1,(0,4)] 
print(u)
"""
"""
ÚKOL: 
1) Vytvořte náhodný sloupcový vektor x délky 5 a náhodný řádkový vektor y délky 5
2) Pomocí vhodných funkcí z knihovny NumPy určete 
    - normu vektoru x
    - skalární součin vektoru y s vektorem x
    - součet vektoru x s transpozicí vektoru y
    
    x = np.random.rand(5,1)
y = np.random.rand(1,5) 

norm = 0
for i in range(5):
    norm += x[i]*x[i]
print(math.sqrt(norm))
#-------------------------
print(np.linalg.norm(x))

skal = 0
for i in range(5):
    skal += x[i]*y[0][i]
print(skal)
#-------------------------
print(np.matmul(y,x))

trans = np.zeros(5)
y = y.T
for i in range(5):
    trans[i] += x[i]+y[i]
print(trans)
y = y.T
#-------------------------
s = x + np.transpose(y)
print(s)
ÚKOL:
Vypočítejte nyní normu vektoru x a skalární součin y*x "manuálně" pomocí cyklů for.
"""

def muj_matvec(A, x):
    y = np.zeros(4)

    print(J)
    print(x)

    for i in range(4):
        for j in range(4):        
            y[i] += J[i][j]*x[j]
    return y

B = np.linspace(0,1,4)
J = np.zeros((4,4))
for i in range(4):
    for j in range(4): 
        J[i][j] = B[i]

x = np.array([0, 1, 2, 3])

print(muj_matvec(J, x))
print(J @ x)
"""
ÚKOL:
Do funkce muj_matvec implementujte vaši verzi násobení matice s vektorem.
Využijte dvě vnořené smyčky for. Na vstupu bude matice A a sloupcový vektor x 
odpovídající délky. Funkce bude vracet vektor y = Ax.
"""
import time

A = np.random.rand(500, 500)
x = np.random.rand(500, 1)

# otestujeme vaši implementaci 
st = time.time()
y = muj_matvec(A, x)
et = time.time()
print(y)
your_time = et - st

# otestujeme zabudovanou implementaci
st = time.time()
yy = A @ x
et = time.time()
print(yy)
numpy_time = et - st

print("Čas výpočtu pomocí vaší funkce: {} sekund".format(your_time))
print("Čas výpočtu pomocí numpy funkce: {} sekund".format(numpy_time))

