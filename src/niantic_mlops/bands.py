"""Bandas de probabilidad de abandono (churn) y acción automática asociada."""
BANDS = [
    (0.20, "Bajo", "Seguimiento estándar"),
    (0.50, "Medio", "Reunión comercial"),
    (0.80, "Alto", "Plan de retención"),
    (1.00, "Crítico", "Escalado a Dirección"),
]


def churn_band(p: float) -> tuple[str, str]:
    """Devuelve (banda, acción) para una probabilidad de churn entre 0 y 1."""
    for upper, band, action in BANDS:
        if p <= upper:
            return band, action
    raise ValueError(f"probabilidad fuera de rango: {p}")
