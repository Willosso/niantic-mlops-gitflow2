"""Rating empresarial (AAA-B) a partir del score de riesgo 0-100 y política de seguimiento."""
RATINGS = [
    (90, "AAA", "Mantener crecimiento"),
    (80, "AA", "Promover servicios"),
    (70, "A", "Seguimiento periódico"),
    (60, "BBB", "Revisión trimestral"),
    (50, "BB", "Plan de retención"),
    (0, "B", "Intervención inmediata"),
]
# Rating a partir del cual la decisión deja de ser automática y exige revisión humana
# (alineado con EBA/GL/2020/06: supervisión humana de modelos automatizados de solvencia).
REVISION_HUMANA = {"BB", "B"}


def rating(score: float) -> tuple[str, str]:
    for minimum, label, action in RATINGS:
        if score >= minimum:
            return label, action
    raise ValueError(f"score fuera de rango: {score}")


def requiere_revision_humana(score: float) -> bool:
    return rating(score)[0] in REVISION_HUMANA
