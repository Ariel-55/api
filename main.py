from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Demo FastAPI en Azure")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {
        "ok": True,
        "mensaje": "FastAPI funcionando correctamente"
    }

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {
        "mensaje": f"Hola {nombre}, esta respuesta viene desde FastAPI"
    }

@app.get("/suma")
def suma(a: int = 0, b: int = 0):
    return {
        "a": a,
        "b": b,
        "resultado": a + b
    }