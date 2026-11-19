import csv
from collections import Counter
from pathlib import Path

from niantic_mlops.bands import churn_band

DATA = Path(__file__).parent.parent / "data"


def test_cuatro_clientes_en_riesgo_bajo_dos_medio_dos_alto():
    with open(DATA / "CHURN_MODEL.csv", encoding="utf-8") as fh:
        bandas = Counter(churn_band(float(r["prob_churn"]))[0] for r in csv.DictReader(fh))
    assert bandas == {"Bajo": 4, "Medio": 2, "Alto": 2}


def test_mobilityx_requiere_plan_de_retencion():
    assert churn_band(0.66) == ("Alto", "Plan de retención")
