# =============================================================
# CARGA MONGODB — CON DATOS REALES (miles de transacciones)
# =============================================================

from pymongo import MongoClient
import pandas as pd
from datetime import datetime
import os

# Conexión a MongoDB usando variables de entorno (Más seguro para GitHub)
# Si no encuentra la variable de entorno, usa una estructura de respaldo de ejemplo
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://usuario:contraseña@cluster0.sh0uytt.mongodb.net/?appName=Cluster0")
client = MongoClient(MONGO_URI)
db = client['sector_financiero_ec']

print("✅ Conectado a MongoDB\n")


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
    
    coleccion = db['perfiles_entidad']
    coleccion.delete_many({})
    
    resultado = coleccion.insert_many(perfiles)
    print(f"   ✅ {len(resultado)} perfiles de bancos cargados\n")


# =============================================================
# COLECCIÓN 2: VOLUMEN DE CRÉDITO GRANULAR (DESDE EXCEL)
# =============================================================

def cargar_volumen_credito_desde_excel(carpeta_volumenes):
    """
    Lee directamente los archivos Excel de volumen de crédito
    y carga los registros a MongoDB
    """
    
    print("📊 Cargando VOLUMEN_CREDITO_GRANULAR desde Excel...")
    
    archivos = [
        "VOLUMEN_CREDITO_2023.xlsx",
        "VOLUMEN_CREDITO_2024.xlsx",
        "VOLUMEN_CREDITO_2025.xlsx",
    ]
    
    coleccion = db['volumen_credito_granular']
    coleccion.delete_many({})
    
    total_registros = 0
    
    for archivo in archivos:
        ruta = os.path.join(carpeta_volumenes, archivo)
        
        if not os.path.exists(ruta):
            print(f"   ⚠️  No encontrado: {ruta}")
            continue
        
        print(f"   📄 Leyendo {archivo}...")
        
        try:
            df = pd.read_excel(
                ruta,
                sheet_name='Volumen de Crédito',
                header=8,
                dtype={
                    "NÚMERO DE OPERACIONES": int,
                    "MONTO OTORGADO": float,
                }
            )
            
            print(f"      {len(df):,} filas leídas")
            
            df = df[df["SUBSISTEMA"].str.strip().str.upper() == "BANCOS PRIVADOS"].copy()
            
            df.dropna(subset=["FECHA", "ENTIDAD", "PROVINCIA", "MONTO OTORGADO"], inplace=True)
            df = df[df["MONTO OTORGADO"] > 0].copy()
            
            for col in ["ENTIDAD", "TIPO DE CREDITO", "PROVINCIA", "SECTOR"]:
                df[col] = df[col].astype(str).str.strip()
            
            df["FECHA"] = pd.to_datetime(df["FECHA"])
            df["anio"] = df["FECHA"].dt.year
            df["mes"] = df["FECHA"].dt.month
            df["trimestre"] = df["mes"].apply(lambda m: f"Q{(m-1)//3 + 1}")
            
            df_mongo = df[[
                "FECHA", "anio", "mes", "trimestre",
                "ENTIDAD", "TIPO DE CREDITO", "ESTADO DE LA OPERACION",
                "PROVINCIA", "CANTON", "SECTOR", "SUBSECTOR",
                "NÚMERO DE OPERACIONES", "MONTO OTORGADO"
            ]].copy()
            
            df_mongo.rename(columns={
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
            }, inplace=True)
            
            registros = df_mongo.to_dict('records')
            
            if registros:
                coleccion.insert_many(registros, ordered=False)
                total_registros += len(registros)
                print(f"      ✅ {len(registros):,} registros cargados")
        
        except Exception as e:
            print(f"      ❌ Error leyendo {archivo}: {e}")
    
    print(f"   ✅ TOTAL: {total_registros:,} registros de volumen cargados\n")


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
    
    coleccion = db['eventos_supervision']
    coleccion.delete_many({})
    
    resultado = coleccion.insert_many(eventos)
    print(f"   ✅ {len(resultado)} eventos de supervisión cargados\n")


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
    print("  CARGA DE MONGODB — CON DATOS REALES")
    print("=" * 70 + "\n")
    
    # Ruta relativa limpia orientada al proyecto
    CARPETA_VOLUMENES = "./data"
    
    cargar_perfiles_entidad_reales()
    cargar_volumen_credito_desde_excel(CARPETA_VOLUMENES)
    cargar_eventos_supervision_reales()
    crear_indices()
    
    print("=" * 70)
    print("  ✅ MONGODB CARGADO CORRECTAMENTE")
    print("=" * 70)
    print("\n📊 Estadísticas de carga:")
    print(f"   perfiles_entidad: {db['perfiles_entidad'].count_documents({})}")
    print(f"   volumen_credito_granular: {db['volumen_credito_granular'].count_documents({})}")
    print(f"   eventos_supervision: {db['eventos_supervision'].count_documents({})}")


if __name__ == "__main__":
    main()