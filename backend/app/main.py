from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, schemas

# 테이블이 없으면 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mock Hacking API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="User already exists")
    new = models.User(name=user.name, username=user.username, password=user.password)
    db.add(new)
    db.commit()
    db.refresh(new)
    return {"msg": "registered", "id": new.id}

@app.post("/api/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(
        models.User.username == user.username,
        models.User.password == user.password
    ).first()
    if not existing:
        raise HTTPException(status_code=401, detail="Bad creds")
    return {
        "msg": f"welcome {existing.username}",
        "user": {
            "name": existing.name,
            "username": existing.username
        }
    }
