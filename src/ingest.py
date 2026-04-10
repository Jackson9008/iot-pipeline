import pandas as pd
from database import get_engine

def process_csv():
    df = pd.read_csv('../data/temperature.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def save_to_db(df):
    engine = get_engine()
    df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    df = process_csv()
    save_to_db(df)
    print("Dados inseridos com sucesso!")
