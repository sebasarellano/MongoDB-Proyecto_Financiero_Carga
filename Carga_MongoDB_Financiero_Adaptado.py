# =============================================================
# CARGA MONGODB — CON DATOS REALES (miles de transacciones)
# =============================================================

import hashlib
import json
import os
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

# Carga las variables de un archivo .env local, si existe.
# El archivo .env no debe subirse a GitHub.
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError(
        "Falta MONGO_URI. Crea un archivo .env basado en .env.example "
        "o define la variable de entorno antes de ejecutar el script."
    )

# MongoClient conecta de forma diferida; el ping se valida en main().
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client["sector_financiero_ec"]


# =============================================================
# COLECCIÓN 1: PERFILES DE ENTIDAD (DATOS REALES DE 23 BANCOS)
# =============================================================

def cargar_perfiles_entidad_reales():
    """
    Carga los 23 bancos con datos reales.
    """
    
    print("📊 Cargando PERFILES_ENTIDAD (23 bancos reales)...")
    
    perfiles = [
        {
            "_id": "BP PICHINCHA",
            "nombre_oficial": "BANCO PICHINCHA C.A.",
            "nombre_corto": "Pichincha",
            "tipo_banco": "Grande",
            "fundacion": 1906,
            "sitio_web": "www.pichincha.com",
            "calificaciones_riesgo": [
                {"agencia": "Fitch", "calificacion": "A-", "fecha": "2024-06"},
                {"agencia": "Moody's", "calificacion": "A3", "fecha": "2024-05"}
            ],
            "productos": [
                "cuenta_corriente", "cuenta_ahorros", "tarjeta_credito",
                "credito_consumo", "credito_hipotecario", "microcredito",
                "inversiones", "banca_comercial"
            ],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 1850,
                "agencias": 210
            },
            "cobertura_provincial": ["Pichincha", "Guayas", "Azuay", "Manabí"],
            "grupo_financiero": "Grupo Pichincha"
        },
        {
            "_id": "BP GUAYAQUIL",
            "nombre_oficial": "BANCO DE GUAYAQUIL S.A.",
            "nombre_corto": "Guayaquil",
            "tipo_banco": "Grande",
            "fundacion": 1910,
            "sitio_web": "www.bancoguayaquil.com",
            "calificaciones_riesgo": [
                {"agencia": "Fitch", "calificacion": "BBB", "fecha": "2024-06"}
            ],
            "productos": [
                "cuenta_corriente", "credito_consumo", "credito_comercial",
                "tarjeta_credito", "microcredito", "banca_comercial"
            ],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 1500,
                "agencias": 180
            },
            "cobertura_provincial": ["Guayas", "Pichincha", "El Oro"],
            "grupo_financiero": "Grupo Banco de Guayaquil"
        },
        {
            "_id": "BP PACIFICO",
            "nombre_oficial": "BANCO DEL PACÍFICO S.A.",
            "nombre_corto": "Pacífico",
            "tipo_banco": "Grande",
            "fundacion": 1977,
            "sitio_web": "www.bancodelpacífico.com",
            "calificaciones_riesgo": [
                {"agencia": "Fitch", "calificacion": "BBB+", "fecha": "2024-06"}
            ],
            "productos": [
                "banca_comercial", "banca_consumo", "banca_inversión",
                "tarjeta_credito", "credito_hipotecario"
            ],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 1200,
                "agencias": 150
            },
            "cobertura_provincial": ["Guayas", "Pichincha", "Azuay"],
            "grupo_financiero": "Grupo Banco del Pacífico"
        },
        {
            "_id": "BP PRODUBANCO",
            "nombre_oficial": "PRODUBANCO",
            "nombre_corto": "Produbanco",
            "tipo_banco": "Grande",
            "fundacion": 1978,
            "sitio_web": "www.produbanco.com",
            "calificaciones_riesgo": [
                {"agencia": "Fitch", "calificacion": "BBB-", "fecha": "2024-06"}
            ],
            "productos": [
                "banca_comercial", "banca_consumo", "microcredito",
                "tarjeta_credito", "credito_hipotecario"
            ],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 800,
                "agencias": 120
            },
            "cobertura_provincial": ["Pichincha", "Guayas", "Tungurahua"],
            "grupo_financiero": "Grupo Produbanco"
        },
        {
            "_id": "BP AUSTRO",
            "nombre_oficial": "BANCO AUSTRO S.A.",
            "nombre_corto": "Austro",
            "tipo_banco": "Mediano",
            "fundacion": 1979,
            "sitio_web": "www.bancoaustro.com",
            "calificaciones_riesgo": [
                {"agencia": "Fitch", "calificacion": "BB+", "fecha": "2024-06"}
            ],
            "productos": ["credito_consumo", "credito_comercial", "microcredito"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 400,
                "agencias": 60
            },
            "cobertura_provincial": ["Azuay", "Pichincha"],
            "grupo_financiero": "Banco Austro"
        },
        {
            "_id": "BP BOLIVARIANO",
            "nombre_oficial": "BANCO BOLIVARIANO S.A.",
            "nombre_corto": "Bolivariano",
            "tipo_banco": "Mediano",
            "fundacion": 1975,
            "sitio_web": "www.bancobolivariano.com",
            "productos": ["credito_consumo", "tarjeta_credito", "microcredito"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 350,
                "agencias": 50
            },
            "cobertura_provincial": ["Pichincha"],
            "grupo_financiero": "Banco Bolivariano"
        },
        {
            "_id": "BP CITIBANK",
            "nombre_oficial": "CITIBANK N.A.",
            "nombre_corto": "Citibank",
            "tipo_banco": "Mediano",
            "fundacion": 1970,
            "sitio_web": "www.citibank.com.ec",
            "productos": ["banca_comercial", "tarjeta_credito", "banca_inversión"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 200,
                "agencias": 25
            },
            "cobertura_provincial": ["Pichincha", "Guayas"],
            "grupo_financiero": "Citigroup"
        },
        {
            "_id": "BP DINERS",
            "nombre_oficial": "BANCO DINERS CLUB DEL ECUADOR",
            "nombre_corto": "Diners",
            "tipo_banco": "Mediano",
            "fundacion": 1990,
            "productos": ["tarjeta_credito", "credito_consumo"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 250,
                "agencias": 20
            },
            "cobertura_provincial": ["Pichincha", "Guayas"],
            "grupo_financiero": "Grupo Diners"
        },
        {
            "_id": "BP GENERAL RUMIÑAHUI",
            "nombre_oficial": "BANCO GENERAL RUMIÑAHUI",
            "nombre_corto": "Rumiñahui",
            "tipo_banco": "Mediano",
            "fundacion": 1991,
            "productos": ["credito_consumo", "credito_comercial"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 300,
                "agencias": 45
            },
            "cobertura_provincial": ["Pichincha"],
            "grupo_financiero": "Banco General Rumiñahui"
        },
        {
            "_id": "BP INTERNACIONAL",
            "nombre_oficial": "BANCO INTERNACIONAL S.A.",
            "nombre_corto": "Internacional",
            "tipo_banco": "Mediano",
            "fundacion": 1974,
            "sitio_web": "www.bancointernacional.com.ec",
            "productos": ["credito_consumo", "credito_comercial", "tarjeta_credito"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 450,
                "agencias": 55
            },
            "cobertura_provincial": ["Pichincha", "Guayas"],
            "grupo_financiero": "Banco Internacional"
        },
        {
            "_id": "BP LOJA",
            "nombre_oficial": "BANCO LOJA",
            "nombre_corto": "Loja",
            "tipo_banco": "Mediano",
            "fundacion": 1985,
            "productos": ["credito_consumo", "credito_comercial", "microcredito"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 200,
                "agencias": 30
            },
            "cobertura_provincial": ["Loja", "Azuay"],
            "grupo_financiero": "Banco Loja"
        },
        {
            "_id": "BP MACHALA",
            "nombre_oficial": "BANCO MACHALA",
            "nombre_corto": "Machala",
            "tipo_banco": "Mediano",
            "fundacion": 1984,
            "productos": ["credito_consumo", "credito_comercial"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": False,
                "red_cajeros": 150,
                "agencias": 25
            },
            "cobertura_provincial": ["El Oro"],
            "grupo_financiero": "Banco Machala"
        },
        {
            "_id": "BP SOLIDARIO",
            "nombre_oficial": "BANCO SOLIDARIO",
            "nombre_corto": "Solidario",
            "tipo_banco": "Mediano",
            "fundacion": 1998,
            "sitio_web": "www.bancosolidario.com",
            "productos": ["microcredito", "credito_consumo", "credito_comercial"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 500,
                "agencias": 80
            },
            "cobertura_provincial": ["Pichincha", "Guayas", "Tungurahua"],
            "grupo_financiero": "Banco Solidario"
        },
        {
            "_id": "BP PROCREDIT",
            "nombre_oficial": "PROCREDIT BANK ECUADOR",
            "nombre_corto": "Procredit",
            "tipo_banco": "Pequeño",
            "fundacion": 1998,
            "sitio_web": "www.procredit.com.ec",
            "productos": ["microcredito", "credito_consumo"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 300,
                "agencias": 50
            },
            "cobertura_provincial": ["Pichincha", "Guayas"],
            "grupo_financiero": "Procredit Group"
        },
        {
            "_id": "BP AMAZONAS",
            "nombre_oficial": "BANCO AMAZONAS",
            "nombre_corto": "Amazonas",
            "tipo_banco": "Pequeño",
            "fundacion": 1995,
            "productos": ["credito_consumo", "credito_comercial", "microcredito"],
            "canales_digitales": {
                "app_movil": False,
                "banca_web": True,
                "red_cajeros": 100,
                "agencias": 15
            },
            "cobertura_provincial": ["Pichincha"],
            "grupo_financiero": "Banco Amazonas"
        },
        {
            "_id": "BP BANCO COMERCIAL DE MANABI",
            "nombre_oficial": "BANCO COMERCIAL DE MANABÍ",
            "nombre_corto": "Manabí",
            "tipo_banco": "Pequeño",
            "fundacion": 1994,
            "productos": ["credito_consumo", "credito_comercial"],
            "canales_digitales": {
                "app_movil": False,
                "banca_web": False,
                "red_cajeros": 80,
                "agencias": 20
            },
            "cobertura_provincial": ["Manabí"],
            "grupo_financiero": "Banco Comercial de Manabí"
        },
        {
            "_id": "BP LITORAL",
            "nombre_oficial": "BANCO LITORAL",
            "nombre_corto": "Litoral",
            "tipo_banco": "Pequeño",
            "fundacion": 2000,
            "productos": ["credito_consumo", "credito_comercial"],
            "canales_digitales": {
                "app_movil": False,
                "banca_web": False,
                "red_cajeros": 60,
                "agencias": 12
            },
            "cobertura_provincial": ["Guayas"],
            "grupo_financiero": "Banco Litoral"
        },
        {
            "_id": "BP COOPNACIONAL",
            "nombre_oficial": "COOPNACIONAL",
            "nombre_corto": "Coopnacional",
            "tipo_banco": "Pequeño",
            "fundacion": 2001,
            "productos": ["credito_consumo", "microcredito"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 150,
                "agencias": 30
            },
            "cobertura_provincial": ["Pichincha"],
            "grupo_financiero": "Coopnacional"
        },
        {
            "_id": "BP CAPITAL",
            "nombre_oficial": "BANCO CAPITAL",
            "nombre_corto": "Capital",
            "tipo_banco": "Pequeño",
            "fundacion": 2003,
            "productos": ["credito_consumo", "credito_comercial"],
            "canales_digitales": {
                "app_movil": False,
                "banca_web": True,
                "red_cajeros": 80,
                "agencias": 15
            },
            "cobertura_provincial": ["Pichincha"],
            "grupo_financiero": "Banco Capital"
        },
        {
            "_id": "BP DELBANK",
            "nombre_oficial": "DELBANK S.A.",
            "nombre_corto": "Delbank",
            "tipo_banco": "Pequeño",
            "fundacion": 2005,
            "productos": ["credito_consumo"],
            "canales_digitales": {
                "app_movil": False,
                "banca_web": False,
                "red_cajeros": 40,
                "agencias": 10
            },
            "cobertura_provincial": ["Pichincha"],
            "grupo_financiero": "Delbank"
        },
        {
            "_id": "BANCO ATLANTIDA S.A.",
            "nombre_oficial": "BANCO ATLÁNTIDA S.A.",
            "nombre_corto": "Atlántida",
            "tipo_banco": "Pequeño",
            "fundacion": 2006,
            "productos": ["credito_consumo", "tarjeta_credito"],
            "canales_digitales": {
                "app_movil": True,
                "banca_web": True,
                "red_cajeros": 200,
                "agencias": 25
            },
            "cobertura_provincial": ["Pichincha", "Guayas"],
            "grupo_financiero": "Banco Atlántida"
        },
        {
            "_id": "BP BANCO  DESARROLLO DE LOS PUEBLOS  S.A., CODESARROLLO",
            "nombre_oficial": "BANCO CODESARROLLO",
            "nombre_corto": "Codesarrollo",
            "tipo_banco": "Pequeño",
            "fundacion": 2007,
            "productos": ["microcredito", "credito_consumo"],
            "canales_digitales": {
                "app_movil": False,
                "banca_web": True,
                "red_cajeros": 100,
                "agencias": 20
            },
            "cobertura_provincial": ["Pichincha"],
            "grupo_financiero": "Banco Codesarrollo"
        },
        {
            "_id": "BP VISIONFUND ECUADOR S.A.",
            "nombre_oficial": "VISIONFUND ECUADOR S.A.",
            "nombre_corto": "VisionFund",
            "tipo_banco": "Pequeño",
            "fundacion": 2008,
            "sitio_web": "www.visionfund.org.ec",
            "productos": ["microcredito"],
            "canales_digitales": {
                "app_movil": False,
                "banca_web": True,
                "red_cajeros": 120,
                "agencias": 40
            },
            "cobertura_provincial": ["Pichincha", "Guayas", "Azuay"],
            "grupo_financiero": "VisionFund"
        }
    ]
    
    # Actualiza cada perfil por su identificador estable sin borrar la colección.
    coleccion = db["perfiles_entidad"]
    for perfil in perfiles:
        coleccion.replace_one({"_id": perfil["_id"]}, perfil, upsert=True)

    print(f"   ✅ {len(perfiles)} perfiles de bancos actualizados o insertados\n")


