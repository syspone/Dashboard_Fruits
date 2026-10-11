# =============================================================================
# Pipeline de dados
# -----------------------------------------------------------------------------
# Roda todas as etapas de ponta a ponta, sem precisar abrir notebook:
#     python -m datafruit.pipeline
# 1) lê data/raw  2) gera os resumos em data/processed  3) exporta o gráfico
# =============================================================================
from datafruit.data import load_fruits, save_processed, total_by
from datafruit.visualization import fruits_by_city_chart, save_figure


def main() -> None:
    df = load_fruits()
    print(f"Dados carregados: {len(df)} registros")

    for column, name in [("Fruits", "total_by_fruit"), ("City", "total_by_city")]:
        path = save_processed(total_by(df, column), name)
        print(f"Resumo salvo em {path}")

    path = save_figure(fruits_by_city_chart(df))
    print(f"Gráfico salvo em {path}")


if __name__ == "__main__":
    main()
