# -*- coding: utf-8 -*-
"""participantstep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19hJNFyievqhlIWjwarENlexHdHQIdiDG
"""

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import random
import math
import scipy.optimize as resol
import scipy.integrate as integr
import time

q = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71}

k = len(q)
print(k)
k
p_ = [random.randint(2, 100) for _ in range(len(q))]
time.sleep(1)
p_
x1i = random.randint(1, len(q) - 1)
x1i
x2i = random.randint(1, len(q) - 1)
x2i
y1i = random.randint(1, len(q) - 1)
y1i
y2i = random.randint(1, len(q) - 1)
y2i
zi = random.randint(1, len(q) - 1)
zi
beta0i = random.randint(1, len(q) - 1)
beta0i
beta1i = random.randint(1, len(q) - 1)
beta2i = random.randint(1, len(q) - 1)
beta3i = random.randint(1, len(q) - 1)
beta4i = random.randint(1, len(q) - 1)
gamma1 = random.randint(1, len(q) - 1)
gamma2 = random.randint(1, len(q) - 1)
z = random.randint(1, len(q) - 1)

print(beta1i)
print(beta2i)
print(beta3i)
print(beta4i)
print(z)
print(gamma1)
print(gamma2)

p = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
     113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199}

g1 = random.randint(1, len(p) - 1)
g2 = random.randint(1, len(p) - 1)
print(g1)
print(g2)

h1 = pow(int(g1), int(gamma1))
print("La valeur de h1 est :", h1)

h2 = pow(int(g2), int(gamma2))
print("La valeur de h2 est :", h2)

# Compute private key sk
x1 = random.randint(1, 100)
x2 = random.randint(1, 100)
y1 = random.randint(1, 100)
y2 = random.randint(1, 100)
z = random.randint(1, 100)

sk = (x1, x2, y1, y2, z)

print(" sk =", sk)

E1i = pow(int(g1), int(x1i)) * pow(int(h1), int(beta1i))
E2i = pow(int(g1), int(y1i)) * pow(int(h1), int(beta2i))
E3i = pow(int(g2), int(x2i)) * pow(int(h2), int(beta3i))
E4i = pow(int(g2), int(y2i)) * pow(int(h2), int(beta4i))
E5i = pow(int(g1), int(zi))
print("La valeur de E1i est :", E1i)
print("La valeur de E2i est :", E2i)
print("La valeur de E3i est :", E3i)
print("La valeur de E4i est :", E4i)
print("La valeur de E5i est :", E5i)

# Diffuser les valeurs E1i, E2i, E3i, E4i et E5i
broadcast_data = (E1i, E2i, E3i, E4i, E5i)

print(broadcast_data)

t = 5

# Génère aléatoirement les coefficients des polynômes
f_coef = np.random.randint(0, 10, size=t + 1)
f_prime_coef = np.random.randint(0, 10, size=t)
g_coef = np.random.randint(0, 10, size=t + 1)
g_prime_coef = np.random.randint(0, 10, size=t)
h_coef = np.random.randint(0, 10, size=t + 1)
h_prime_coef = np.random.randint(0, 10, size=t)

# Crée des objets de polynômes à partir des coefficients générés
f = np.poly1d(f_coef)
f_prime = np.poly1d(f_prime_coef)
g = np.poly1d(g_coef)
g_prime = np.poly1d(g_prime_coef)
h = np.poly1d(h_coef)
h_prime = np.poly1d(h_prime_coef)

print("Le polynôme f(x) est :", f)
print("Le polynôme f'(x) est :", f_prime)
print("Le polynôme g(x) est :", g)
print("Le polynôme g'(x) est :", g_prime)
print("Le polynôme h(x) est :", h)
print("Le polynôme h'(x) est :", h_prime)

a_coef = np.random.rand(t + 1) * 10
b_coef = np.random.rand(t) * 10
a_prime_coef = np.random.rand(t + 1) * 10
b_prime_coef = np.random.rand(t) * 10
a_prime_prime_coef = np.random.rand(t + 1) * 10
b_prime_prime_coef = np.random.rand(t) * 10

# Crée des objets de polynômes à partir des coefficients générés
f = np.poly1d(a_coef)
f_prime = np.poly1d(b_coef)
g = np.poly1d(a_prime_coef)
g_prime = np.poly1d(b_prime_coef)
h = np.poly1d(a_prime_prime_coef)
h_prime = np.poly1d(b_prime_prime_coef)

print("Le polynôme f(x) est :", f)
print("Le polynôme f'(x) est :", f_prime)
print("Le polynôme g(x) est :", g)
print("Le polynôme g'(x) est :", g_prime)
print("Le polynôme h(x) est :", h)
print("Le polynôme h'(x) est :", h_prime)

x1i = np.random.randint(-10, 10)

# Génère aléatoirement les coefficients des termes du polynôme
f_coef = np.random.rand(t + 1) * 10
f_coef[0] = x1i - sum(f_coef[1:] * (-1) ** np.arange(1, t + 1))