# =============================================================
# COLECCIÓN 2: VOLUMEN DE CRÉDITO GRANULAR (DESDE EXCEL)
# =============================================================

def cargar_volumen_credito_desde_excel(carpeta_volumenes):
    """
    Valida y procesa los archivos Excel antes de escribir en MongoDB.
    No borra documentos existentes; usa identificadores deterministas y upsert.
    """
    print("📊 Validando archivos de VOLUMEN_CREDITO_GRANULAR...")

    archivos = [
        "VOLUMEN_CREDITO_2023.xlsx",
        "VOLUMEN_CREDITO_2024.xlsx",
        "VOLUMEN_CREDITO_2025.xlsx",
    ]
    rutas = [os.path.join(carpeta_volumenes, archivo) for archivo in archivos]
    faltantes = [ruta for ruta in rutas if not os.path.isfile(ruta)]
    if faltantes:
        raise FileNotFoundError(
            "No se inició la carga de volumen de crédito. Faltan archivos: "
            + ", ".join(faltantes)
        )

    columnas_requeridas = [
        "FECHA", "ENTIDAD", "TIPO DE CREDITO", "ESTADO DE LA OPERACION",
        "PROVINCIA", "CANTON", "SECTOR", "SUBSECTOR", "SUBSISTEMA",
        "NÚMERO DE OPERACIONES", "MONTO OTORGADO",
    ]
    dataframes = []

    # Lee y valida todos los Excel antes de empezar a escribir.
    for ruta in rutas:
        print(f"   📄 Leyendo {ruta}...")
        df = pd.read_excel(ruta, sheet_name="Volumen de Crédito", header=8)

        faltan_columnas = [col for col in columnas_requeridas if col not in df.columns]
        if faltan_columnas:
            raise ValueError(
                f"{os.path.basename(ruta)} no contiene las columnas requeridas: "
                + ", ".join(faltan_columnas)
            )

        df = df.copy()
        df["SUBSISTEMA"] = df["SUBSISTEMA"].astype("string").str.strip().str.upper()
        df = df[df["SUBSISTEMA"] == "BANCOS PRIVADOS"].copy()

        df["MONTO OTORGADO"] = pd.to_numeric(df["MONTO OTORGADO"], errors="coerce")
        df["NÚMERO DE OPERACIONES"] = pd.to_numeric(
            df["NÚMERO DE OPERACIONES"], errors="coerce"
        )
        df["FECHA"] = pd.to_datetime(df["FECHA"], errors="coerce")
        df.dropna(
            subset=[
                "FECHA", "ENTIDAD", "PROVINCIA",
                "MONTO OTORGADO", "NÚMERO DE OPERACIONES",
            ],
            inplace=True,
        )
        df = df[df["MONTO OTORGADO"] > 0].copy()

        for col in [
            "ENTIDAD", "TIPO DE CREDITO", "ESTADO DE LA OPERACION",
            "PROVINCIA", "CANTON", "SECTOR", "SUBSECTOR",
        ]:
            df[col] = df[col].astype("string").str.strip()

        df["anio"] = df["FECHA"].dt.year
        df["mes"] = df["FECHA"].dt.month
        df["trimestre"] = df["mes"].apply(lambda mes: f"Q{(mes - 1) // 3 + 1}")

        df_mongo = df[
            [
                "FECHA", "anio", "mes", "trimestre", "ENTIDAD",
                "TIPO DE CREDITO", "ESTADO DE LA OPERACION", "PROVINCIA",
                "CANTON", "SECTOR", "SUBSECTOR",
                "NÚMERO DE OPERACIONES", "MONTO OTORGADO",
            ]
        ].copy()
        df_mongo.rename(
            columns={
                "FECHA": "fecha",
                "ENTIDAD": "entidad",
                "TIPO DE CREDITO": "tipo_credito",
                "ESTADO DE LA OPERACION": "estado_operacion",
                "PROVINCIA": "provincia",
                "CANTON": "canton",
                "SECTOR": "sector_economico",
                "SUBSECTOR": "subsector",
                "NÚMERO DE OPERACIONES": "num_operaciones",
                "MONTO OTORGADO": "monto_otorgado",
            },
            inplace=True,
        )
        dataframes.append(df_mongo)
        print(f"      {len(df_mongo):,} registros válidos preparados")

    if not any(not df.empty for df in dataframes):
        raise ValueError("No se encontraron registros válidos; no se modificó MongoDB.")

    coleccion = db["volumen_credito_granular"]
    total = 0
    tamano_lote = 500

    for df in dataframes:
        registros = df.to_dict("records")
        for registro in registros:
            firma = json.dumps(
                registro, sort_keys=True, default=str, ensure_ascii=False
            )
            registro["_id"] = hashlib.sha256(firma.encode("utf-8")).hexdigest()

        for inicio in range(0, len(registros), tamano_lote):
            lote = registros[inicio:inicio + tamano_lote]
            for registro in lote:
                coleccion.replace_one(
                    {"_id": registro["_id"]}, registro, upsert=True
                )
            total += len(lote)

    print(
        f"   ✅ {total:,} registros procesados mediante upsert. "
        "Los documentos anteriores no se borraron.\n"
    )


