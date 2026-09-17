from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()
start = time.time()

class ContactMessage(BaseModel):
    nom: str
    email: str
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/contact")
def contact(msg: ContactMessage):
    # Pour l'instant, on log simplement le message reçu
    # Plus tard : envoi d'email, ou stockage en base
    print(f"Nouveau message de {msg.nom} ({msg.email}): {msg.message}")
    return {"success": True}