# Crée un objet de polynôme à partir des coefficients générés
f = np.poly1d(f_coef)

print("Le polynôme f(x) est :", f)
print("f(-1) =", f(-1))

y1i = np.random.randint(-10, 10)

# Génère aléatoirement les coefficients des termes du polynôme
f_coef = np.random.rand(t + 1) * 10
f_coef[0] = y1i - sum(f_coef[1:] * (-2) ** np.arange(1, t + 1))

# Crée un objet de polynôme à partir des coefficients générés
f = np.poly1d(f_coef)

print("Le polynôme f(x) est :", f)
print("f(-2) =", f(-2))

beta1i = np.random.randint(-10, 10)

# Génère aléatoirement les coefficients des termes du polynôme
f_prime = np.random.rand(t + 1) * 10
f_prime[0] = beta1i - sum(f_prime[1:] * (-1) ** np.arange(1, t + 1))

# Crée un objet de polynôme à partir des coefficients générés
f = np.poly1d(f_prime)

print("Le polynôme f(x) est :", f)
print("f'(-1) =", f(-1))

beta2i = np.random.randint(-10, 10)

# Génère aléatoirement les coefficients des termes du polynôme
f_prime = np.random.rand(t + 1) * 10
f_prime[0] = beta2i - sum(f_prime[1:] * (-2) ** np.arange(1, t + 1))

# Crée un objet de polynôme à partir des coefficients générés
f = np.poly1d(f_prime)

print("Le polynôme f(x) est :", f)
print("f'(-2) =", f(-2))

x2i = np.random.randint(-10, 10)

# Génère aléatoirement les coefficients des termes du polynôme
g_coef = np.random.rand(t + 1) * 10
g_coef[0] = x2i - sum(g_coef[1:] * (-1) ** np.arange(1, t + 1))

# Crée un objet de polynôme à partir des coefficients générés
g = np.poly1d(g_coef)

print("Le polynôme g(x) est :", g)
print("g(-1) =", g(-1))

t = 5
y2i = np.random.randint(-10, 10)

# Génère aléatoirement les coefficients des termes du polynôme
g_coef = np.random.rand(t + 1) * 10
g_coef[0] = y2i - sum(g_coef[1:] * (-2) ** np.arange(1, t + 1))

# Crée un objet de polynôme à partir des coefficients générés
g = np.poly1d(g_coef)

print("Le polynôme g(x) est :", g)
print("g(-2) =", g(-2))

beta3i = np.random.randint(-10, 10)

# Génère aléatoirement les coefficients des termes du polynôme
g_prime = np.random.rand(t + 1) * 10
g_prime[0] = beta3i - sum(g_prime[1:] * (-2) ** np.arange(1, t + 1))

# Crée un objet de polynôme à partir des coefficients générés
g = np.poly1d(g_prime)

print("Le polynôme g(x) est :", g)
print("g'(-1) =", g(-1))

t = 5
beta4i = np.random.randint(-10, 10)

# Génère aléatoirement les coefficients des termes du polynôme
g_prime = np.random.rand(t + 1) * 10
g_prime[0] = beta4i - sum(g_prime[1:] * (-2) ** np.arange(1, t + 1))

# Crée un objet de polynôme à partir des coefficients générés
g = np.poly1d(g_prime)

print("Le polynôme g(x) est :", g)
print("g'(-2) =", g(-2))

t = 5
zi = np.random.randint(-10, 10)
a_prime_prime_coef = np.random.rand(t + 1) * 10
# Génère aléatoirement les coefficients des termes du polynôme
h_coef = np.random.rand(t + 1) * 10

h_coef[0] = (zi)

# Crée un objet de polynôme à partir des coefficients générés


print("Le polynôme h(x) est :", h_coef)

##########
import numpy as np

t = 5
beta0i = np.random.randint(-10, 10)
b_prime_prime_coef = np.random.rand(t) * 10
# Génère aléatoirement les coefficients des termes du polynôme
h_prime = np.random.rand(t + 1) * 10
h_prime[0] = (beta0i)

# Crée un objet de polynôme à partir des coefficients générés


print("Le polynôme h'(x) est :", h_prime)

a_coef = np.random.rand(t + 1) * 10
b_coef = np.random.rand(t) * 10
a_prime_coef = np.random.rand(t + 1) * 10
b_prime_coef = np.random.rand(t) * 10
a_prime_prime_coef = np.random.rand(t + 1) * 10
b_prime_prime_coef = np.random.rand(t) * 10

# Crée des objets de polynômes à partir des coefficients générés
f = np.poly1d(a_coef)
f_prime = np.poly1d(b_coef)
g = np.poly1d(a_prime_coef)
g_prime = np.poly1d(b_prime_coef)
h = np.poly1d(a_prime_prime_coef)
h_prime = np.poly1d(b_prime_prime_coef)

