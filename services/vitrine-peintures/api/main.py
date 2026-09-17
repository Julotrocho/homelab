from fastapi import FastAPI
from pydantic import BaseModel
import time, os, smtplib
from email.mime.text import MIMEText
import psycopg2

app = FastAPI()
start = time.time()

SMTP_USER = os.environ["SMTP_USER"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
DEST_EMAIL = os.environ["DEST_EMAIL"]
DB_PASSWORD = os.environ["DB_PASSWORD"]

def get_db_connection():
    return psycopg2.connect(
        host="db", dbname="contacts", user="contact", password=DB_PASSWORD
    )

@app.on_event("startup")
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            nom TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            recu_le TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

class ContactMessage(BaseModel):
    nom: str
    email: str
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/contact")
def contact(msg: ContactMessage):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO messages (nom, email, message) VALUES (%s, %s, %s)",
        (msg.nom, msg.email, msg.message)
    )
    conn.commit()
    cur.close()
    conn.close()

    corps = f"Nouveau message de {msg.nom} ({msg.email}) :\n\n{msg.message}"
    email_msg = MIMEText(corps)
    email_msg["Subject"] = f"Vitrine — message de {msg.nom}"
    email_msg["From"] = SMTP_USER
    email_msg["To"] = DEST_EMAIL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email_msg)

    return {"success": True}

@app.get("/messages")
def list_messages():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT nom, email, message, recu_le FROM messages ORDER BY recu_le DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"nom": r[0], "email": r[1], "message": r[2], "recu_le": r[3].isoformat()} for r in rows]
