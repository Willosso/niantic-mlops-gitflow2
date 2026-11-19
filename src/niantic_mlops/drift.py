"""Semáforo de métricas del modelo y de la deriva (PSI)."""
import csv
from pathlib import Path

# (verde si >=, rojo si <) según el cuadro de umbrales de la memoria.
UMBRALES = {"accuracy": (90, 85), "precision": (85, 80), "recall": (85, 80), "f1_score": (88, 82)}
PSI_AMBAR, PSI_ROJO = 0.10, 0.20


def semaforo_metrica(nombre: str, valor: float) -> str:
    verde, rojo = UMBRALES[nombre]
    if valor >= verde:
        return "verde"
    return "rojo" if valor < rojo else "ámbar"


def semaforo_psi(psi: float) -> str:
    if psi < PSI_AMBAR:
        return "verde"
    return "rojo" if psi > PSI_ROJO else "ámbar"


def cargar_semanas(data_dir: Path) -> list[dict]:
    with open(data_dir / "MLOPS_MONITOR.csv", encoding="utf-8") as fh:
        ml = {int(r["semana"]): {k: float(v) for k, v in r.items()} for r in csv.DictReader(fh)}
    with open(data_dir / "DRIFT_MONITOR.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            ml[int(r["semana"])]["psi"] = float(r["psi"])
    return [ml[s] for s in sorted(ml)]
