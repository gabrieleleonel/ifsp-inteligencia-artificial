import pandas as pd

data = pd.read_csv('GasPricesinBrazil_2004-2019-checkpoint.csv', sep=';')
data.rename(columns={'Unnamed':'DEU RUIM','DATA INICIAL': 'Data Inicial','DATA FINAL': 'Data Final','REGIÃO':'Região','ESTADO':'Estado','PRODUTO':'Produto','NúMERO DE POSTOS PESQUISADOS':'Número de Postos Pesquisados','UNIDADE DE MEDIDA':'Unidade de Medida','PREÇO MÉDIO REVENDA':'Preço Médio de Revenda','DESVIO PADRÃO REVENDA':'Desvio Padrão de Revenda','PREÇO MÍNIMO REVENDA':'Preço Mínimo de Revenda','PREÇO MÁXIMO REVENDA':'Preço Máximo de Revenda','MARGEM MÉDIA REVENDA':'Margem Média de Revenda','COEF DE VARIAÇÃO REVENDA':'Coef de Variacao de Revenda','PREÇO MÉDIO DISTRIBUIÇÃO':'Preço Médio de Distribuição','DESVIO PADRÃO DISTRIBUIÇÃO':'Desvio Padrão de Distribuição','PREÇO MÍNIMO DISTRIBUIÇÃO':'Preço Mínimo de Distribuição','PREÇO MÁXIMO DISTRIBUIÇÃO':'Preço Máximo de Distribuição','COEF DE VARIAÇÃO DISTRIBUIÇÃO':'Coef de Variacao de Distribuição','MÊS':'Mês','ANO':'Ano'
},inplace=True)

print(list(data))