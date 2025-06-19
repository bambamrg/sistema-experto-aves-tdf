from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os # Importar el módulo os
from fastapi.middleware.cors import CORSMiddleware # <<-- Asegúrate de que esta línea esté presente

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # <<-- ESTA ES CLAVE: la URL donde corre tu frontend de React
    # Si en algún momento tu React corre en otro dominio/puerto (ej. una IP en red local, o un dominio de despliegue),
    # también deberías añadirlo aquí.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)

# Cargar el árbol de decisión desde el archivo JSON
DECISION_TREE = {}
ARBOL_JSON_PATH = 'arbol.json'

# Verificar si el archivo arbol.json existe, si no, crearlo con el contenido de ejemplo
if not os.path.exists(ARBOL_JSON_PATH):
    sample_tree_content = {
        "__v": 1,
        "description": "Guion JSON para la representación del conocimiento de aves autóctonas de Tierra del Fuego",
        "domain": "Biodiversidad de Tierra del Fuego",
        "subdomain": "Aves Autóctonas de Tierra del Fuego",
        "representation_type": "Árbol de Decisión",
        "nodes": [
            {
                "id": "root",
                "question": "¿Tamaño?",
                "options": [
                    {"value": "Pequeño", "next": "pequeno_habitat"},
                    {"value": "Mediano", "next": "mediano_habitat"},
                    {"value": "Grande", "next": "grande_habitat"}
                ]
            },
            {
                "id": "pequeno_habitat",
                "question": "¿Hábitat Principal?",
                "options": [
                    {"value": "Bosque", "next": "pequeno_bosque_color"},
                    {"value": "Costa", "next": "pequeno_costa_color"},
                    {"value": "Humedal", "next": "pequeno_humedal_color"}
                ]
            },
            {
                "id": "pequeno_costa_color",
                "question": "¿Coloración Predominante del Plumaje?",
                "options": [
                    {"value": "Marron/Gris", "result": "Playerito Rabadilla Blanca (Calidris Fuscicollis)"}
                ]
            },
            {
                "id": "pequeno_bosque_color",
                "question": "¿Coloración Predominante del Plumaje?",
                "options": [
                    {"value": "Blanco", "result": "Rayadito (Aphrastura spinicauda)"},
                    {"value": "Negro/Blanco", "result": "Picaflor Rubí (Sephanoides sephaniodes)"}
                ]
            },
            {
                "id": "pequeno_humedal_color",
                "question": "¿Coloración Predominante del Plumaje?",
                "options": [
                    {"value": "Gris/Blanco", "result": "Pitotoy Chico (Tringa Flavipes)"}
                ]
            },
            {
                "id": "mediano_habitat",
                "question": "¿Hábitat Principal?",
                "options": [
                    {"value": "Bosque", "next": "mediano_bosque_color"},
                    {"value": "Costa", "next": "mediano_costa_color"},
                    {"value": "Estepa", "next": "mediano_estepa_color"}
                ]
            },
            {
                "id": "mediano_costa_color",
                "question": "¿Coloración Predominante del Plumaje?",
                "options": [
                    {"value": "Negro/Blanco", "result": "Gaviota Cocinera (Larus Domnicanus)"}
                ]
            },
            {
                "id": "mediano_bosque_color",
                "question": "¿Coloración Predominante del Plumaje?",
                "options": [
                    {"value": "Negro/Blanco/Rojo", "result": "Carpintero Gigante (Campephilus Magellanicus)"}
                ]
            },
            {
                "id": "mediano_estepa_color",
                "question": "¿Coloración Predominante del Plumaje?",
                "options": [
                    {"value": "Marron/Gris", "result": "Águila Mora (Geranoaetus Melanoleucus)"}
                ]
            },
            {
                "id": "grande_habitat",
                "question": "¿Hábitat Principal?",
                "options": [
                    {"value": "Costa", "next": "grande_costa_color"},
                    {"value": "Estepa", "next": "grande_estepa_color"}
                ]
            },
            {
                "id": "grande_costa_color",
                "question": "¿Coloración Predominante del Plumaje?",
                "options": [
                    {"value": "Negro", "result": "Albatros Ceja Negra (Thalassarche Melanophris)"}
                ]
            },
            {
                "id": "grande_estepa_color",
                "question": "¿Coloración Predominante del Plumaje?",
                "options": [
                    {"value": "Negro", "result": "Condor Andino (Vultur Gryphus)"}
                ]
            }
        ]
    }
    with open(ARBOL_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(sample_tree_content, f, indent=2, ensure_ascii=False)
    print(f"Archivo '{ARBOL_JSON_PATH}' creado con contenido de ejemplo.")


try:
    with open(ARBOL_JSON_PATH, 'r', encoding='utf-8') as f:
        DECISION_TREE = json.load(f)
except FileNotFoundError:
    raise RuntimeError(f"Error: El archivo '{ARBOL_JSON_PATH}' no se encontró. Asegúrate de que el archivo JSON del árbol de decisión esté en el mismo directorio.")
except json.JSONDecodeError:
    raise RuntimeError(f"Error: El archivo '{ARBOL_JSON_PATH}' no es un JSON válido. Verifica el formato del archivo.")

def get_node_by_id(node_id: str):
    for node in DECISION_TREE['nodes']:
        if node['id'] == node_id:
            return node
    return None

class UserResponse(BaseModel):
    current_node_id: str
    selected_option_value: str

@app.get("/")
async def read_root():
    return {"message": "Bienvenido al Sistema Experto de Aves Autóctonas de Tierra del Fuego"}

@app.get("/start")
async def start_consultation():
    root_node = get_node_by_id("root")
    if not root_node:
        raise HTTPException(status_code=500, detail="El nodo 'root' no se encontró en el árbol de decisión. El archivo JSON podría estar malformado o incompleto.")
    return {
        "node_id": root_node["id"],
        "question": root_node["question"],
        "options": [{"value": opt["value"]} for opt in root_node["options"]]
    }

@app.post("/consult")
async def consult_expert_system(user_response: UserResponse):
    current_node = get_node_by_id(user_response.current_node_id)
    if not current_node:
        raise HTTPException(status_code=404, detail=f"Nodo actual con ID '{user_response.current_node_id}' no encontrado.")

    next_step = None
    for option in current_node["options"]:
        if option["value"] == user_response.selected_option_value:
            next_step = option
            break

    if not next_step:
        raise HTTPException(status_code=400, detail=f"Opción seleccionada '{user_response.selected_option_value}' no válida para la pregunta actual.")

    if "result" in next_step:
        return {
            "node_id": "result",
            "result": next_step["result"],
            "message": "¡Hemos identificado el ave!"
        }
    elif "next" in next_step:
        next_node = get_node_by_id(next_step["next"])
        if not next_node:
            raise HTTPException(status_code=500, detail=f"El siguiente nodo '{next_step['next']}' no se encontró en el árbol de decisión. Posible error en el JSON.")
        return {
            "node_id": next_node["id"],
            "question": next_node["question"],
            "options": [{"value": opt["value"]} for opt in next_node["options"]]
        }
    else:
        raise HTTPException(status_code=500, detail="Error en la estructura del árbol de decisión: el nodo no tiene 'result' ni 'next'.")