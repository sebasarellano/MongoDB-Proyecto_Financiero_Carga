# MongoDB-Proyecto_Financiero_Carga
Pipeline ETL en Python para la extracción, limpieza e ingesta de datos financieros masivos hacia una base de datos NoSQL en MongoDB.

# 🏦 ETL e Ingesta de Datos de Instituciones Financieras en MongoDB

## 📌 Descripción del Proyecto
Este proyecto forma parte de un desarrollo más amplio enfocado en la gestión y almacenamiento eficiente de información del sector financiero ecuatoriano. Su objetivo principal es automatizar el proceso de extracción, transformación y carga (**ETL**) de datos institucionales hacia una base de datos NoSQL (**MongoDB**), optimizando las consultas y el almacenamiento de documentos semi-estructurados.

## 🚀 Características Principales
- **Conexión y Gestión NoSQL:** Implementación de flujos de conexión seguros y operaciones CRUD utilizando `PyMongo`.
- **Procesamiento de Datos:** Limpieza, normalización y estructuración previa de registros financieros masivos utilizando Python.
- **Arquitectura Escalable:** Diseño pensado para manejar esquemas flexibles adaptados a la variabilidad de los reportes financieros.

## 🛠️ Tecnologías y Librerías Utilizadas
- **Lenguaje:** Python
- **Base de Datos:** MongoDB / MongoDB Atlas
- **Librerías:** `pymongo`, `pandas`, `json` *(agrega las que hayas usado)*

## ⚙️ Estructura del Código
- `src/load_mongo.py`: Script principal encargado de conectar con el cluster de MongoDB e insertar la data procesada en colecciones específicas.
- *(Añade una breve mención de los otros scripts si tienes separación de código)*.

## 💡 Aprendizajes y Retos
*Diseñar este pipeline permitió entender los retos de lidiar con esquemas dinámicos en bases de datos NoSQL frente a las relacionales tradicionales, asegurando una carga eficiente sin pérdida de integridad en los datos financieros.*
