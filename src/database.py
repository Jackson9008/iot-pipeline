from sqlalchemy import create_engine

DB_URL = "postgresql://iot_user:iot_pass@localhost:5432/iot_db"

def get_engine():
    return create_engine(DB_URL)
