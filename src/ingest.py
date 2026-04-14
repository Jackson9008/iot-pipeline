import pandas as pd
from pathlib import Path
from sqlalchemy import text
from database import get_engine

def process_csv():
    BASE_DIR = Path(__file__).resolve().parent.parent
    csv_path = BASE_DIR / "data" / "temperature.csv"

    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    return df

def save_to_db(df):
    engine = get_engine()
    df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
    return engine

def create_views(engine):
    BASE_DIR = Path(__file__).resolve().parent
    sql_path = BASE_DIR / "views.sql"

    with open(sql_path, 'r') as file:
        sql_commands = file.read().split(';')

    with engine.connect() as conn:
        for command in sql_commands:
            if command.strip():
                conn.execute(text(command))
        conn.commit()

if __name__ == "__main__":
    print(" Processando CSV...")
    df = process_csv()

    print(" Salvando no banco...")
    engine = save_to_db(df)

    print(" Criando views...")
    create_views(engine)

    print(" Pipeline finalizado com sucesso!")