f_coef = np.random.randint(0, 10, size=t + 1)

g_coef = np.random.randint(0, 10, size=t + 1)

h_coef = np.random.randint(0, 10, size=t + 1)

# Calcule les termes de la somme CMik
t = 3
for k in range(t + 1):
    CMik = g_coef[k] * a_coef[k] * h_coef[k] * b_coef[k] * g_coef[k] * a_prime_coef[k] * h_coef[k] * b_prime_coef[k]
    print("La valeur de CMik est : ")
    print(CMik)

    cmik = g_coef[k] * a_prime_prime_coef[k] * h_coef[k] * b_prime_prime_coef[k]

    print("La valeur de cmik est : ")
    print(cmik)

    cmi0 = g_coef[k] * zi * h_coef[k] * beta0i

# for i in range(1, n+1):
# for tau in range(1, 3):
# for j in range(1, n+1):
# Yt = (tau + 2, i)
# for k in range(tau+1):
# E_tau_i = Yt * sum([CMik[-tau+k][i]])
# print(E_tau_i)


Qtemp = ['participant1', 'participant2', 'participant3', 'participant4',
         'participant5']  # Liste des participants qualifiés initiale

for i in Qtemp:
    Qtemp.remove(i)
    print("Participant Pi a été disqualifié. Nouvelle liste de participants qualifiés : ", Qtemp)
else:
    print("Le participanti n'est pas présent dans la liste des participants qualifiés.")

    n = 5
participants = ["P1", "P2", "P3"]
shares = {}


# Define some arbitrary functions
def fi(j):
    return j ** 2


def f_prime_i(j):
    return j ** 3


def gi(j):
    return 2 * j


def g_prime_i(j):
    return 3 * j


def hi(j):
    return j + 1


def h_prime_i(j):
    return j - 1


# Compute the shares for each participant and index
for i in range(1, n + 1):
    for participant in participants:
        sfij = fi(i)
        sf_prime_ij = f_prime_i(i)
        sgij = gi(i)
        sg_prime_ij = g_prime_i(i)
        shij = hi(i)
        sh_prime_ij = h_prime_i(i)

        shares[(participant, i)] = (sfij, sf_prime_ij, sgij, sg_prime_ij, shij, sh_prime_ij)

# Print the shares for a specific participant and index
print(shares[("P2", 3)])

import random

# Définir l'ensemble de valeurs possibles pour Sj
Sj = [100, 25, 63, 58, 77, 91]

# Choisir des valeurs aléatoires pour aj, bj, a'j, b'j, a''j et b''j
aj = random.choice(Sj)
bj = random.choice(Sj)
a_prime_j = random.choice(Sj)
b_prime_j = random.choice(Sj)
a_double_prime_j = random.choice(Sj)
b_double_prime_j = random.choice(Sj)

# Créer l'ensemble S'j à partir des valeurs aléatoires choisies
S_prime_j = {aj, bj, a_prime_j, b_prime_j, a_double_prime_j, b_double_prime_j}
print("s'j :", S_prime_j)

# Définir les constantes g1, g2, h1 et h2
g1 = 3
g2 = 5
h1 = 7
h2 = 11
pow(int(h1), int(b_double_prime_j))
# Calculer les valeurs de S''j à partir des valeurs aléatoires choisies
S_double_prime_j = {pow(int(g1), int(aj)), pow(int(g2), int(a_prime_j)), pow(int(g1), int(a_double_prime_j)),
                    pow(int(h1), int(bj)), pow(int(h2), int(b_prime_j)), pow(int(h1), int(b_double_prime_j))}
print("s''j :", S_double_prime_j)

###################4-b####################
import random

# Définir l'ensemble de valeurs possibles pour Sk
Sk = [101, 111, 141, 121, 321, 412]

# Choisir des valeurs aléatoires pour ak, bk, a'k, b'k, a''k et b''k
ak = random.choice(Sk)
bk = random.choice(Sk)
a_prime_k = random.choice(Sk)
b_prime_k = random.choice(Sk)
a_double_prime_k = random.choice(Sk)
b_double_prime_k = random.choice(Sk)

# Créer l'ensemble S'k à partir des valeurs aléatoires choisies
S_prime_k = {ak, bk, a_prime_k, b_prime_k, a_double_prime_k, b_double_prime_k}
print("s'k :", S_prime_k)

# Définir les constantes g1, g2, h1 et h2
g1 = 3
g2 = 5
h1 = 7
h2 = 11

# Calculer les valeurs de S''k à partir des valeurs aléatoires choisies

S_double_prime_k = {pow(int(g1), int(ak)), pow(int(g2), int(a_prime_k)), pow(int(g1), int(a_double_prime_k)),
                    pow(int(h1), int(bk)), pow(int(h2), int(b_prime_k)), pow(int(h1), int(b_double_prime_k))}
print("s''k :", S_double_prime_k)

########################4-c################

# Définir l'ensemble Q de participants
Qtemp = ['P1', 'P2', 'P3', 'P4']

