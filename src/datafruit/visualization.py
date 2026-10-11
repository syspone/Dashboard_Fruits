# =============================================================================
# Gráficos
# -----------------------------------------------------------------------------
# Funções que recebem um DataFrame e devolvem figuras do Plotly. Ficam aqui
# para que o notebook e o dashboard usem exatamente o mesmo gráfico.
# =============================================================================
from pathlib import Path

import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure

from datafruit import config


def fruits_by_city_chart(df: pd.DataFrame) -> Figure:
    """Barras agrupadas: quantidade de cada fruta, uma cor por cidade."""
    return px.bar(
        df,
        x="Fruits",
        y="Amount",
        color="City",
        barmode="group",
        title="Quantidade de Frutas por Cidade",
        labels={"Fruits": "Fruta", "Amount": "Quantidade", "City": "Cidade"},
    )


def save_figure(fig: Figure, path: Path = config.FIGURE_FILE) -> Path:
    """Exporta a figura como PNG (usa o Kaleido)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_image(path, width=1000, height=600, scale=2)
    return path
