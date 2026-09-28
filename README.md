# Dashboard Fruits

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-008DE4?style=for-the-badge&logo=plotly&logoColor=white)
![Kaleido](https://img.shields.io/badge/Kaleido-6C3483?style=for-the-badge)
![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)

## Sobre o Projeto

Projeto de análise de dados feito para praticar a criação de um DataFrame e sua visualização em um dashboard web.

O projeto usa dados fictícios de quantidade de frutas por cidade. Os dados são organizados em uma tabela com **Pandas**, transformados em um gráfico de barras com **Plotly** e exibidos em uma página web criada com **Dash**.

O projeto foi desenvolvido com finalidade educacional e de portfólio. O código é didático: cada passo vem comentado, para que quem está começando consiga acompanhar.

## Objetivos

- Criar um DataFrame a partir de um dicionário Python;
- Comparar a quantidade de cada fruta entre as cidades;
- Gerar um gráfico de barras agrupadas com Plotly Express;
- Exportar o gráfico como imagem (PNG);
- Publicar o gráfico em um dashboard web com Dash;
- Praticar visualização de dados com Python.

## Dados

O projeto usa um dataset fictício, criado dentro do próprio código, com três colunas:

- **Fruits**: nome da fruta (Maçã, Laranja, Melão e Uva);
- **Amount**: quantidade;
- **City**: cidade (Gramado, São Luís e Curitiba).

Ao todo são **6 registros**, com **4 frutas** e **3 cidades**.

| Fruits  | Amount | City     |
|---------|-------:|----------|
| Maçã    | 4      | Gramado  |
| Laranja | 1      | São Luís |
| Melão   | 2      | Gramado  |
| Laranja | 2      | São Luís |
| Uva     | 4      | Curitiba |
| Melão   | 5      | Curitiba |

## Análise

Foram analisados indicadores relacionados a:

- Quantidade total de frutas;
- Quantidade por fruta;
- Quantidade por cidade.

A soma de todas as quantidades é **18 unidades**.

O **Melão** é a fruta com maior quantidade, com **7 unidades** (2 em Gramado e 5 em Curitiba).

**Curitiba** tem a maior quantidade, com **9 unidades**, e **São Luís** a menor, com **3 unidades**.

## Demonstração

### Quantidade de Frutas por Cidade

![Quantidade de Frutas por Cidade](fruits.png)

*Gráfico de barras agrupadas gerado com Plotly: cada cor representa uma cidade.*

## Metodologia

O projeto foi desenvolvido em quatro etapas:

1. **Criação dos dados**: montagem do DataFrame com Pandas;
2. **Visualização**: criação do gráfico de barras agrupadas com Plotly Express;
3. **Exportação**: gravação do gráfico em `fruits.png` com Kaleido;
4. **Dashboard**: montagem da página com Dash e publicação em um servidor local.

## Como Executar

1. Instale as dependências (Python 3.14):

   ```bash
   pip install pandas plotly dash kaleido
   ```

2. Execute o script:

   ```bash
   python DataFruits.py
   ```

3. Abra [http://127.0.0.1:8050](http://127.0.0.1:8050) no navegador.

Para desligar o servidor, use `Ctrl+C` no terminal (ou o botão Stop do PyCharm).

## Tecnologias e Ferramentas

- **Python**
- **Pandas**
- **Plotly**
- **Dash**
- **Kaleido**
- **PyCharm**

## Estrutura do Projeto

```text
DataFruit/
│
├── DataFruits.py   # cria os dados, o gráfico e o dashboard
├── fruits.png      # imagem do gráfico exportada pelo script
└── README.md
```

## Objetivo de Aprendizagem

Este projeto foi desenvolvido para praticar e consolidar conhecimentos em:

- Criação e manipulação de DataFrames com Pandas;
- Visualização de dados com Plotly;
- Desenvolvimento de dashboards web com Dash;
- Exportação de gráficos como imagem;
- Organização e documentação de projetos.

## Autor

**Cristian Matias de Souza**, Analista de Dados
