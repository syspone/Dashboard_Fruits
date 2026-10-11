# =============================================================================
# Carga e preparação dos dados
# -----------------------------------------------------------------------------
# Lê o CSV bruto (data/raw), confere se ele está no formato esperado e gera
# os resumos usados na análise (data/processed).
# =============================================================================
from pathlib import Path

import pandas as pd

from datafruit import config

# Colunas que o CSV precisa ter
EXPECTED_COLUMNS = ["Fruits", "Amount", "City"]


def load_fruits(path: Path = config.RAW_FRUITS_FILE) -> pd.DataFrame:
    """Lê o CSV de frutas e valida as colunas."""
    df = pd.read_csv(path)

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Colunas ausentes em {path.name}: {sorted(missing)}")

    if (df["Amount"] < 0).any():
        raise ValueError("A coluna Amount não pode ter valores negativos.")

    return df[EXPECTED_COLUMNS]


def total_by(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Soma a quantidade agrupando por uma coluna (ex.: 'Fruits' ou 'City')."""
    return (
        df.groupby(column, as_index=False)["Amount"]
        .sum()
        .sort_values("Amount", ascending=False, ignore_index=True)
    )


def save_processed(df: pd.DataFrame, name: str) -> Path:
    """Salva um DataFrame tratado em data/processed/<name>.csv."""
    config.PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = config.PROCESSED_DATA_DIR / f"{name}.csv"
    df.to_csv(path, index=False)
    return path
