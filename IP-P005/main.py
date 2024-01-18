import numpy as np
import pandas as pd

# Exercício 1: Criando um conjunto de dados

identificador = ['tic18Py06472', 'tic18Py12345', 'tic18Py67890']
idade = [25, 28, 22]
formação = [2, 0, 3]  # 0: Formação técnica, 1: Formação técnica graduação em andamento, 2: Graduação em andamento, 3: Graduação concluída
formaçãoGeral = [1, 0, None]  # 0: Engenharia, 1: Computação
formaçãoEspecífica = ['Ciência da Computação', 'Engenharia Elétrica', None]
andamentoGraduação = [75.0, None, None]  # Em percentual
tempoFormação = [None, None, 2]  # Em anos
experiênciaPrevia = [True, False, True]

# Exibindo os dados
print("Identificador:", identificador)
print("Idade:", idade)
print("Formação:", formação)
print("Formação Geral:", formaçãoGeral)
print("Formação Específica:", formaçãoEspecífica)
print("Andamento Graduação:", andamentoGraduação)
print("Tempo de Formado:", tempoFormação)
print("Experiência Prévia em Programação:", experiênciaPrevia)

# Exercício 2: Trabalhando com Series

# Definindo listas
identificador = ['tic18Py06472', 'tic18Py12345', 'tic18Py67890']
idade = [25, 28, 22]
formacao = [2, 0, 3]  # 0: Formação técnica, 1: Formação técnica graduação em andamento, 2: Graduação em andamento, 3: Graduação concluída
formacaoGeral = [1, 0, None]  # 0: Engenharia, 1: Computação
formacaoEspecifica = ['Ciência da Computação', 'Engenharia Elétrica', None]
andamentoGraduacao = [75.0, None, None]  # Em percentual
tempoFormacao = [None, None, 2]  # Em anos
experienciaPrevia = [True, False, True]

# Criando o objeto Index
index = pd.Index(identificador)

# Convertendo listas em objetos Series
idade_series = pd.Series(idade, index=index, name='Idade')
formacao_series = pd.Series(formacao, index=index, name='Formação')
formacaoGeral_series = pd.Series(formacaoGeral, index=index, name='Formação Geral')
formacaoEspecifica_series = pd.Series(formacaoEspecifica, index=index, name='Formação Específica')
andamentoGraduacao_series = pd.Series(andamentoGraduacao, index=index, name='Andamento Graduação')
tempoFormacao_series = pd.Series(tempoFormacao, index=index, name='Tempo de Formado')
experienciaPrevia_series = pd.Series(experienciaPrevia, index=index, name='Experiência Prévia em Programação')

# Extraindo informações
media_idade = idade_series.mean()
membros_mais_jovens = idade_series[idade_series == idade_series.min()].index.tolist()
membros_mais_velhos = idade_series[idade_series == idade_series.max()].index.tolist()

# Identificando perfil de formação
perfil_formacao = ""
if formacao_series.isin([0, 1]).any():
    perfil_formacao = "Predominantemente Técnicos"
elif formacao_series.isin([2]).any():
    perfil_formacao = "Predominantemente Graduandos"
elif formacao_series.isin([3]).all():
    perfil_formacao = "Todos Graduados"

# Identificando área de formação predominante
area_formacao_predominante = ""
if formacaoGeral_series.isin([0]).any():
    area_formacao_predominante = "Engenheiros"
elif formacaoGeral_series.isin([1]).any():
    area_formacao_predominante = "Área de Computação"

# Criando o DataFrame
df = pd.DataFrame({
    'Idade': idade_series,
    'Formação': formacao_series,
    'Formação Geral': formacaoGeral_series,
    'Formação Específica': formacaoEspecifica_series,
    'Andamento Graduação': andamentoGraduacao_series,
    'Tempo de Formado': tempoFormacao_series,
    'Experiência Prévia em Programação': experienciaPrevia_series
})