# Définir la valeur sfij
sfij = 2

# Définir la constante g1
g1 = 3

# Choisir une valeur aléatoire pour aj
aj = random.choice(Sj)

# Calculer le produit de toutes les valeurs g1 * ak pour chaque participant dans Q
product_g1_ak = 1
for Pk in Qtemp:
    ak = random.choice(Sk)
    product_g1_ak *= g1 * ak

# Calculer λ1 en utilisant la formule donnée
lambda_1 = sfij * g1 * aj * product_g1_ak
print("λ1 : ", lambda_1)

# Définir l'ensemble Q de participants
Qtemp = ['P1', 'P2', 'P3']

# Définir la valeur sgij
sgij = 2

# Définir la constante g2
g2 = 5

# Choisir une valeur aléatoire pour a'j
a_prime_j = random.choice(Sj)

# Calculer le produit de toutes les valeurs g2 * a'k pour chaque participant dans Q
product_g2_aprime_k = 1
for Pk in Qtemp:
    a_prime_k = random.choice(Sk)
    product_g2_aprime_k *= g2 * a_prime_k

# Calculer λ'1 en utilisant la formule donnée
lambda_prime_1 = sgij * g2 * a_prime_j * product_g2_aprime_k
print("λ'1 : ", lambda_prime_1)

# Définir l'ensemble Q de participants
Qtemp = ['P1', 'P2', 'P3']

# Définir la valeur shij
shij = 3

# Définir la constante g1
g1 = 7

# Choisir une valeur aléatoire pour a''j
a_double_prime_j = random.choice(Sj)

# Calculer le produit de toutes les valeurs g1 * a''k pour chaque participant dans Q
product_g1_adoubleprime_k = 1
for Pk in Qtemp:
    a_double_prime_k = random.choice(Sk)
    product_g1_adoubleprime_k *= g1 * a_double_prime_k

# Calculer λ''1 en utilisant la formule donnée
lambda_double_prime_1 = shij * g1 * a_double_prime_j * product_g1_adoubleprime_k
print("λ''1 : ", lambda_double_prime_1)

# Définir la valeur sfij
sfij = 2

# Définir la constante g1
g1 = 3

# Choisir une valeur aléatoire pour aj
aj = random.choice(Sj)

# Calculer λ2 en utilisant la formule donnée
lambda_2 = sfij * (g1 * aj)
print("λ2 : ", lambda_2)

# Définir la valeur sgij
sgij = 2

# Définir la constante g2
g2 = 5

# Choisir une valeur aléatoire pour a'j
a_prime_j = random.choice(Sj)

# Calculer λ'2 en utilisant la formule donnée
lambda_prime_2 = sgij * (g2 * a_prime_j)
print("λ'2 : ", lambda_prime_2)

# Définir la valeur shij
shij = 3

# Définir la constante g1
g1 = 7

# Choisir une valeur aléatoire pour a''j
a_double_prime_j = random.choice(Sj)

# Calculer λ''2 en utilisant la formule donnée
lambda_double_prime_2 = shij * (g1 * a_double_prime_j)
print("λ''2 : ", lambda_double_prime_2)

# Définir l'ensemble Q de participants
Q = ['P1', 'P2', 'P3', 'P4']

# Définir la valeur sf'ij
sf_prime_ij = 2

# Définir la constante h1
h1 = 5

# Choisir une valeur aléatoire pour bj
bj = random.choice(Sj)

# Calculer le produit de toutes les valeurs h1 * bk pour chaque participant dans Q
product_h1_bk = 1
for Pk in Q:
    b_k = random.choice(Sk)
    product_h1_bk *= h1 * b_k

# Calculer γ1 en utilisant la formule donnée
gamma_1 = sf_prime_ij * h1 * bj * product_h1_bk
print(" γ1 : ", gamma_1)

# Définir l'ensemble Q de participants
Q = ['P1', 'P2', 'P3', 'P4']

# Définir la valeur sg'ij
sg_prime_ij = 3

# Définir la constante h2
h2 = 7

# Choisir une valeur aléatoire pour b'j
b_prime_j = random.choice(Sj)

# Calculer le produit de toutes les valeurs h2 * b'k pour chaque participant dans Q
product_h2_b_prime_k = 1
for Pk in Q:
    b_prime_k = random.choice(Sk)
    product_h2_b_prime_k *= h2 * b_prime_k

# Calculer γ'1 en utilisant la formule donnée
gamma_prime_1 = sg_prime_ij * h2 * b_prime_j * product_h2_b_prime_k
print(" γ'1 : ", gamma_prime_1)

# Définir l'ensemble Q de participants
Q = ['P1', 'P2', 'P3', 'P4']

# Définir la valeur sh'ij
sh_prime_ij = 5

# Définir la constante h1
h1 = 3

# Choisir une valeur aléatoire pour b''j
b_double_prime_j = random.choice(Sj)

