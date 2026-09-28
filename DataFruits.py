# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Criado em.....: 07/09/2026 22:53
# Versão........: 2.0 (versão didática)
# -----------------------------------------------------------------------------
# Descrição.....: Criando dataframe e Gerando os Graficos no servidor
# Dependências..: Python 3.14, pandas, plotly, dash, kaleido
# =============================================================================
import pandas as pd            # pandas: monta e manipula tabelas (DataFrames)
import plotly.express as px    # plotly express: cria gráficos com uma linha
from dash import Dash, html, dcc  # dash: coloca o gráfico numa página web

# -----------------------------------------------------------------------------
# PASSO 1 - Criar o DataFrame
# Um DataFrame é uma tabela. Cada chave do dicionário vira uma coluna,
# e cada lista traz os valores daquela coluna (uma posição = uma linha).
# -----------------------------------------------------------------------------
df = pd.DataFrame({
    'Fruits': ['Maçã', 'Laranja', 'Melão', 'Laranja', 'Uva', 'Melão'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City':   ['Gramado', 'São Luís', 'Gramado', 'São Luís', 'Curitiba', 'Curitiba'],
})
print(df)

# -----------------------------------------------------------------------------
# PASSO 2 - Criar o gráfico
# x = o que vai no eixo horizontal, y = a altura das barras,
# color = separa as barras por cidade, barmode='group' = barras lado a lado.
# -----------------------------------------------------------------------------
fig = px.bar(df, x='Fruits', y='Amount', color='City', barmode='group')

# (Opcional) Salva o gráfico como imagem, para ver direto na IDE
fig.write_image('fruits.png', width=1000, height=600, scale=2)

# -----------------------------------------------------------------------------
# PASSO 3 - Montar a página com Dash
# O layout é a "cara" da página: uma lista de componentes, de cima para baixo.
#   html.H1   -> um título
#   dcc.Graph -> o espaço onde o gráfico do Plotly aparece
# -----------------------------------------------------------------------------
app = Dash()

app.layout = html.Div([
    html.H1('Dashboard Fruits'),
    dcc.Graph(figure=fig),
])

# -----------------------------------------------------------------------------
# PASSO 4 - Ligar o servidor
# Abra http://127.0.0.1:8050 no navegador.
# Para desligar, use o botão vermelho de Stop no PyCharm (ou Ctrl+C).
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # debug=True mostra os erros na própria página;
    # use_reloader=False impede que o script rode duas vezes
    app.run(debug=True, use_reloader=False)
