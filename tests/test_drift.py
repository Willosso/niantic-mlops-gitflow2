from pathlib import Path

from niantic_mlops.drift import cargar_semanas, semaforo_metrica, semaforo_psi
from niantic_mlops.triggers import decidir

DATA = Path(__file__).parent.parent / "data"


def test_semaforos_de_la_semana_7():
    s7 = cargar_semanas(DATA)[6]
    assert semaforo_metrica("accuracy", s7["accuracy"]) == "rojo"
    assert semaforo_psi(s7["psi"]) == "rojo"


def test_psi_ambar_en_semana_5():
    assert semaforo_psi(cargar_semanas(DATA)[4]["psi"]) == "ámbar"


def test_regla_original_solo_salta_en_semana_7():
    semanas = cargar_semanas(DATA)
    alertas = [int(f["semana"]) for i, f in enumerate(semanas) if decidir(f, semanas[i - 1] if i else None) == "HOTFIX"]
    assert alertas == [7]
