import pandas as pd
import numpy as np

df_vendas = pd.read_csv("/content/vendas.csv")

#Visualização das primeiras linhas
df_vendas.head()

#Visualização das últimas linhas
df_vendas.tail()

#Quantidade de linhas do csv
len(df_vendas)

#Verificando informações gerais do DF
df_vendas.info()
df_vendas.describe()

#Criar uma coluna chamada Receita Total (Quantidade * Preco_Unitario)
df_vendas["Receita_Total"] = df_vendas["Quantidade"] * df_vendas["Preco_Unitario"]
df_vendas.head()

#Selecionar apenas as colunas Produto e Receita_Total
df_vendas[["Produto", "Receita_Total"]].head()

#Linhas onde a quantidade é maior que 20 (fatiamento)
df_vendas[df_vendas["Quantidade"] > 20].head()

#LOC (Selecionar linhas e colunas por rótulo (Produto = 'Monitor'))
df_vendas.loc[df_vendas["Produto"] == "Monitor", ["ID_Venda", "Quantidade", "Preco_Unitario"]].head()

#Selecionar as primeiras 3 linhas e as colunas de 1 a 3
df_vendas.iloc[0:3, 1:4]

#Cálculos (Pandas e Numpy)
#Descobrir o faturamento (Receita Total)
print(f"Receita Total de Vendas da Loja: {df_vendas["Receita_Total"].sum():.2f}")

#Preço médio unitário dos produtos
print(f"O preço média unitário dos produtos é: {df_vendas["Preco_Unitario"].mean():.2f}")

#Quantidade mínima e máxima de produtos vendidos
print(f"Quantidade mínima de produtos vendidos: {df_vendas["Quantidade"].min()}")
print(f"Quantidade máxima de produtos vendidos: {df_vendas["Quantidade"].max()}")

#Simular valores ausentes dentro do DF
df_vendas_com_nan = df_vendas.copy()
df_vendas_com_nan.loc[df_vendas_com_nan.sample(frac=0.05).index,'Preco_Unitario'] = np.nan
df_vendas_com_nan.loc[df_vendas_com_nan.sample(frac=0.03).index, 'Quantidade'] = np.nan

#Verificar se existe valores ausentes
df_vendas_com_nan.isna().sum()

#Preencher os valores ausentes em quantidade com a média dos valores (fillna)
df_vendas_preenchido = df_vendas_com_nan.copy()
media_qtd = df_vendas_preenchido['Quantidade'].mean()
df_vendas_preenchido['Quantidade'].fillna(media_qtd, inplace=True)

#Remover as linhas com valores ausentes (dropna)
df_vendas_limpo = df_vendas_preenchido.dropna(subset=['Preco_Unitario'])

#Quantidade e receita total por produto
vendas_por_produto = df_vendas_limpo.groupby("Produto").agg(
    Quantidade_Total = ("Quantidade", sum),
    Receita_Total = ("Receita_Total", sum)
).reset_index()

#Ordenar os valores por quantidade total para saber o produto mais vendido
produto_mais_vendido = vendas_por_produto.sort_values(by="Quantidade_Total", ascending=False).iloc[0]

#Ordenar os valores por receita total para saber o maior valor total gerado
produto_maior_receita = vendas_por_produto.sort_values(by="Receita_Total", ascending=False).iloc[0]

df_produtos = pd.read_csv('/content/produtos.csv')
df_produtos.head()
df_vendas_limpo.info()

#Converter a coluna Data_Venda para o tipo correto de data
df_vendas_limpo['Data_Venda'] = pd.to_datetime(df_vendas_limpo['Data_Venda'])

#Analisar as vendas por mês
df_vendas_limpo["Mes_Venda"] = df_vendas_limpo["Data_Venda"].dt.month

#Agrupar por mês para calcular a receita total mês a mês
vendas_por_mes = df_vendas_limpo.groupby("Mes_Venda")["Receita_Total"].sum().reset_index()

#Combinar os dados de vendas e produtos
df_merge = pd.merge(df_vendas_limpo, df_produtos, on="Produto", how="left")

#Análise de vendas por categoria (Receita Total por categoria)
vendas_por_categoria = df_merge.groupby("Categoria")["Receita_Total"].sum().reset_index()
print(vendas_por_categoria)

#Filtragem dentro do DataFrame
df_merge.head()

#Filtrar por coluna (Produto, Quantidade, Receita Total)
df_colunas_filtradas = df_merge.filter(items=["Produto", "Quantidade", "Receita_Total"])

#Filtragem mais avançadas (Produto Teclado, quantidade > 10)
df_query = df_merge.query("Produto == 'Teclado' and Quantidade > 10")







