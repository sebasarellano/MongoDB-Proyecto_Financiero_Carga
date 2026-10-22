# Pipeline ETL financiero con Python y MongoDB

Proyecto de ingeniería de datos que implementa un flujo **ETL (Extract, Transform, Load)** para preparar información financiera institucional y cargarla en colecciones de **MongoDB**. El código está orientado a datos del sector financiero ecuatoriano y utiliza Python para validar, normalizar y estructurar los archivos antes de su almacenamiento.

## Objetivo

Automatizar la transformación de archivos tabulares a documentos NoSQL, separando la información por tipo de entidad, volumen de crédito y eventos de supervisión. El proyecto permite practicar validación de entradas, conexión segura a una base MongoDB y operaciones de carga repetibles.

## Tecnologías

- Python
- pandas
- PyMongo
- MongoDB / MongoDB Atlas
- python-dotenv
- Excel como formato de entrada

## Flujo de trabajo

1. **Extracción:** lectura de los archivos Excel esperados desde la carpeta data/.
2. **Validación:** comprobación de que los archivos requeridos existan y contengan las columnas necesarias.
3. **Transformación:** normalización de valores faltantes y preparación de registros para su almacenamiento.
4. **Conexión:** lectura de la cadena de conexión desde la variable de entorno MONGO_URI y verificación de conectividad.
5. **Carga:** escritura en las colecciones de MongoDB mediante operaciones de actualización/inserción (*upsert*) para evitar borrar indiscriminadamente toda la colección antes de cargar datos.

## Colecciones de destino

| Colección | Contenido esperado |
|---|---|
| perfiles_entidad | Perfiles o características de las entidades financieras |
| volumen_credito_granular | Registros de volumen de crédito con mayor nivel de detalle |
| eventos_supervision | Registros de eventos de supervisión |

La estructura exacta de cada documento depende de las columnas presentes en los archivos de entrada y de las transformaciones implementadas en el script.

## Estructura del repositorio

- Carga_MongoDB_Financiero_Adaptado.py: script principal del proceso ETL.
- requirements.txt: dependencias de Python.
- .env.example: plantilla para configurar la conexión.
- .gitignore: evita versionar archivos locales como credenciales y datos de entrada.
- data/: carpeta local esperada para los archivos Excel de entrada; los archivos de datos no se distribuyen necesariamente con el repositorio.

## Requisitos previos

- Python 3.10 o una versión compatible.
- Una instancia local de MongoDB o una cuenta de MongoDB Atlas.
- Los tres archivos Excel de entrada esperados por el script.

## Instalación y configuración

1. Clona el repositorio y entra en la carpeta del proyecto.
2. Crea y activa un entorno virtual:

   ~~~bash
   python -m venv .venv
   ~~~

   En Windows:

   ~~~powershell
   .venv\Scripts\Activate.ps1
   ~~~

3. Instala las dependencias:

   ~~~bash
   pip install -r requirements.txt
   ~~~

4. Crea una copia local de .env.example con el nombre .env.
5. En .env, configura MONGO_URI con tu propia cadena de conexión. No publiques ese archivo ni incluyas credenciales en el código.
6. Coloca en data/ los archivos Excel requeridos por el script, con los nombres y las columnas que espera el código.

## Ejecución

Desde la raíz del repositorio, ejecuta:

~~~bash
python Carga_MongoDB_Financiero_Adaptado.py
~~~

El script comprueba la configuración de conexión y valida los archivos de entrada antes de iniciar la carga. La ejecución completa requiere una conexión válida y los archivos fuente correspondientes.

## Seguridad e integridad de los datos

- La URI de MongoDB se configura mediante MONGO_URI; no uses credenciales reales en el repositorio.
- Los archivos de entrada locales deben mantenerse fuera del control de versiones si contienen datos que no deben publicarse.
- Las operaciones *upsert* permiten actualizar o insertar registros coincidentes, pero **no eliminan automáticamente documentos antiguos que ya no aparecen en una nueva versión de los archivos fuente**.
- Si una ejecución se interrumpe, revisa las colecciones de destino antes de volver a procesar los datos.
- La estructura del pipeline está documentada, pero la reproducción depende de disponer de los archivos de entrada y de una instancia MongoDB configurada.

## Posibles mejoras

- Añadir pruebas automatizadas para las validaciones y las transformaciones.
- Incorporar un registro de ejecución (*logging*) con conteos de filas leídas, rechazadas y cargadas.
- Documentar la procedencia, fecha de corte y significado de cada variable de los archivos fuente.
- Definir una estrategia explícita para eliminar o marcar registros que desaparezcan de las fuentes.

## Aprendizajes

El proyecto aborda problemas habituales de ingeniería de datos: validación de archivos, normalización de datos tabulares, configuración segura de credenciales, modelado documental y carga repetible en una base NoSQL.
