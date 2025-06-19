// frontend/src/App.js
import React from 'react';
import './App.css';
import ExpertSystem from './ExpertSystem'; // Importa el nuevo componente

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Sistema Experto de Aves Autóctonas de Tierra del Fuego</h1>
      </header>
      <main>
        <ExpertSystem /> {/* Renderiza el componente del sistema experto */}
      </main>
    </div>
  );
}

export default App;