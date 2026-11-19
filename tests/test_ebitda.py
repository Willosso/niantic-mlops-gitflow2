from pathlib import Path

import pytest

from niantic_mlops.ebitda import ebitda_en_riesgo, ebitda_expuesto, ebitda_por_cliente

DATA = Path(__file__).parent.parent / "data"


def test_ebitda_total_1284k():
    assert sum(ebitda_por_cliente(DATA).values()) == 1_284_000


def test_ebitda_en_riesgo_204_5k():
    assert sum(ebitda_en_riesgo(DATA).values()) == pytest.approx(204_500)


def test_expuesto_crece_con_la_caida_del_recall():
    assert ebitda_expuesto(DATA, 71) == pytest.approx(59_305)
    assert ebitda_expuesto(DATA, 71) > ebitda_expuesto(DATA, 89) == pytest.approx(22_495)