# Calculer le produit de toutes les valeurs h1 * b''k pour chaque participant dans Q
product_h1_b_double_prime_k = 1
for Pk in Q:
    b_double_prime_k = random.choice(Sk)
    product_h1_b_double_prime_k *= h1 * b_double_prime_k

# Calculer γ''1 en utilisant la formule donnée
gamma_double_prime_1 = sh_prime_ij * h1 * b_double_prime_j * product_h1_b_double_prime_k
print(" γ''1 : ", gamma_double_prime_1)

# Définir la valeur sf'ij
sf_prime_ij = 2

# Définir la constante h1
h1 = 5

# Choisir une valeur aléatoire pour bj
bj = random.choice(Sj)

# Calculer γ2 en utilisant la formule donnée
gamma_2 = sf_prime_ij * (h1 * bj)
print(" γ2 : ", gamma_2)

# Définir la valeur sg'ij
sg_prime_ij = 3

# Définir la constante h2
h2 = 7

# Choisir une valeur aléatoire pour b'j
b_prime_j = random.choice(Sj)

# Calculer γ'2 en utilisant la formule donnée
gamma_prime_2 = sg_prime_ij * (h2 * b_prime_j)
print(" γ'2 : ", gamma_prime_2)

# Définir la valeur sh'ij
sh_prime_ij = 5

# Définir la constante h1
h1 = 3

# Choisir une valeur aléatoire pour b''j
b_double_prime_j = random.choice(Sj)

# Calculer γ''2 en utilisant la formule donnée
gamma_double_prime_2 = sh_prime_ij * (h1 * b_double_prime_j)
print(" γ''2 : ", gamma_double_prime_2)
#################4-d############"


parts = [aj, bj, a_prime_j, b_prime_j, a_double_prime_j, b_double_prime_j]  # Exemple de parts
parts = [ak, bk, a_prime_k, b_prime_k, a_double_prime_k, b_double_prime_k]

print(" les parts sont  envoyees ", parts)

alpha = lambda_1 / lambda_2
print('α = ', alpha)
alpha_prime = lambda_prime_1 / lambda_prime_2
print(" α' = ", alpha_prime)
alpha_double_prime = lambda_double_prime_1 / lambda_double_prime_2
print(" α'' = ", alpha_double_prime)
beta = gamma_1 / gamma_2
print(" β = ", beta)
beta_prime = gamma_prime_1 / gamma_prime_2
print(" β' = ", beta_prime)
beta_double_prime = gamma_double_prime_1 / gamma_double_prime_2
print(" β'' = ", beta_double_prime)
# Définir la séquence de valeurs
seq = [1, 2, 3, 4, 5]

# Calculer r en utilisant la formule donnée
r = sum(seq)
print('r=', r)
# Définir la séquence de valeurs
sequence_prime = [3, 6, 9, 12, 15]

# Calculer r' en utilisant la formule donnée
r_prime = sum(sequence_prime)
print("r'=", r_prime)

# Définir la séquence de valeurs
sequence_double_prime = [1, 3, 5, 7, 9]

# Calculer r'' en utilisant la formule donnée
r_double_prime = sum(sequence_double_prime)
print("r''=", r_double_prime)

# Définir la séquence de valeurs
sequence = [0.5, 1.2, 2.1, 3.3, 5.4]

# Calculer t en utilisant la formule donnée
t = sum(sequence)
print("t=", t)
# Définir la séquence de valeurs
sequence_prime = [1.2, 2.4, 3.6, 4.8, 6.0]

# Calculer t' en utilisant la formule donnée
t_prime = sum(sequence_prime)
print("t'=", t_prime)

# Définir la séquence de valeurs
sequence_double_prime = [0.1, 0.3, 0.5, 0.7, 0.9]

# Calculer t'' en utilisant la formule donnée
t_double_prime = sum(sequence_double_prime)
print("t''=", t_double_prime)

# Given values
g1 = 2.0
g2 = 3.0
h1 = 2.5
h2 = 3.5
lambda_2 = 580
lambda_prime_2 = 1911
lambda_double_prime_2 = 0.9
gamma_2 = 0.6
gamma_prime_2 = 0.8
gamma_double_prime_2 = 0.9

# Calculate α/1r
sfij = 1.0
alpha_1_r = pow(int(g1), int(sfij))
print("α/1r =", alpha_1_r)

# Calculate α'/1r'
sgij = 1.0
alpha_prime_1_r_prime = pow(int(g2), int(sgij))
print("α'/1r' =", alpha_prime_1_r_prime)

# Calculate α''/1r''
shij = 1.0
alpha_double_prime_1_r_double_prime = pow(int(g1), int(shij))
print("α''/1r'' =", alpha_double_prime_1_r_double_prime)

# Calculate β/1t
sf_prime_ij = 1.0
beta_1_t = pow(int(h1), int(sf_prime_ij))
print("β/1t =", beta_1_t)

