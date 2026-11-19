"""Disparadores de reentrenamiento y hotfix (regla multiseñal, hotfix v2.0.1).

Motivo del hotfix: con la regla original (solo PSI > 0,20) la alerta saltaba en la semana 7,
cuando la accuracy llevaba una semana en rojo (81 % en S6). Ver análisis empírico en la memoria.

T1 AVISO     accuracy < 90 %  o  PSI >= 0,10
T2 REENTRENAR PSI >= 0,10  y  caída de accuracy >= 2 puntos respecto a la semana anterior
T3 HOTFIX    accuracy < 85 %  o  PSI > 0,20   (incidencia, bloqueo de promoción y reentrenamiento urgente)
"""


def decidir(fila: dict, anterior: dict | None = None) -> str:
    caida = (anterior["accuracy"] - fila["accuracy"]) if anterior else 0
    if fila["psi"] > 0.20 or fila["accuracy"] < 85:
        return "HOTFIX"
    if fila["psi"] >= 0.10 and caida >= 2:
        return "REENTRENAR"
    if fila["accuracy"] < 90 or fila["psi"] >= 0.10:
        return "AVISO"
    return "OK"
