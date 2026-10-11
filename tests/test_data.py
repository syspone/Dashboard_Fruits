import pandas as pd
import pytest

from datafruit.data import load_fruits, total_by


def test_load_fruits_reads_raw_csv():
    df = load_fruits()
    assert list(df.columns) == ["Fruits", "Amount", "City"]
    assert len(df) == 6
    assert df["Amount"].sum() == 18


def test_load_fruits_rejects_missing_columns(tmp_path):
    path = tmp_path / "bad.csv"
    pd.DataFrame({"Fruits": ["Maçã"], "Amount": [1]}).to_csv(path, index=False)
    with pytest.raises(ValueError, match="City"):
        load_fruits(path)


def test_total_by_city():
    result = total_by(load_fruits(), "City")
    assert result.iloc[0].to_dict() == {"City": "Curitiba", "Amount": 9}
    assert result.iloc[-1].to_dict() == {"City": "São Luís", "Amount": 3}


def test_total_by_fruit():
    result = total_by(load_fruits(), "Fruits")
    assert result.iloc[0].to_dict() == {"Fruits": "Melão", "Amount": 7}