# Calculate β'/1t'
sg_prime_ij = 1.0
beta_prime_1_t_prime = pow(int(h2), int(sg_prime_ij))
print("β'/1t' =", beta_prime_1_t_prime)

# Calculate β''/1t''
sh_prime_ij = 1.0
beta_double_prime_1_t_double_prime = pow(int(h1), int(sh_prime_ij))
print("β''/1t'' =", beta_double_prime_1_t_double_prime)

# Check equation 3
alpha_1r = 49
beta_1t = 9
alpha_prime_1_r_prime = 25
beta_prime_1t_prime = 343

produit = alpha_1r * beta_1t * alpha_prime_1_r_prime * beta_prime_1t_prime
equation = pow(int(g1), int(sfij)) * pow(int(h1), int(sf_prime_ij)) * pow(int(g2), int(sgij)) * pow(int(h2),
                                                                                                    int(sg_prime_ij))
if produit == equation:
    print("L'équation est vérifiée.")
else:
    print("L'équation n'est pas vérifiée.")

alpha_double_prime_1_r_double_prime = 343
beta_double_prime_1_t_double_prime = 243

produit1 = alpha_double_prime_1_r_double_prime * beta_double_prime_1_t_double_prime
equation1 = pow(int(g1), int(shij)) * pow(int(h1), int(sh_prime_ij))
if produit1 == equation1:
    print("L'équation est vérifiée.")
else:
    print("L'équation n'est pas vérifiée.")

# Calculate sfij for each participant Pj
aj_list = [1.0, 2.0, 3.0, 4.0, 5.0]
sfij = 1.0
for aj in aj_list:
    sfij = lambda_2 / (g1 * sfij) * aj
    print("sfij pour Pj =", aj, ":", sfij)

# Calculate sgij for each participant Pj
a_prime_j_list = [1.5, 2.5, 3.5, 4.5, 5.5]
sgij = 1.0
for a_prime_j in a_prime_j_list:
    sgij = lambda_prime_2 / (g2 * sgij) * a_prime_j
    print("sgij pour Pj =", a_prime_j, ":", sgij)

# Calculate shij for each participant Pj
a_double_prime_j_list = [1.2, 2.2, 3.2, 4.2, 5.2]
shij = 1.0
for a_double_prime_j in a_double_prime_j_list:
    shij = lambda_double_prime_2 / (g1 * shij) * a_double_prime_j
    print("shij pour Pj =", a_double_prime_j, ":", shij)

# Calculate sf'ij for each participant Pj
bj_list = [1.8, 2.8, 3.8, 4.8, 5.8]
sf_prime_ij = 1.0
for bj in bj_list:
    sf_prime_ij = gamma_2 / (h1 * sf_prime_ij) * bj
    print("sf'ij pour Pj =", bj, ":", sf_prime_ij)

# Calculate sg'ij for each participant Pj
b_prime_j_list = [1.3, 2.3, 3.3, 4.3, 5.3]
sg_prime_ij = 1.0
for b_prime_j in b_prime_j_list:
    sg_prime_ij = gamma_prime_2 / (h2 * sg_prime_ij) * b_prime_j
    print("sg'ij pour Pj =", b_prime_j, ":", sg_prime_ij)

# Calculate sh'ij for each participant Pj
b_double_prime_j_list = [1.2, 2.2, 3.2, 4.2, 5.2]
sh_prime_ij = 1.0
for b_double_prime_j in b_double_prime_j_list:
    sh_prime_ij = gamma_double_prime_2 / (h1 * sh_prime_ij) * b_double_prime_j
    print("sh'ij pour Pj =", b_double_prime_j, ":", sh_prime_ij)

# Calculate e1
lambda2 = 0.5
g1sfij = 3.5
aj_list = [1.2, 2.3, 3.4, 4.5, 5.6]
e1 = lambda2 * sum(g1sfij * aj for aj in aj_list)
print("e1 :", e1)

# Calculate e'1
lambda2_prime = 0.8
g2sgij = 1.5
a_prime_j_list = [1.2, 2.3, 3.4, 4.5, 5.6]
e1_prime = lambda2_prime * sum(g2sgij * a_prime_j for a_prime_j in a_prime_j_list)
print("e'1 :", e1_prime)

# Calculate e''1
lambda2_double_prime = 0.3
g1shij = 2.5
a_double_prime_j_list = [1.2, 2.3, 3.4, 4.5, 5.6]
e1_double_prime = lambda2_double_prime * sum(g1shij * a_double_prime_j for a_double_prime_j in a_double_prime_j_list)
print("e''1 :", e1_double_prime)

# Calculate e2
gamma2 = 0.4
h1sf_prime_ij = 1.5
bj_list = [1.2, 2.3, 3.4, 4.5, 5.6]
e2 = gamma2 * sum(h1sf_prime_ij * bj for bj in bj_list)
print("e2 :", e2)

