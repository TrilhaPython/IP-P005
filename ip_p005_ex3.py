import numpy as np

print(np.__version__ )

identificador = ['tic18Py02676','tic18Py11188','tic18Py22289','tic18Py33390','tic18Py44477','tic18Py55579']
idade = [47, 35, 33, 33, 46, 44]
formação = [3,0,1,2,2,1]
formaçãoGeral = [1,None,0,1,1,0] #pos1==None por causa de formação_pos1==0
#formaçãoEspecífica = [1,None,0,1] 
formaçãoEspecífica = ['CiC',None,'Eng.Mec','TIC','CiC','Eng.Civ']
andamentoGraduação = [None,None,.75,.8,.7,.6]
tempoFormação = [10,None,None,None,None,None]
experiênciaPrevia = [True,False,True,False,False,True]

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

lformação=['Formação técnica',
            'Tec.Graduação em andamento',
            'Graduação em andamento',
            'Graduação concluída']
mode_formação = psformação.mode()
#print(">>",mode_formação.values)
#mode_formação_indices = psformação[psformação == mode_formação.values].index
print("Formação:")
for key in mode_formação:
    print("-> ",lformação[key])

lformaçãoGeral=['Engenharia','Computação']
#my_list = [x for x in my_list if x is not None]

mode_fs=psformaçãoGeral.dropna().mode()
#print(">>",mode_fs)
print("Formação Geral: ")
for key in mode_fs:
    print("\t-> ",lformaçãoGeral[int(key)])
print('-'*50)
#print(psidade)
#print(psidade.index)
#print(psidade.co)
dftitcol=pd.DataFrame({'Idade':psidade, 
                       'Formação':psformação,'Form.Geral':psformaçãoGeral,
                            'Form.Espec.':psformaçãoEspecífica,'Andam.Grad.':psandamentoGraduação, 
                            'Temp.Form.':pstempoFormação,'Exp.Previa':psexperiênciaPrevia})

print(dftitcol)
strpsformação=[]
for key in psformação.values: 
       strpsformação.append(lformação[key])
#print(strpsformação)
psformaçãoGeral.fillna(-1,inplace=True)
strpsformaçãoGeral=[]
for key in psformaçãoGeral: 
        #print('>>>', key)
        if key == -1:
            strpsformaçãoGeral.append('None')
        else:
            strpsformaçãoGeral.append(lformaçãoGeral[int(key)])
#print(strpsformação)

dftitcol=pd.DataFrame({'Idade':psidade, 
                       'Formação':strpsformação,'Form.Geral':strpsformaçãoGeral,
                            'Form.Espec.':psformaçãoEspecífica,'Andam.Grad.':psandamentoGraduação, 
                            'Temp.Form.':pstempoFormação,'Exp.Previa':psexperiênciaPrevia})

print(dftitcol)
