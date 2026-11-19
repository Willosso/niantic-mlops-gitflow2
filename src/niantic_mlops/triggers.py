"""Disparadores de reentrenamiento y hotfix."""


def decidir(fila: dict, anterior: dict | None = None) -> str:
    """Regla original: solo actúa cuando el PSI supera el umbral crítico de 0,20."""
    return "HOTFIX" if fila["psi"] > 0.20 else "OK"
