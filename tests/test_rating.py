import csv
from pathlib import Path

from niantic_mlops.rating import rating, requiere_revision_humana

DATA = Path(__file__).parent.parent / "data"


def test_cartera_coincide_con_la_memoria():
    esperado = {"C001": "AAA", "C002": "AA", "C003": "A", "C004": "BBB",
                "C005": "AAA", "C006": "BB", "C007": "A", "C008": "AAA"}
    with open(DATA / "RISK_SCORE.csv", encoding="utf-8") as fh:
        obtenido = {r["cliente_id"]: rating(float(r["score_riesgo"]))[0] for r in csv.DictReader(fh)}
    assert obtenido == esperado


def test_bb_exige_revision_humana():
    assert requiere_revision_humana(57) and not requiere_revision_humana(61)
