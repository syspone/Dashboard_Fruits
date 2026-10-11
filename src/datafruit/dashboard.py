# =============================================================================
# Dashboard web com Dash
# -----------------------------------------------------------------------------
# Monta a página e liga o servidor. Para rodar:
#     python -m datafruit.dashboard
# e abra http://127.0.0.1:8050 no navegador (porta configurável no .env).
# =============================================================================
from dash import Dash, dcc, html

from datafruit import config
from datafruit.data import load_fruits
from datafruit.visualization import fruits_by_city_chart


def create_app() -> Dash:
    """Cria o app Dash com o layout da página."""
    df = load_fruits()

    app = Dash(__name__, title="Dashboard Fruits")
    app.layout = html.Div([
        html.H1("Dashboard Fruits"),
        dcc.Graph(figure=fruits_by_city_chart(df)),
    ])
    return app


def main() -> None:
    app = create_app()
    # use_reloader=False impede que o script rode duas vezes no modo debug
    app.run(
        host=config.DASH_HOST,
        port=config.DASH_PORT,
        debug=config.DASH_DEBUG,
        use_reloader=False,
    )


if __name__ == "__main__":
    main()