# Extraindo informações do DataFrame
media_idade_df = df['Idade'].mean()
membros_mais_jovens_df = df[df['Idade'] == df['Idade'].min()]['Idade']
membros_mais_velhos_df = df[df['Idade'] == df['Idade'].max()]['Idade']

# Exibindo resultados
print("Análise usando Series:")
print("Idade Média:", media_idade)
print("Membros mais jovens:", membros_mais_jovens)
print("Membros mais velhos:", membros_mais_velhos)
print("Perfil de Formação:", perfil_formacao)
print("Área de Formação Predominante:", area_formacao_predominante)

print("\nAnálise usando DataFrame:")
print("Idade Média:", media_idade_df)
print("Membros mais jovens:")
print(membros_mais_jovens_df)
print("Membros mais velhos:")
print(membros_mais_velhos_df)

# Exercício 3: Trabalhando com DataFrames

# Definindo listas
identificador = ['tic18Py06472', 'tic18Py12345', 'tic18Py67890']
idade = [25, 28, 22]
formacao = [2, 0, 3]  # 0: Formação técnica, 1: Formação técnica graduação em andamento, 2: Graduação em andamento, 3: Graduação concluída
formacaoGeral = [1, 0, None]  # 0: Engenharia, 1: Computação
formacaoEspecifica = ['Ciência da Computação', 'Engenharia Elétrica', None]
andamentoGraduacao = [75.0, None, None]  # Em percentual
tempoFormacao = [None, None, 2]  # Em anos
experienciaPrevia = [True, False, True]

# Criando o DataFrame
df = pd.DataFrame({
    'Identificador': identificador,
    'Idade': idade,
    'Formação': formacao,
    'Formação Geral': formacaoGeral,
    'Formação Específica': formacaoEspecifica,
    'Andamento Graduação': andamentoGraduacao,
    'Tempo de Formado': tempoFormacao,
    'Experiência Prévia em Programação': experienciaPrevia
})

# Exibindo o DataFrame
print(df)

# Extraindo informações do DataFrame
media_idade_df = df['Idade'].mean()
membros_mais_jovens_df = df[df['Idade'] == df['Idade'].min()]['Identificador']
membros_mais_velhos_df = df[df['Idade'] == df['Idade'].max()]['Identificador']

# Identificando perfil de formação
perfil_formacao_df = ""
if df['Formação'].isin([0, 1]).any():
    perfil_formacao_df = "Predominantemente Técnicos"
elif df['Formação'].isin([2]).any():
    perfil_formacao_df = "Predominantemente Graduandos"
elif df['Formação'].isin([3]).all():
    perfil_formacao_df = "Todos Graduados"

# Identificando área de formação predominante
area_formacao_predominante_df = ""
if df['Formação Geral'].isin([0]).any():
    area_formacao_predominante_df = "Engenheiros"
elif df['Formação Geral'].isin([1]).any():
    area_formacao_predominante_df = "Área de Computação"

# Tratamento da coluna 'Formação Específica'
# Aqui, uma estratégia simples seria preencher os valores NaN com uma categoria genérica, como 'Outro'
df['Formação Específica'].fillna('Outro', inplace=True)

# Exibindo resultados
print("\nAnálise usando DataFrame:")
print("Idade Média:", media_idade_df)
print("Membros mais jovens:")
print(membros_mais_jovens_df.to_list())
print("Membros mais velhos:")
print(membros_mais_velhos_df.to_list())
print("Perfil de Formação:", perfil_formacao_df)
print("Área de Formação Predominante:", area_formacao_predominante_df)
print("\nDataFrame com tratamento da coluna 'Formação Específica':")
print(df)

# Exercício 4: Trabalhando com MultiIndex

# Definindo listas para a trilha Python
identificador_python = ['tic18Py06472', 'tic18Py12345', 'tic18Py67890']
idade_python = [25, 28, 22]
formacao_python = [2, 0, 3]
formacaoGeral_python = [1, 0, None]
formacaoEspecifica_python = ['Ciência da Computação', 'Engenharia Elétrica', None]
andamentoGraduacao_python = [75.0, None, None]
tempoFormacao_python = [None, None, 2]
experienciaPrevia_python = [True, False, True]

