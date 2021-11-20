from fastapi import Depends, FastAPI
from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session as DBSession

from api import schema
from api.database import Base, engine
from api.dependencies import get_db
from api.models import Reading, Run, Sensor, Session

app = FastAPI()

Base.metadata.create_all(bind=engine)


# Sessions
@app.post("/sessions/", response_model=schema.SessionResponse, tags=["sessions"])
def create_session(session: schema.SessionBase, db: DBSession = Depends(get_db)):
    session = Session(**session)  # Convert from Pydantic obj to SQLAlchemy obj
    db.add(session)
    db.commit()
    return session


@app.get("/sessions/{session_id}", response_model=schema.SessionResponse, tags=["sessions"])
def get_session(session_id: int, db: DBSession = Depends(get_db)):
    return db.execute(select(Session).where(Session.id == session_id)).first()


# Sensors
@app.post("/sensors/", response_model=schema.SensorResponse, tags=["sensors"])
def create_sensor(sensor: schema.SensorBase, db: DBSession = Depends(get_db)):
    sensor = Sensor(**sensor)  # Convert from Pydantic obj to SQLAlchemy obj
    db.add(sensor)
    db.commit()
    return sensor


@app.get("/sensors/{sensor_id}", response_model=schema.SensorResponse, tags=["sensors"])
def get_sensor(sensor_id: int, db: DBSession = Depends(get_db)):
    return db.execute(select(Sensor).where(Sensor.id == sensor_id)).first()


# Runs
@app.post("/runs/", response_model=schema.RunResponse, tags=["runs"])
def create_run(run: schema.RunBase, db: DBSession = Depends(get_db)):
    run = Run(**run)  # Convert from Pydantic obj to SQLAlchemy obj
    db.add(run)
    db.commit()
    return run


@app.get("/runs/{run_id}", response_model=schema.RunResponse, tags=["runs"])
def get_run(run_id: int, db: DBSession = Depends(get_db)):
    return db.execute(select(Run).where(Run.id == run_id)).first()


# Readings
@app.post("/readings/", response_model=schema.ReadingResponse, tags=["readings"])
def create_reading(reading: schema.ReadingBase, db: DBSession = Depends(get_db)):
    reading = Reading(**reading)  # Convert from Pydantic obj to SQLAlchemy obj
    db.add(reading)
    db.commit()
    return reading


@app.get("/readings/{reading_id}", response_model=schema.ReadingResponse, tags=["readings"])
def get_reading(reading_id: int, db: DBSession = Depends(get_db)):
    return db.execute(select(Reading).where(Reading.id == reading_id)).first()
