from niantic_mlops.api import payload_drift


def test_payload_ultima_semana_reentrenada():
    p = payload_drift()
    assert p["semana"] == 8 and p["psi_estado"] == "verde" and p["accion"] == "OK"