# Definindo listas para a trilha .Net
identificador_dotnet = ['tic18Dot123', 'tic18Dot456', 'tic18Dot789']
idade_dotnet = [22, 23, 21]
formacao_dotnet = [1, 2, 0]
formacaoGeral_dotnet = [0, 1, None]
formacaoEspecifica_dotnet = ['Engenharia de Software', 'Sistemas de Informação', None]
andamentoGraduacao_dotnet = [90.0, 50.0, None]
tempoFormacao_dotnet = [None, None, 1]
experienciaPrevia_dotnet = [False, True, True]

# Definindo listas para a trilha Java
identificador_java = ['tic18Java111', 'tic18Java222', 'tic18Java333']
idade_java = [24, 26, 23]
formacao_java = [3, 0, 2]
formacaoGeral_java = [0, 1, None]
formacaoEspecifica_java = ['Engenharia Civil', 'Ciência da Computação', None]
andamentoGraduacao_java = [None, None, 60.0]
tempoFormacao_java = [3, None, None]
experienciaPrevia_java = [True, False, False]

# Criando o MultiIndex
index_levels = ['Trilha', 'Identificador']
index_values = [('Python', i) for i in identificador_python] + [('DotNet', i) for i in identificador_dotnet] + [('Java', i) for i in identificador_java]
multi_index = pd.MultiIndex.from_tuples(index_values, names=index_levels)

# Criando o DataFrame com MultiIndex
df_multi = pd.DataFrame({
    'Idade': idade_python + idade_dotnet + idade_java,
    'Formação': formacao_python + formacao_dotnet + formacao_java,
    'Formação Geral': formacaoGeral_python + formacaoGeral_dotnet + formacaoGeral_java,
    'Formação Específica': formacaoEspecifica_python + formacaoEspecifica_dotnet + formacaoEspecifica_java,
    'Andamento Graduação': andamentoGraduacao_python + andamentoGraduacao_dotnet + andamentoGraduacao_java,
    'Tempo de Formado': tempoFormacao_python + tempoFormacao_dotnet + tempoFormacao_java,
    'Experiência Prévia em Programação': experienciaPrevia_python + experienciaPrevia_dotnet + experienciaPrevia_java
}, index=multi_index)

# Exibindo o DataFrame com MultiIndex
print("DataFrame com MultiIndex:")
print(df_multi)

# Extraindo informações do DataFrame com MultiIndex
media_idade_multi = df_multi.groupby('Trilha')['Idade'].mean()
membros_mais_jovens_multi = df_multi.loc[df_multi.groupby('Trilha')['Idade'].idxmin()].index.get_level_values('Identificador')
membros_mais_velhos_multi = df_multi.loc[df_multi.groupby('Trilha')['Idade'].idxmax()].index.get_level_values('Identificador')

# Identificando perfil de formação por trilha
perfil_formacao_multi = df_multi.groupby('Trilha')['Formação'].apply(lambda x: "Predominantemente Técnicos" if (x.isin([0, 1])).any() else ("Predominantemente Graduandos" if (x.isin([2])).any() else ("Todos Graduados" if (x.isin([3])).all() else "")))

# Identificando área de formação predominante por trilha
area_formacao_predominante_multi = df_multi.groupby('Trilha')['Formação Geral'].apply(lambda x: "Engenheiros" if (x.isin([0])).any() else ("Área de Computação" if (x.isin([1])).any() else ""))

# Exibindo resultados
print("\nAnálise por Trilha usando DataFrame com MultiIndex:")
print("Idade Média por Trilha:", media_idade_multi)
print("Membros mais jovens por Trilha:")
print(membros_mais_jovens_multi.to_list())
print("Membros mais velhos por Trilha:")
print(membros_mais_velhos_multi.to_list())
print("Perfil de Formação por Trilha:")
print(perfil_formacao_multi)
print("Área de Formação Predominante por Trilha:")
print(area_formacao_predominante_multi)