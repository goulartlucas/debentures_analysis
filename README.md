# Debentures Analysis
Este projeto foi desenvolvido para facilitar a análise e visualização de dados de debêntures do mercado secundário brasileiro. Ele inclui scripts em Python para processamento dos dados, um banco de dados SQLite para consultas SQL e um relatório visual criado no Power BI.

## Estrutura do Projeto

- **debentures_analysis/**
  - **data/**
    - `consolidated_debentures.csv` — Dataset consolidado de debêntures
  - **images/**
    - `taxa_indicativa_media_DI+.png` — Gráfico da taxa indicativa média
  - **power_bi/**
    - `debentures_analysis_report.pbix` — Relatório do Power BI
  - **scripts/**
    - `main_script.py` — Script principal para processamento de dados
  - `README.md` — Documentação do projeto
  - `requirements.txt` — Dependências do Python
  - `debentures.db` — Banco de dados SQLite com dados das debêntures


## Instruções de Configuração
1. Criação do Ambiente Virtual: Crie e ative um ambiente virtual com os seguintes comandos:
   python -m venv venv
   source venv/bin/activate    # Para Mac/Linux
   venv\Scripts\activate       # Para Windows
2. Instalação das Dependências: Instale as dependências listadas no requirements.txt:
   pip install -r requirements.txt
3. Execução do Script Principal: Para processar os dados e gerar o dataset consolidado, execute o script principal:
   python scripts/main_script.py

## Relatório Power BI
O arquivo debentures_analysis_report.pbix no diretório power_bi contém um relatório interativo com visualizações das métricas principais das debêntures. Este relatório inclui gráficos de linha, cartões de métrica e filtros de segmentação.

O relatório do Power BI está disponível na pasta **power_bi/debentures_analysis_report.pbix**, para visualizar o relatório:
- Clique em View raw ou baixe diretamente o arquivo .pbix da pasta power_bi.
- Abra o Power BI Desktop.
- No Power BI Desktop, vá para Arquivo > Abrir e selecione o arquivo .pbix baixado.

## Consultas SQL
Dentro do banco de dados debentures.db, algumas consultas SQL foram implementadas para responder a perguntas específicas, como:

- Quantidade de debêntures listadas no dia anterior.
- Duration média das debêntures nos últimos 5 dias úteis.
- Códigos únicos de debêntures de uma empresa específica.

