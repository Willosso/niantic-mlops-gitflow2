# Changelog

## [2.0.1] - 2026-11-19 (hotfix/v2.0.1)
- Modelo de churn reentrenado con ventana ampliada (métricas de la semana 8: accuracy 93, precision 91, recall 90, F1 90).
- Regla de disparo multiseñal: AVISO / REENTRENAR / HOTFIX. El reentrenamiento salta en la semana 5 y la alerta roja en la 6 (antes, semana 7).

## [2.0.0] - 2026-11-19 (release/v2.0)
- Churn v2.0.0 validado con las métricas de la semana 1 (accuracy 92, precision 90, recall 89, F1 89): supera la puerta de calidad.
- Rating AAA-B con revisión humana para BB o inferior; semáforo de métricas y PSI con el disparador original (PSI > 0,20).
- API `/health` y `/drift/latest`, Dockerfile y pipeline CI/CD con puerta de calidad.
