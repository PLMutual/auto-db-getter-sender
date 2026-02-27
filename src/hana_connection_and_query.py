import os
import json
import pandas as pd
from hdbcli import dbapi


def read_hana(sql: str, params=None) -> pd.DataFrame:
    """Lee una query en HANA y retorna un DataFrame."""
    return pd.read_sql(sql, conn, params=params)

def cleanup(file_path):
    os.remove(file_path)

print("Get ENV")
with open(".env", "r") as env_file: 
    dotenv = json.load(env_file)

# Fails if no .env file.
HANA_HOST = dotenv["HANA_HOST"]
HANA_PORT = dotenv["HANA_PORT"]
HANA_USER = dotenv["HANA_USER"]
HANA_PASS = dotenv["HANA_PASS"]

print("Connect to DB")
# Ends script if connection fails without raising Error
conn = dbapi.connect(
    address=HANA_HOST,
    port=HANA_PORT,
    user=HANA_USER,
    password=HANA_PASS
)

# Prepare SQL query
# Ajusta el nombre del objeto si en tu HANA es ZISH.PREV/... u otro path
VIEW_SOLICITUDES = '"_SYS_BIC"."ZISH/ZCV_SOLICITUDES"'  # <-- AJUSTA SI APLICA

# Traemos SOLO lo necesario para tu df final + la fecha para filtrar
sql = f"""
SELECT
    "SLCT_ID_SOLICITUD"      AS "N_ORDEN",
    "SLCT_AGENCIA_DERIVACION" AS "Agencia_derivación",
    "SLCT_ESTADO_DETALLE"     AS "Estado_detalle",
    "SLCT_FECHA_SOLICITUD"    AS "SLCT_FECHA_SOLICITUD"
FROM {VIEW_SOLICITUDES}
"""

print("Make query")
df = read_hana(sql)

print("Apply filters & transformations")
# =========================
# 4) Tipos y filtro desde 2025 en adelante
# =========================
# Convertir a fecha (robusto: soporta timestamp/string)
df["SLCT_FECHA_SOLICITUD"] = pd.to_datetime(df["SLCT_FECHA_SOLICITUD"], errors="coerce")

# Filtrar desde 2025-01-01 (incluye 2025 y 2026, etc.)
df = df[df["SLCT_FECHA_SOLICITUD"] >= pd.Timestamp("2025-01-01")].copy()

# Si quieres dejar solo tipo "date" (sin hora):
df["SLCT_FECHA_SOLICITUD"] = df["SLCT_FECHA_SOLICITUD"].dt.date

# Renombrar N_ORDEN -> "N° orden"
df = df.rename(columns={"N_ORDEN": "N° orden"})

# Mantener solo las columnas solicitadas, en el orden solicitado
df_final = df[["Agencia_derivación", "Estado_detalle", "SLCT_FECHA_SOLICITUD", "N° orden"]].copy()

print("Save")
df_final.to_csv("solicitudes_2025_plus.csv", index=False, encoding="utf-8-sig")

print("Ending connection to DB")
conn.close()


if __name__ == "__main__":
    print(HANA_HOST)
    print(HANA_PORT)

    print("df_final:")
    print(df_final.head())
    print(f"Filas: {len(df_final):,}")
    print("===")
    print(df.head())
    print("===")
    df_1 = df["Agencia_derivación"]
    print(df_1.head())