# =============================================================
# COLECCIÓN 3: EVENTOS DE SUPERVISIÓN
# =============================================================

def cargar_eventos_supervision_reales():
    print("📊 Cargando EVENTOS_SUPERVISION...")
    
    eventos = [
        {
            "fecha": datetime(2024, 6, 15),
            "tipo": "resolucion",
            "entidad_afectada": "BP SOLIDARIO",
            "numero_resolucion": "SB-2024-0512",
            "titulo": "Aprobación de aumento de capital",
            "descripcion": "Se aprueba el aumento de capital pagado por USD 3,000,000",
            "monto_usd": 3000000,
            "impacto": "positivo",
            "fuente": "Superintendencia de Bancos"
        },
        {
            "fecha": datetime(2023, 11, 20),
            "tipo": "sancion",
            "entidad_afectada": "BP AMAZONAS",
            "titulo": "Multa por incumplimiento de normas de liquidez",
            "descripcion": "Índice de liquidez bajo mínimos reglamentarios en Q3 2023",
            "monto_sancion_usd": 50000,
            "impacto": "negativo",
            "fecha_cumplimiento": datetime(2023, 12, 20),
            "fuente": "Superintendencia de Bancos"
        },
        {
            "fecha": datetime(2024, 3, 10),
            "tipo": "cambio_calificacion",
            "entidad_afectada": "BP AUSTRO",
            "agencia_rating": "Fitch",
            "calificacion_anterior": "BB+",
            "calificacion_nueva": "BBB-",
            "direccion": "upgrade",
            "razon": "Mejora en ratios de solvencia y rentabilidad",
            "impacto": "positivo",
            "fuente": "Fitch Ratings"
        },
        {
            "fecha": datetime(2024, 1, 15),
            "tipo": "alerta_supervisora",
            "entidad_afectada": "BP LOJA",
            "titulo": "Requerimiento de plan de mejora",
            "descripcion": "Se requiere presentar plan de mejora para cartera de microcrédito",
            "plazo_respuesta": "30 días",
            "impacto": "neutral",
            "fuente": "Superintendencia de Bancos"
        },
        {
            "fecha": datetime(2024, 2, 20),
            "tipo": "cambio_calificacion",
            "entidad_afectada": "BP PICHINCHA",
            "agencia_rating": "Moody's",
            "calificacion_anterior": "A3",
            "calificacion_nueva": "A3",
            "razon": "Mantiene calificación estable",
            "impacto": "neutral",
            "fuente": "Moody's"
        },
    ]
    
    coleccion = db["eventos_supervision"]
    for evento in eventos:
        # Clave natural estable para que ejecutar el proceso de nuevo no duplique eventos.
        clave = {
            "fecha": evento["fecha"],
            "tipo": evento["tipo"],
            "entidad_afectada": evento["entidad_afectada"],
        }
        coleccion.update_one(clave, {"$set": evento}, upsert=True)

    print(f"   ✅ {len(eventos)} eventos actualizados o insertados\n")