# Calculate e'2
gamma2_prime = 0.6
h2sg_prime_ij = 2.5
b_prime_j_list = [1.2, 2.3, 3.4, 4.5, 5.6]
e2_prime = gamma2_prime * sum(h2sg_prime_ij * b_prime_j for b_prime_j in b_prime_j_list)
print("e'2 :", e2_prime)

# Calculate e''2
gamma2_double_prime = 0.2
h1sh_prime_ij = 3.5
b_double_prime_j_list = [1.2, 2.3, 3.4, 4.5, 5.6]
e2_double_prime = gamma2_double_prime * sum(
    h1sh_prime_ij * b_double_prime_j for b_double_prime_j in b_double_prime_j_list)
print("e''2 :", e2_double_prime)

# Check if Pk concludes that Pj lied
if (e1 == sfij) or (e1_prime == sgij) or (e1_double_prime == shij) == (e2 == sf_prime_ij) or (
        e2_prime == sg_prime_ij) or (e2_double_prime == sh_prime_ij):
    print("Pk conclut que Pj a menti.")
else:
    print("Pk conclut que Pi a menti.")

import numpy as np

num_participants = 5

# Generate random secret keys for each participant
secret_keys = np.random.randint(0, 1000, num_participants)


# Shamir's Secret Sharing Scheme
def generate_shares(secret, num_shares, threshold):
    # Coefficients for the polynomial
    coefficients = np.random.randint(1, 100, threshold - 1)
    coefficients = np.insert(coefficients, 0, secret)

    # Generate shares
    x_values = np.arange(1, num_shares + 1)
    shares = [np.polyval(coefficients, x) for x in x_values]

    return shares


# Example usage
secret_value = 42  # The secret value to be shared
num_shares = 5  # Number of shares to generate
threshold = 3  # Minimum number of shares required to reconstruct the secret

shares = generate_shares(secret_value, num_shares, threshold)
print("Generated shares:", shares)
x = shares


def generate_local_key(secret_key):
    # Some local key generation logic (you can replace this with your specific algorithm)
    return secret_key + np.random.randint(0, 100)


# Generate local keys for each participant
local_keys = [generate_local_key(secret_key) for secret_key in secret_keys]


def reconstruct_secret(shares, threshold):
    x_values = np.arange(1, threshold + 1)
    secret = np.sum(np.prod([(shares[j] / np.prod(x_values[x_values != x[j]] - x[j])) for j in range(threshold)]))
    return int(secret)


# Example usage to reconstruct the secret
required_shares = shares[:threshold]  # Minimum number of shares needed for reconstruction
reconstructed_secret = reconstruct_secret(required_shares, threshold)
print("Reconstructed secret:", reconstructed_secret)


# Define a global key generation function (e.g., XOR operation)
def generate_global_key(keys):
    return np.bitwise_xor.reduce(keys)


def handle_complaints(complaints):
    # Some complaint management logic (you can replace this with your specific algorithm)
    # For example, you could take majority votes or apply weighted responses based on trust levels.
    return np.bitwise_xor.reduce(complaints)


# Example of participants making complaints
complaints = [generate_local_key(secret_key) for secret_key in secret_keys]

# Apply the complaint management strategy to resolve the complaints
resolved_key = handle_complaints(complaints)


# Define a function to handle complaints from participants
def handle_complaints(complaints):
    # Some complaint management logic (you can replace this with your specific algorithm)
    # For example, you could take majority votes or apply weighted responses based on trust levels.
    return np.bitwise_xor.reduce(complaints)


# Example of participants making complaints
complaints = [generate_local_key(secret_key) for secret_key in secret_keys]

# Apply the complaint management strategy to resolve the complaints
resolved_key = handle_complaints(complaints)
# Combine local keys to obtain the global key
global_key = generate_global_key(local_keys)

# Verify the global key using the resolved_key (complaint management) and the secret keys
if np.bitwise_xor.reduce([global_key] + complaints) == resolved_key:
    print("Global key generation successful.")
else:
    print("Global key generation failed.")

import numpy as np


# Step 2: Key Generation Protocol (Shamir's Secret Sharing)
def generate_shares(secret, num_participants, threshold):
    # Generate a random polynomial of degree threshold-1 with 'secret' as the constant term
    coefficients = [secret] + [np.random.randint(1, 100) for _ in range(threshold - 1)]

    # Generate shares for each participant
    shares = {}
    for participant in range(1, num_participants + 1):
        shares[participant] = sum(coeff * participant ** idx for idx, coeff in enumerate(coefficients))

    return shares


# Step 3: Complaint Management Strategy
def handle_complaint(shares, participant_id, threshold):
    if len(shares) < threshold:
        # Not enough shares to reconstruct the secret
        print(f"Participant {participant_id} doesn't have enough shares.")
        return

    # In a real implementation, more sophisticated strategies should be used.
    # For simplicity, we'll just remove the participant's share here.
    del shares[participant_id]
    print(f"Participant {participant_id}'s share has been removed.")


