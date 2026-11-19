"""API mínima de salud y monitorización (stdlib). Sirve /health y /drift/latest."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from . import __version__
from .drift import cargar_semanas, semaforo_metrica, semaforo_psi
from .triggers import decidir

DATA = Path(__file__).resolve().parent.parent.parent / "data"


def payload_drift(data_dir: Path = DATA) -> dict:
    semanas = cargar_semanas(data_dir)
    ultima, previa = semanas[-1], (semanas[-2] if len(semanas) > 1 else None)
    return {
        "semana": int(ultima["semana"]),
        "accuracy": semaforo_metrica("accuracy", ultima["accuracy"]),
        "psi": ultima["psi"],
        "psi_estado": semaforo_psi(ultima["psi"]),
        "accion": decidir(ultima, previa),
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        rutas = {"/health": lambda: {"status": "ok", "version": __version__},
                 "/drift/latest": payload_drift}
        if self.path not in rutas:
            self.send_error(404)
            return
        body = json.dumps(rutas[self.path]()).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
