"""EBITDA por cliente y EBITDA en riesgo (EBITDA x probabilidad de abandono)."""
import csv
from collections import defaultdict
from pathlib import Path


def ebitda_por_cliente(data_dir: Path) -> dict[str, float]:
    tot: dict[str, float] = defaultdict(float)
    with open(data_dir / "FACT_INGRESOS.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            tot[r["cliente_id"]] += float(r["ingresos"]) - float(r["costes"])
    return dict(tot)


def ebitda_en_riesgo(data_dir: Path) -> dict[str, float]:
    with open(data_dir / "CHURN_MODEL.csv", encoding="utf-8") as fh:
        churn = {r["cliente_id"]: float(r["prob_churn"]) for r in csv.DictReader(fh)}
    return {c: e * churn[c] for c, e in ebitda_por_cliente(data_dir).items()}


def ebitda_expuesto(data_dir: Path, recall: float) -> float:
    """EBITDA en riesgo que el modelo NO detecta (1 - recall). Estimación ilustrativa."""
    return sum(ebitda_en_riesgo(data_dir).values()) * (1 - recall / 100)
