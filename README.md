# School AI - Plataforma Web de Asistencia Docente con IA

School AI es una plataforma web educativa basada en inteligencia artificial que apoya a docentes en la planificación, evaluación, análisis de datos y generación de actividades.

## 🚀 Características Principales

- Evaluaciones Diferenciadas
- Generador de Actividades
- Planificador de Clases
- Tabulación de Pruebas
- Sistema de Recomendaciones con RAG
- Consola de Administración

## 🛠️ Tecnologías

- Frontend: React + Tailwind
- Backend: Flask (Python)
- Base de datos: Supabase y pgvector
- Autenticación: Clerk
- Hosting: Render.com

## 📋 Requisitos Previos

- Python 3.8+
- Node.js 16+
- npm o yarn
- Cuenta en Supabase
- Cuenta en Clerk
- Cuenta en OpenAI

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/nicobrave/school-ai.git
cd school-ai
```

2. Configurar el backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configurar el frontend:
```bash
cd frontend
npm install
```

4. Configurar variables de entorno:
   - Crear archivo `.env` en la raíz del backend
   - Crear archivo `.env` en la raíz del frontend
   - Ver `.env.example` para las variables necesarias

## 🏃‍♂️ Ejecución

1. Iniciar el backend:
```bash
cd backend
source venv/bin/activate
python main.py
```

2. Iniciar el frontend:
```bash
cd frontend
npm run dev
```

## 📚 Documentación

- [Documentación de la API](docs/api.md)
- [Guía de Contribución](docs/contributing.md)
- [Guía de Despliegue](docs/deployment.md)

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, lee nuestra [guía de contribución](docs/contributing.md) para más detalles.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Estructura del Proyecto

```
schoolai/
├── backend/           # API Flask con búsqueda semántica
├── frontend/          # Aplicación React
├── minedocs/          # Documentos para embeddings
└── render.yml         # Configuración de despliegue
```

## Despliegue en Render

### 1. Configuración del Backend

1. Crear un nuevo servicio web en Render
2. Conectar con el repositorio de GitHub
3. Configurar las variables de entorno:
   ```
   PORT=8000
   FLASK_APP=main.py
   FLASK_ENV=production
   SECRET_KEY=(tu clave secreta)
   SUPABASE_URL=(tu URL de Supabase)
   SUPABASE_KEY=(tu clave de servicio de Supabase)
   OPENAI_API_KEY=(tu clave de OpenAI)
   ```

### 2. Configuración del Frontend

1. Crear otro servicio web en Render
2. Conectar con el mismo repositorio
3. Configurar las variables de entorno:
   ```
   VITE_SUPABASE_URL=(tu URL de Supabase)
   VITE_SUPABASE_KEY=(tu clave anónima de Supabase)
   VITE_CLERK_PUBLISHABLE_KEY=(tu clave de Clerk)
   VITE_API_URL=https://school-ai-backend.onrender.com
   ```

### 3. Verificación

1. Probar el endpoint `/api/ping` del backend
2. Verificar la búsqueda semántica
3. Comprobar la conexión del frontend

## Desarrollo Local

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # o `venv\Scripts\activate` en Windows
pip install -r requirements.txt
python main.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Tecnologías Utilizadas

- Backend: Flask, Supabase, OpenAI
- Frontend: React, Vite, Clerk
- Búsqueda: pgvector, embeddings
- Despliegue: Render 