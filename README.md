# niantic-mlops · repositorio Git-Flow (Actividad 2)

Repositorio del proyecto *Business Analytics, MLOps y Riesgo* de Niantic Spatial
(Modelos de Servicio · Máster en Big Data · Universidad Europea).

- `src/niantic_mlops/`: código del modelo y de la operativa MLOps.
- `data/`: dataset sintético del proyecto (8 clientes, 5 meses, 8 semanas de monitorización).
- `tests/`: pruebas automáticas (`pytest -q`).

## Ejecución

```bash
pip install pytest && pytest -q                                   # pruebas
PYTHONPATH=src python -m niantic_mlops.quality_gate data/candidate_metrics.json   # puerta de calidad
docker build -t niantic-churn-api . && docker run -p 8080:8080 niantic-churn-api # API en /health y /drift/latest
```

## Git-Flow

`main` (versiones publicadas con tag) · `develop` (integración) · `feature/*` · `release/*` · `hotfix/*`.
El pipeline `.github/workflows/ci.yml` ejecuta pruebas → puerta de calidad → build de Docker → staging/producción.

## Transparencia

Historial reconstruido por el equipo para demostrar el flujo Git-Flow del proyecto. Cada commit indica el
**rol simulado** del caso (Data Scientist, MLOps Engineer, Risk Manager, Business Owner) y el apoyo de IA
recibido (ver la declaración de uso de IA de la memoria).
