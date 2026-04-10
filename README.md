# 🚀 Pipeline de Dados com IoT, Docker e Streamlit

## 📌 Sobre o Projeto

Este projeto tem como objetivo construir um **pipeline de dados completo** para processamento de informações provenientes de dispositivos IoT (sensores de temperatura).

A solução envolve a ingestão, processamento, armazenamento e visualização de dados utilizando tecnologias modernas de Big Data.

---

## 🎯 Objetivo

Desenvolver um pipeline capaz de:

* 📥 Coletar dados de temperatura (CSV)
* ⚙️ Processar os dados com Python
* 🗄️ Armazenar no PostgreSQL (Docker)
* 📊 Criar análises com SQL (Views)
* 📈 Visualizar dados com Streamlit

---

## 🧰 Tecnologias Utilizadas

* 🐍 Python
* 🐳 Docker
* 🐘 PostgreSQL
* 📊 Streamlit
* 📈 Plotly
* 📦 Pandas
* 🔗 SQLAlchemy

---

## 📁 Estrutura do Projeto

```bash
iot-pipeline/
│
├── data/                  # Base de dados (CSV)
├── src/                   # Scripts Python
│   ├── ingest.py
│   ├── database.py
│   └── views.sql
│
├── dashboard/             # Aplicação Streamlit
│   └── dashboard.py
│
├── docker/                # Configuração do PostgreSQL
│   └── docker-compose.yml
│
├── docs/                  # Documentação
│   └── relatorio.pdf
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Como Executar o Projeto

### 🔹 1. Clonar o repositório

```bash
git clone <https://github.com/Jackson9008/iot-pipeline.git>
cd iot-pipeline
```

---

### 🔹 2. Subir o banco de dados (Docker)

```bash
cd docker
docker compose up -d
cd ..
```

---

### 🔹 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Inserir dados no banco

```bash
cd src
python ingest.py
cd ..
```

---

### 🔹 5. Criar as Views SQL

```bash
python -c "
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://iot_user:iot_pass@localhost:5432/iot_db')

queries = [
'''CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;''',

'''CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM timestamp) as hora,
COUNT(*) as contagem
FROM temperature_readings
GROUP BY hora;''',

'''CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(timestamp) as data,
MAX(temperature) as temp_max,
MIN(temperature) as temp_min
FROM temperature_readings
GROUP BY data;'''
]

with engine.connect() as conn:
    for q in queries:
        conn.execute(text(q))
    conn.commit()
"
```

---

### 🔹 6. Executar o Dashboard

```bash
python -m streamlit run dashboard/dashboard.py
```

👉 Acesse: http://localhost:8501

---

## 📊 Dashboard

O dashboard apresenta:

* 📊 Média de temperatura por dispositivo
* ⏱ Leituras por hora
* 🌡 Temperaturas máximas e mínimas por dia

---

## 🧠 Views SQL

### 1. avg_temp_por_dispositivo

Calcula a média de temperatura por sensor.

### 2. leituras_por_hora

Analisa a distribuição das leituras ao longo do dia.

### 3. temp_max_min_por_dia

Mostra variações térmicas diárias.

---

## 📊 Base de Dados

Dataset utilizado:

🔗 https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices

---

## 💡 Insights

* Identificação de padrões de temperatura
* Análise de comportamento por dispositivo
* Variações térmicas ao longo do tempo

---

## 🚀 Aplicações Reais

* Monitoramento industrial
* Agricultura inteligente
* Controle ambiental
* Smart cities

---

## 📌 Autor

**Jackson Sousa**
   Jr DevOps 


---

## 📎 Observações

Este projeto foi desenvolvido para fins acadêmicos, aplicando conceitos de:

* IoT
* Big Data
* Engenharia de Dados

---
