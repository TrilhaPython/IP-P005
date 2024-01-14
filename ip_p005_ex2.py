import numpy as np

print(np.__version__ )

identificador = ['tic1802676','tic1811188','tic1822289','tic1833390']
idade = [47, 35, 33, 33]
formação = [3,0,3,2]
formaçãoGeral = [1,0,0,1]
formaçãoEspecífica = [1,None,0,1]
andamentoGraduação = [.8,None,None,.75]
tempoFormação = [None,10,None,None]
experiênciaPrevia = [True,False,True,False]

import pandas as pd
#print(pd.__version__ )

psidade = pd.Series(idade, index=identificador)
psformação = pd.Series(formação, index=identificador)
psformaçãoGeral = pd.Series(formaçãoGeral, index=identificador)
psformaçãoEspecífica = pd.Series(formaçãoEspecífica, index=identificador)
psandamentoGraduação = pd.Series(andamentoGraduação, index=identificador)
pstempoFormação = pd.Series(tempoFormação, index=identificador)
psexperiênciaPrevia = pd.Series(experiênciaPrevia, index=identificador)

min_age = psidade.min()
print("Idade mínima: ", min_age)
min_age_indices = psidade[psidade == min_age].index
for key in min_age_indices:
    print("\t-> ",key)

max_age = psidade.max()
print("Idade máxima: ", max_age)
max_age_indices = psidade[psidade == max_age].index
for key in max_age_indices:
    print("\t-> ",key)

print("Idade média: ", psidade.mean())

lformação=['Formação téccnica',
            'Graduação em andamento',
            'Graduação em andamento',
            'Graduação concluída']
mode_formação = psformação.mode()
#print(">>",mode_formação.values)
#mode_formação_indices = psformação[psformação == mode_formação.values].index
for key in mode_formação:
    print("-> ",lformação[key])

lformaçãoEspecífica=['Engenharia','Computação']
#my_list = [x for x in my_list if x is not None]

mode_fs=psformaçãoEspecífica.dropna().mode()
print(">>",mode_fs)
for key in mode_fs:
    print("\t-> ",lformaçãoEspecífica[int(key)])
