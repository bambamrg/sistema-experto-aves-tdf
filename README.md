![image](https://github.com/user-attachments/assets/3f8022e3-3441-4202-a881-3d805b16d6ee)

TECNICATURA SUPERIOR EN CIENCIA DE DATOS E INTELIGENCIA ARTIFICIAL

MATERIA: Desarrollo de Sistemas de Inteligencia Artificial

DOCENTE: Lic. Mirabete Martín

ALUMNO: Aranda Iván

# Sistema experto de IA
Sistema experto de ia para la identificación de aves de la provincia de tierra del fuego

## Descripción del proyecto
Este proyecto se centra en el desarrollo de un Sistema Experto que reconozca e identifique aves autóctonas presentes en la provincia de Tierra del Fuego, creando una herramienta intuitiva que, a partir de ciertas características observables, pueda guiar a personas no expertas en la identificación de las diversas especies que habitan en nuestra provincia.

Se consultó a un experto humano - Maximiliano Aguilar - Agente de conservación de áreas protegidas del municipio de Río Grande. El conocimiento extraído se representó mediante un árbol de decisión para facilitar la toma de decisiones secuencial y lógica.

## Guía de instalación y ejecución

### Requisitos previos
Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas en tu sistema operativo:

1. Python 3.8 o superior:
   * Verifica tu versión: Abre una terminal y escribe python --version o python3 --version.
   * Descarga: python.org/downloads/
2. pip (Administrador de paquetes de Python):
   * Generalmente viene incluido con Python.
   * Verifica: pip --version o pip3 --version.
3. Node.js (LTS recomendado):
   * Incluye npm (Node Package Manager).
   * Verifica tu versión: node -v y npm -v.
   * Descarga: nodejs.org/es/download/
4. Editor de código
   * Como Visual Studio Code (VSC)

### Clonar el repositorio
Crear una carpeta en la que se clonara y guaradará este repositorio

### Pasos de instalación
1.  Configuración y Ejecución del Backend (FastAPI)
   
    * Crear y Activar un Entorno Virtual (Recomendado):
      
    * Crear el entorno virtual:
      
        python -m venv venv
      
    * Activar el entorno virtual:
      
    En Windows (Command Prompt):
    
        .\venv\Scripts\activate
    
      (Verás (venv) al inicio de tu línea de comando si se activó correctamente).
    
    * Instalar las Dependencias de Python:
      
    Con el entorno virtual activado, instala las librerías necesarias para FastAPI.
    
        pip install -r requirements.txt
    
    * Ejecutar el Servidor FastAPI:
      
    Ahora, inicia el servidor de FastAPI.
    
        uvicorn main:app --reload
    
      Deja esta terminal abierta y el servidor ejecutándose.

3. Configuración y Ejecución del Frontend (React)
    * Navega al Directorio del Frontend:
      
    Abre tu segunda terminal y ve a la carpeta frontend de tu proyecto:
   
        cd sistema-experto-aves-tdf/frontend
   
    * Instalar las Dependencias de Node.js:
      
    Instala todas las librerías de React y otras dependencias del frontend
   
    * Ejecutar la Aplicación React:
      
    Inicia el servidor de desarrollo de React.
   
        npm start
   
      Esto abrirá automáticamente tu navegador web en http://localhost:3000. Si no se abre, navega manualmente a esa dirección.
   
      Deberías ver tu aplicación de sistema experto.
   
      Deja esta terminal abierta y el servidor ejecutándose.

# Estructura del proyecto

mi_sistema_experto_aves/
├── .gitignore              # Archivo para Git para ignorar archivos y carpetas no deseados
├── README.md               # Documentación general del proyecto (cómo funciona, cómo ejecutarlo, etc.)
├── .venv/              # Directorio para el entorno virtual de Python (ignorado por Git)
├── main.py             # Archivo principal de la aplicación FastAPI y lógica del sistema experto
├── arbol.json          # Archivo JSON con la base de conocimiento del árbol de decisión
├── requirements.txt    # Lista de dependencias de Python (generada con `pip freeze > requirements.txt`)
├── Documentos
│
└── Frontend/               # Contiene todo lo relacionado con la aplicación React
|   ├── node_modules
    ├── public/             # Archivos estáticos públicos (index.html, favicon.ico, imágenes estáticas)
    │   └── index.html
    │   └── favicon.ico
    │   └── logo192.png
    |   └── logo512.png
    |   └── manifest.json
    |   └── robots.txt
    ├── src/                # Código fuente de la aplicación React
    │   ├── ExpertSystem.js      # Lógica principal del componente
    │   └── ExpertSystem.css     # Estilos específicos del componente
    │   ├── App.js          # Componente raíz de la aplicación
    │   ├── App.css         # Estilos globales de la aplicación
    |   ├── App.test.js
    │   ├── index.js        # Punto de entrada de la aplicación React
    │   ├── index.css       # Estilos CSS globales para el body, etc.
    |   ├── logo.svg
    |   ├── reportWebVitals.js
    |   └── setupTests.js
    ├── .gitignore
    ├── package.json        # Archivo de configuración de Node.js/npm (dependencias, scripts)
    ├── package-lock.json   # Bloqueo de versiones exactas de dependencias (generado automáticamente)
    └── README.md           # Documentación específica del frontend
