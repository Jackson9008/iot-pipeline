CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;

CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM timestamp) as hora,
COUNT(*) as contagem
FROM temperature_readings
GROUP BY hora;

CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(timestamp) as data,
MAX(temperature) as temp_max,
MIN(temperature) as temp_min
FROM temperature_readings
GROUP BY data;