# Example usage
num_participants = 5
threshold = 3
secret_key = 42

# Generate shares
shares = generate_shares(secret_key, num_participants, threshold)

# Simulate a complaint from a participant
complaining_participant = 3
handle_complaint(shares, complaining_participant, threshold)

# Now, you can proceed with the complaint-free shares to reconstruct the secret if needed.

import numpy as np


# Distributed Multi-Key Generation Protocol
def generate_key_part(node_id):
    # Simulated key generation process (Replace with your actual algorithm)
    key_part = np.random.randint(0, 256, size=32, dtype=np.uint8)
    print(f"Node {node_id} generated key part: {key_part}")
    return key_part


def combine_key_parts(key_parts):
    # Simple XOR combination of key parts (Replace with your actual algorithm)
    combined_key = key_parts[0] ^ key_parts[1]
    print(f"Combined Key: {combined_key}")
    return combined_key


# Complaint Management Strategy Algorithm
class ComplaintManager:
    def __init__(self):
        self.complaints = []

    def log_complaint(self, node_id, severity, description):
        self.complaints.append((node_id, severity, description))
        print(f"Complaint logged - Node {node_id}, Severity: {severity}, Description: {description}")

    def store_parts(self, parts, file_name):
        with open(file_name, "w") as f:
            for part in parts:
                f.write(part + "\n")
                print(f"L'ensemble des parts a été stocké dans le fichier {file_name} !")

    def send_parts(self, parts, url):

        import requests
        data = {"parts": parts}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("L'ensemble des parts a été envoyé avec succès !")
        else:
            print("Erreur lors de l'envoi de l'ensemble des parts...")

    def resolve_complaints(self):
        # Simulated complaint resolution (Replace with your actual algorithm)
        for complaint in self.complaints:
            node_id, severity, description = complaint
            if severity == "low":
                print(f"Complaint from Node {node_id} resolved with low priority.")
            elif severity == "medium":
                print(f"Complaint from Node {node_id} resolved with medium priority.")
            else:
                print(f"Complaint from Node {node_id} resolved with high priority.")
        self.complaints = []  # Clear resolved complaints

    def generate_key(self, parts):

        key = ""
        for i in range(len(parts[0])):
            char_set = set(part[i] for part in parts)
            key += random.choice(list(char_set))
        return key

    def publish_key(self, parts, key):

        with open("key.txt", "w") as f:
            f.write(key)
        print(f"La clé ({key}) a été publiée avec succès !")

    def find_max_votes(self, votes):

        max_votes = max(votes.values())
        max_participants = [participant for participant, num_votes in votes.items() if num_votes == max_votes]
        if len(max_participants) == 1:
            return max_participants[0]
        else:
            return max_participants

    def disqualify_participants(self, compplaints, threshold):

        disqualified = [participant for participant, num_complaint in complaints.items() if num_complaint > threshold]
        return disqualified


# Example usage
if __name__ == "__main__":
    # Distributed Multi-Key Generation Protocol
    node1_key_part = generate_key_part(1)
    node2_key_part = generate_key_part(2)
    combined_key = combine_key_parts([node1_key_part, node2_key_part])
    parts = ["abcde", "fghij", "klmno", "pqrst"]  # Exemple de parts
    # Stocker l'ensemble des parts dans un fichier texte
    parts2 = ["abcde", "fghij", "klmno", "pqrst"]  # Exemple de parts
    url = "https://example.com/api/parts"  # Exemple d'URL de serveur distant

    parts3 = ["abcde", "fghij", "klmno", "pqrst"]  # Exemple de parts

    parts4 = ["abcde", "fghij", "klmno", "pqrst"]  # Exemple de parts

    votes = {"Participant 1": 10, "Participant 2": 15, "Participant 3": 7, "Participant 4": 15,
             "Participant 5": 8}  # Exemple de votes pour chaque participant

    # Complaint Management Strategy Algorithm
    complaint_manager = ComplaintManager()
    complaint_manager.log_complaint(1, "low", "Node 1 is running slow")
    complaint_manager.log_complaint(2, "high", "Node 2 crashed")
    random_key = complaint_manager.generate_key(parts)  # Générer une clé aléatoire à partir des parts
    print("Clé choisie au hasard   :", random_key)

    complaint_manager.publish_key(parts, random_key)

    max_votes = complaint_manager.find_max_votes(votes)  # Trouver les participants avec le maximum de votes
    print("Participant(s) avec le maximum de votes :", max_votes)
    malicious_participants = complaint_manager.disqualify_participants(votes,
                                                                       12)  # Disqualifier les participants qui ont plus de 12 votes
    if len(malicious_participants) > 0:
        print("Les participants malhonnêtes sont :", malicious_participants)
    else:
        print("Aucun participant malhonnête n'a été identifié.")

    complaint_manager.store_parts(parts, "parts.txt")
    complaint_manager.send_parts(parts2, url)
    complaint_manager.resolve_complaints()