import os
import pandas as pd
import matplotlib
import sqlite3  # Biblioteca para usar SQLite com Python
matplotlib.use('Agg')  # Usa o backend 'Agg' para evitar problemas com Tkinter
import matplotlib.pyplot as plt

# Diretório onde os arquivos foram salvos
input_dir = 'Daily Prices'

# Função para consolidar os arquivos em um único DataFrame
def consolidate_files():
    all_data = []  # Lista para armazenar os DataFrames de cada arquivo

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".csv"):  # Verifica arquivos com extensão .csv
            file_path = os.path.join(input_dir, file_name)
            # Extrai a data do nome do arquivo (formato "aaaammdd")
            file_date = pd.to_datetime(file_name.split(".")[0], format="%Y%m%d")
            
            # Carrega o arquivo Excel em um DataFrame, pulando as linhas até a linha 10, sem cabeçalho
            try:
                df = pd.read_excel(file_path, skiprows=9, header=None)  # Lê os dados sem considerar cabeçalho

                # Define os nomes das colunas manualmente
                df.columns = ['Código', 'Nome', 'Repac./ Venc.', 'Índice/ Correção', 'Taxa de Compra', 
                              'Taxa de Venda', 'Taxa Indicativa', 'Desvio Padrão', 'Intervalo Min.', 
                              'Intervalo Máx.', 'PU', '% PU Par', 'Duration', '% Reune', 'Outras Informações']
                
                # Adiciona uma coluna 'Data' ao DataFrame com a data extraída
                df['Data'] = file_date

                # Seleciona apenas as colunas relevantes
                df = df[['Código', 'Nome', 'Repac./ Venc.', 'Índice/ Correção', 'Taxa de Compra', 
                         'Taxa de Venda', 'Taxa Indicativa', 'Desvio Padrão', 'Intervalo Min.', 
                         'Intervalo Máx.', 'PU', '% PU Par', 'Duration', '% Reune', 'Data']]
                
                # Adiciona o DataFrame à lista
                all_data.append(df)
            except Exception as e:
                print(f"Erro ao processar o arquivo {file_name}: {e}")

    # Verifica se há arquivos para concatenar
    if all_data:
        consolidated_data = pd.concat(all_data, ignore_index=True)
        return consolidated_data
    else:
        print("Nenhum arquivo CSV encontrado para consolidar.")
        return None

# Consolida os arquivos baixados e exibe o DataFrame resultante
consolidated_df = consolidate_files()
if consolidated_df is not None:
    print("\nPrimeiras linhas do DataFrame consolidado:")
    print(consolidated_df.head())  # Exibe as primeiras linhas para verificação
else:
    print("Consolidação falhou. Verifique se os arquivos estão na pasta correta.")

# Verifique todos os valores únicos na coluna 'Índice/ Correção'
print("\nValores únicos na coluna 'Índice/ Correção':")
print(consolidated_df['Índice/ Correção'].unique())

# Adiciona a coluna 'Indexador' ao DataFrame consolidado
# Função para identificar o tipo de indexador com base no valor da coluna 'Índice/ Correção'
def get_indexador(value):
    if isinstance(value, str):  # Verifica se o valor é uma string
        if 'DI' in value:
            return 'DI +'
        elif 'IPCA' in value:
            return 'IPCA +'
        else:
            return '% do DI'
    else:
        return None  # Retorna None se o valor não for uma string

# Aplica a função para criar a coluna 'Indexador'
consolidated_df['Indexador'] = consolidated_df['Índice/ Correção'].apply(get_indexador)

# Exibe as primeiras linhas para verificação da nova coluna
print("\nPrimeiras linhas com a coluna 'Indexador' adicionada:")
print(consolidated_df[['Código', 'Índice/ Correção', 'Indexador']].head())

# Verifique os indexadores únicos
print("\nIndexadores únicos encontrados:", consolidated_df['Indexador'].unique())

# Exporta o DataFrame consolidado para um arquivo CSV
consolidated_df.to_csv("consolidated_debentures.csv", index=False, encoding="utf-8")

# Passo 5: Simulação de Banco de Dados com SQLite

print("\nIniciando simulação do banco de dados SQLite...")

# Conectar ao banco de dados SQLite (ou criar um novo arquivo de banco de dados)
conn = sqlite3.connect('debentures.db')

# Carregar o DataFrame consolidado para o SQLite
consolidated_df.to_sql('debentures', conn, if_exists='replace', index=False)

# Consulta 1: Quantidade de debêntures listadas no dia anterior
print("\n--- Consulta 1: Quantidade de debêntures listadas no dia anterior ---")
query1 = """
SELECT COUNT(DISTINCT Código) AS quantidade_de_debentures
FROM debentures
WHERE Data = (SELECT MAX(Data) FROM debentures WHERE Data < (SELECT MAX(Data) FROM debentures));
"""
result1 = pd.read_sql_query(query1, conn)
print(result1.to_string(index=False))

# Consulta 2: Duration média de todas as debêntures em cada um dos últimos 5 dias úteis
print("\n--- Consulta 2: Duration média de todas as debêntures nos últimos 5 dias úteis ---")
query2 = """
SELECT Data, AVG(Duration) AS duration_media
FROM debentures
GROUP BY Data
ORDER BY Data DESC
LIMIT 5;
"""
result2 = pd.read_sql_query(query2, conn)
print(result2.to_string(index=False))

# Consulta 3: Códigos únicos de todas as debêntures da empresa “VALE S/A”
print("\n--- Consulta 3: Códigos únicos de todas as debêntures da empresa 'VALE S/A' ---")
query3 = """
SELECT DISTINCT Código
FROM debentures
WHERE Nome LIKE '%VALE S/A%';
"""
result3 = pd.read_sql_query(query3, conn)
print(result3 if not result3.empty else "Nenhuma debênture encontrada para 'VALE S/A'.")

# Fechar a conexão com o banco de dados
conn.close()
print("\nSimulação de banco de dados concluída.")
