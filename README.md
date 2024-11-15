# Debentures Analysis
Este projeto foi desenvolvido para atender ao desafio de análise de dados de debêntures do mercado secundário brasileiro, com aprimoramentos que agregam valor adicional. O projeto inclui scripts em Python para o processamento e consolidação de dados em um formato compatível com o Power BI. Além disso, foi criado um relatório completo no Power BI, proporcionando visualizações que facilitam a análise. Para enriquecer ainda mais o projeto e simplificar as consultas SQL sugeridas, foi implementado um banco de dados SQLite, permitindo consultas rápidas e dinâmicas. Essa estrutura visa tornar a análise de dados mais eficiente e acessível para a equipe de Research, indo além dos requisitos básicos do desafio.

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

