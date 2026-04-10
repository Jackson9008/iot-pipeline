@echo off

echo 🚀 Subindo PostgreSQL...
cd docker
docker-compose up -d

timeout /t 5

cd ..

echo 📦 Instalando dependencias...
pip install -r requirements.txt

echo 📥 Inserindo dados...
cd src
python ingest.py

echo 🧠 Criando views...

python -c "
from sqlalchemy import create_engine
engine = create_engine('postgresql://iot_user:iot_pass@localhost:5432/iot_db')

sql = '''
CREATE VIEW IF NOT EXISTS avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;

CREATE VIEW IF NOT EXISTS leituras_por_hora AS
SELECT EXTRACT(HOUR FROM timestamp) as hora,
COUNT(*) as contagem
FROM temperature_readings
GROUP BY hora;

CREATE VIEW IF NOT EXISTS temp_max_min_por_dia AS
SELECT DATE(timestamp) as data,
MAX(temperature) as temp_max,
MIN(temperature) as temp_min
FROM temperature_readings
GROUP BY data;
'''

with engine.connect() as conn:
    conn.execute(sql)

print('Views criadas!')
"

cd ..

echo 🎉 Tudo pronto!
echo Rode agora: streamlit run dashboard/dashboard.py
