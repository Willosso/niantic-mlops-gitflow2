FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PYTHONPATH=/app/src
WORKDIR /app
COPY src ./src
COPY data ./data
RUN useradd --system --uid 10001 mlops && chown -R mlops /app
USER mlops
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request as u; u.urlopen('http://localhost:8080/health')"
CMD ["python", "-m", "niantic_mlops.api"]
