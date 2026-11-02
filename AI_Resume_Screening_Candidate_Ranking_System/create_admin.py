"""Run locally to create an admin. There is intentionally no public admin signup."""
import sqlite3
from pathlib import Path
from getpass import getpass
from datetime import datetime
from werkzeug.security import generate_password_hash
db=Path(__file__).resolve().parent/"hirelens.db"
name=input("Admin name: ").strip(); email=input("Admin email: ").strip().lower(); password=getpass("Password (minimum 8 characters): ")
if not name or not email or len(password)<8:
 print("Name and email are required; password must have at least 8 characters.")
else:
 with sqlite3.connect(db) as c:
  c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,password_hash TEXT NOT NULL,role TEXT NOT NULL CHECK(role IN('admin','candidate')),created_at TEXT NOT NULL)")
  try:
   c.execute("INSERT INTO users(name,email,password_hash,role,created_at) VALUES(?,?,?,?,?)",(name,email,generate_password_hash(password),"admin",datetime.now().strftime("%Y-%m-%d %H:%M")))
   print("Admin created. Run app.py and log in.")
  except sqlite3.IntegrityError: print("This email already exists.")
