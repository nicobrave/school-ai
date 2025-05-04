# main.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
from supabase import create_client, Client
from openai import OpenAI
import math
import logging
from logging.handlers import RotatingFileHandler

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('app.log', maxBytes=10000000, backupCount=5),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 1) Carga de .env
load_dotenv()

# 2) Configuración desde variables de entorno
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MIN_SIMILARITY = float(os.getenv("MIN_SIMILARITY", 0.78))

# Validación de variables de entorno
if not all([SUPABASE_URL, SUPABASE_KEY, OPENAI_API_KEY]):
    logger.error("Faltan variables de entorno requeridas")
    raise ValueError("Faltan variables de entorno requeridas")

# 3) Inicializa clientes
try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    client = OpenAI(api_key=OPENAI_API_KEY)
    logger.info("Clientes inicializados correctamente")
except Exception as e:
    logger.error(f"Error al inicializar clientes: {str(e)}")
    raise

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0

# Ping para pruebas
@app.route('/api/ping')
def ping():
    logger.info("Ping recibido")
    return jsonify({"pong": True})

# Rutas fake
FAKE_DB = {
    'evaluaciones': [{'id':'e1','titulo':'Diagnóstico Lectura','descripcion':'Versión A/B diferenciada.'}],
    'actividades': [], 'planificador': [], 'tabulador': []
}

@app.route('/api/evaluaciones', methods=['GET','POST'])
def evaluaciones():
    if request.method == 'POST':
        data = request.json
        FAKE_DB['evaluaciones'].append(data)
        return jsonify(data), 201
    return jsonify(FAKE_DB['evaluaciones'])

@app.route('/api/actividades', methods=['GET','POST'])
def actividades():
    if request.method == 'POST':
        data = request.json
        FAKE_DB['actividades'].append(data)
        return jsonify(data), 201
    return jsonify(FAKE_DB['actividades'])

@app.route('/api/planificador', methods=['GET','POST'])
def planificador():
    if request.method == 'POST':
        data = request.json
        FAKE_DB['planificador'].append(data)
        return jsonify(data), 201
    return jsonify(FAKE_DB['planificador'])

@app.route('/api/tabulador', methods=['GET','POST'])
def tabulador():
    if request.method == 'POST':
        data = request.json
        FAKE_DB['tabulador'].append(data)
        return jsonify(data), 201
    return jsonify(FAKE_DB['tabulador'])

# Búsqueda semántica real
@app.route("/api/search")
def semantic_search():
    try:
        q = request.args.get("q", "").strip()
        if not q:
            logger.warning("Búsqueda sin parámetro 'q'")
            return jsonify({"error": 'Missing "q" parameter'}), 400

        try:
            n = int(request.args.get("n", 3))
        except ValueError:
            n = 3
            logger.warning(f"Valor inválido para 'n', usando valor por defecto: {n}")

        logger.info(f"Búsqueda iniciada: '{q}' con n={n}")

        # 1) OpenAI embedding
        try:
            response = client.embeddings.create(
                model="text-embedding-3-small",
                input=q
            )
            query_vector = response.data[0].embedding
            logger.info("Embedding generado exitosamente")
        except Exception as e:
            logger.error(f"Error al generar embedding: {str(e)}")
            return jsonify({"error": f"OpenAI embedding failed: {str(e)}"}), 500

        # 2) Supabase RPC
        try:
            rpc_response = supabase.postgrest.rpc(
                "match_documents_embeddings",
                {
                    "query_embedding": query_vector,
                    "match_count": n
                }
            ).execute()

            results = rpc_response.data if rpc_response.data else []
            logger.info(f"Búsqueda completada. Resultados encontrados: {len(results)}")
            
            return jsonify({
                "query": q,
                "results": results
            })

        except Exception as e:
            logger.error(f"Error en búsqueda Supabase: {str(e)}")
            return jsonify({"error": f"Supabase search failed: {str(e)}"}), 500

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    logger.info(f"Iniciando servidor en puerto {port}")
    app.run(host="0.0.0.0", port=port, debug=False)  # debug=False para producción