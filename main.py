from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, EnergyRecord

app = FastAPI()


class EnergyInput(BaseModel):
    value: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Energy Database API is running"}


@app.get("/energy")
def get_energy():
    db = SessionLocal()
    records = db.query(EnergyRecord).all()
    db.close()

    values = [record.value for record in records]
    return {"energy_production": values}


@app.post("/add-energy")
def add_energy(new_energy: EnergyInput):
    db = SessionLocal()

    record = EnergyRecord(value=new_energy.value)
    db.add(record)
    db.commit()
    db.refresh(record)

    db.close()

    return {
        "message": "New energy value saved to database",
        "saved_value": record.value
    }


@app.get("/summary")
def get_summary():
    db = SessionLocal()
    records = db.query(EnergyRecord).all()
    db.close()

    values = [record.value for record in records]

    if not values:
        return {
            "average_energy": 0,
            "max_energy": 0,
            "min_energy": 0,
            "count": 0
        }

    average = sum(values) / len(values)
    maximum = max(values)
    minimum = min(values)
    count = len(values)

    return {
        "average_energy": average,
        "max_energy": maximum,
        "min_energy": minimum,
        "count": count
    }