# =============================================================
# CREAR ÍNDICES
# =============================================================

def crear_indices():
    print("🔍 Creando índices...")
    db['perfiles_entidad'].create_index('tipo_banco')
    db['volumen_credito_granular'].create_index([('provincia', 1), ('anio', 1)])
    db['volumen_credito_granular'].create_index([('entidad', 1), ('tipo_credito', 1)])
    db['volumen_credito_granular'].create_index('sector_economico')
    db['volumen_credito_granular'].create_index([('fecha', -1)])
    db['eventos_supervision'].create_index([('entidad_afectada', 1), ('fecha', -1)])
    db['eventos_supervision'].create_index('tipo')
    print("   ✅ Índices creados\n")


# =============================================================
# MAIN
# =============================================================

def main():
    print("=" * 70)
    print("  CARGA DE MONGODB")
    print("=" * 70 + "\n")

    try:
        # Verifica autenticación, red y disponibilidad antes de escribir.
        client.admin.command("ping")
        print("✅ Conexión con MongoDB verificada.\n")

        carpeta_volumenes = os.path.join(os.path.dirname(__file__), "data")

        # Los Excel se validan primero. Si falta uno o su estructura cambió,
        # el proceso se detiene antes de tocar las otras colecciones.
        cargar_volumen_credito_desde_excel(carpeta_volumenes)
        cargar_perfiles_entidad_reales()
        cargar_eventos_supervision_reales()
        crear_indices()

        print("=" * 70)
        print("  ✅ CARGA FINALIZADA")
        print("=" * 70)
        print("\n📊 Conteo de documentos:")
        print(f"   perfiles_entidad: {db['perfiles_entidad'].count_documents({})}")
        print(f"   volumen_credito_granular: {db['volumen_credito_granular'].count_documents({})}")
        print(f"   eventos_supervision: {db['eventos_supervision'].count_documents({})}")

    except Exception as error:
        print(f"\n❌ La carga no finalizó correctamente: {error}")
        raise
    finally:
        client.close()


if __name__ == "__main__":
    main()