#  Análise nutricional de Fast Foods

Projeto de análise e tratamento de dados nutricionais de redes de fast food utilizando Python Pandas, com preparação dos dados para construção de dashboard no PowerBi.

---

## Objetivo

Realizar o processo de preparação e validação de dados (ETL leve) a partir de um dataset do Kaggle, garantindo:

- Padronização dos nomes das colunas
- Verificação de integridade dos dados
- Remoção de duplicatas
- Conversão correta de tipos numéricos
- Validação de valores inconsistentes
- Exportação de dataset tratado para BI

O foco do projeto é demonstrar organização, boas práticas e estruturação de código em projetos de dados.

---

## Estrutura do Projeto
dashboard-kaggle/
│
├── data/
│ ├── raw/ # Dados originais do Kaggle
├── src/
│ ├── padronizacao.py # Função de padronização de colunas
│ ├── verificacao.py # Funções de verificação de dados
│ └── tratamento.py # Funções de tratamento e conversão
│
├── app.py # Script principal
├── README.md
└── requirements.txt


---

## Tecnologias Utilizadas

- Python 3.11.6
- Pandas



## Etapas do Processo

1. Leitura do dataset original
2. Padronização dos nomes das colunas
3. Verificação de valores nulos
4. Remoção de duplicatas
5. Conversão de colunas para tipo numérico
6. Validação de valores negativos

---

## Como Executar o Projeto

### Clonar o repositório

```bash
git clone <jsjsjs>
