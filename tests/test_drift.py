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


def _acciones():
    semanas = cargar_semanas(DATA)
    return [decidir(f, semanas[i - 1] if i else None) for i, f in enumerate(semanas)]


def test_regla_multiseñal_adelanta_el_reentrenamiento_a_la_semana_5():
    assert _acciones() == ["OK", "OK", "OK", "AVISO", "REENTRENAR", "HOTFIX", "HOTFIX", "OK"]


def test_la_alerta_roja_llega_una_semana_antes_que_con_la_regla_original():
    acciones = _acciones()
    assert acciones.index("HOTFIX") + 1 == 6  # antes: semana 7 (solo PSI > 0,20)
