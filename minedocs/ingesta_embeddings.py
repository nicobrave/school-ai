import os
import fitz  # PyMuPDF
import tiktoken
from openai import OpenAI
from supabase import create_client, Client
from dotenv import load_dotenv
import time

# Cargar variables de entorno
load_dotenv()

# Configuración
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBED_MODEL = "text-embedding-3-small"
PDF_DIR = os.path.expanduser("~/Desktop/schoolai/minedocs")

# Inicialización de clientes
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
client = OpenAI(api_key=OPENAI_API_KEY)

# Funciones
def extraer_texto_por_bloques(pdf_path, tokens_por_bloque=300):
    try:
        doc = fitz.open(pdf_path)
        texto_total = " ".join([page.get_text() for page in doc])
        doc.close()
        
        encoding = tiktoken.encoding_for_model("gpt-4")
        tokens = encoding.encode(texto_total)
        bloques = [tokens[i:i+tokens_por_bloque] for i in range(0, len(tokens), tokens_por_bloque)]
        return [encoding.decode(b) for b in bloques]
    except Exception as e:
        print(f"Error al extraer texto de {pdf_path}: {e}")
        return []

def procesar_documento(pdf_path):
    nombre = os.path.basename(pdf_path)
    bloques = extraer_texto_por_bloques(pdf_path)

    if not bloques:
        print(f"No se pudieron extraer bloques de {nombre}")
        return

    print(f"Iniciando procesamiento: {nombre} | {len(bloques)} bloques")

    for i, bloque in enumerate(bloques):
        try:
            # Agregar un pequeño retraso para evitar límites de tasa
            if i > 0 and i % 10 == 0:
                time.sleep(1)

            response = client.embeddings.create(
                input=bloque,
                model=EMBED_MODEL
            )
            
            # La nueva API devuelve los embeddings directamente
            embedding = response.data[0].embedding
            
            supabase.table("documentos_embeddings").insert({
                "fuente": nombre,
                "fragmento": bloque,
                "embedding": embedding
            }).execute()
            
            print(f"[{i+1}/{len(bloques)}] Insertado bloque de {nombre}")
        except Exception as e:
            print(f"Error en bloque {i+1} de {nombre}: {e}")
            # Agregar un retraso más largo si hay un error
            time.sleep(5)

def procesar_carpeta():
    archivos_pdf = [f for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]
    print(f"Encontrados {len(archivos_pdf)} archivos PDF para procesar")
    
    for archivo in archivos_pdf:
        ruta_completa = os.path.join(PDF_DIR, archivo)
        print(f"\nProcesando: {archivo}")
        procesar_documento(ruta_completa)
        print(f"Completado: {archivo}\n")

# Ejecutar
if __name__ == "__main__":
    try:
        procesar_carpeta()
        print("\nProcesamiento completado exitosamente!")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario")
    except Exception as e:
        print(f"\nError general: {e}")
