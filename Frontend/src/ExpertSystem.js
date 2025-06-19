// frontend/src/ExpertSystem.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ExpertSystem.css'; // Creamos este CSS después

const API_BASE_URL = 'http://127.0.0.1:8000'; // URL de tu API de FastAPI

function ExpertSystem() {
  const [currentNode, setCurrentNode] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  //const [selectedOption, setSelectedOption] = useState(''); // Para manejar la opción seleccionada si es un <select>
  const [answeredQuestionsCount, setAnsweredQuestionsCount] = useState(0);
  // Nuevo estado para el historial de preguntas y respuestas
  const [history, setHistory] = useState([]);

  useEffect(() => {
    // Al cargar el componente, inicia la consulta
    startConsultation();
  }, []); // El array vacío asegura que se ejecuta solo una vez al montar

  const startConsultation = async () => {
    setLoading(true);
    setError(null);
    setAnsweredQuestionsCount(0);
    setHistory([]); // Resetear el historial al inicio de una nueva consulta
    try {
      const response = await axios.get(`${API_BASE_URL}/start`);
      setCurrentNode(response.data);
    } catch (err) {
      console.error("Error al iniciar la consulta:", err);
      setError("No se pudo conectar con el sistema experto. Inténtalo de nuevo más tarde.");
    } finally {
      setLoading(false);
    }
  };

  const handleOptionSelect = async (optionValue) => {
    setLoading(true);
    setError(null);

    // Guardar la pregunta actual y la respuesta seleccionada en el historial
    // Necesitamos el texto completo de la pregunta del currentNode antes de actualizarlo
    const currentQuestionText = currentNode.question;
    setHistory(prevHistory => [
      ...prevHistory,
      { question: currentQuestionText, answer: optionValue }
    ]);

    try {
      const response = await axios.post(`${API_BASE_URL}/consult`, {
        current_node_id: currentNode.node_id,
        selected_option_value: optionValue
      });

      if (response.data.node_id !== "result") {
        setAnsweredQuestionsCount(prevCount => prevCount + 1);
      }

      setCurrentNode(response.data); // Actualiza el nodo actual con la respuesta de la API
      //setSelectedOption(''); // Resetea la opción seleccionada si se usó un <select>
    } catch (err) {
      console.error("Error al consultar:", err.response ? err.response.data : err.message);
      setError(`Error al procesar la respuesta: ${err.response?.data?.detail || 'Error desconocido'}`);
      // Si hay un error, podrías querer remover la última entrada del historial
      setHistory(prevHistory => prevHistory.slice(0, prevHistory.length -1));
    } finally {
      setLoading(false);
    }
  };

  //const progressPercentage = (answeredQuestionsCount / MAX_QUESTIONS) * 100;

  if (loading) {
    return <div className="expert-system-container">Cargando...</div>;
  }

  if (error) {
    return <div className="expert-system-container error-message">{error}</div>;
  }

  if (!currentNode) {
    return <div className="expert-system-container">No se pudo cargar el sistema experto.</div>;
  }

  // Si es un resultado final
  if (currentNode.node_id === "result") {
    return (
      <div className="expert-system-container result-card">
        <h2>{currentNode.message}</h2>
        <p className="bird-name">{currentNode.result}</p>

        {/* Resumen de la consulta */}
        <div className="summary-container">
          <h3>Tu camino a la identificación:</h3>
          <ul className="summary-list">
            {history.map((entry, index) => (
              <li key={index} className="summary-item">
                <span className="summary-question">{entry.question}</span>: <span className="summary-answer">{entry.answer}</span>
              </li>
            ))}
          </ul>
        </div>

        <button onClick={startConsultation} className="reset-button">
          Iniciar Nueva Consulta
        </button>
      </div>
    );
  }

  // Si es una pregunta
  return (
    <div className="expert-system-container question-card">
      <h2>{currentNode.question}</h2>
      <div className="options-container">
        {currentNode.options.map((option) => (
          <button
            key={option.value}
            className="option-button"
            onClick={() => handleOptionSelect(option.value)}
          >
            {option.value}
          </button>
        ))}
      </div>
      {/* Si prefieres un select en lugar de botones, podrías usar esto (descomentar y ajustar) */}
      {/* <select
        className="option-select"
        value={selectedOption}
        onChange={(e) => setSelectedOption(e.target.value)}
      >
        <option value="">Selecciona una opción</option>
        {currentNode.options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.value}
          </option>
        ))}
      </select>
      <button
        className="submit-button"
        onClick={() => handleOptionSelect(selectedOption)}
        disabled={!selectedOption}
      >
        Siguiente
      </button> */}
    </div>
  );
}

export default ExpertSystem;