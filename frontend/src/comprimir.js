import React, { useState } from 'react';

const Comprimir = () => {
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);

  const handleExport = async () => {
    setLoading(true);
    try {
      const response = await fetch('/tasks/comprimir/', {
        method: 'GET',
      });
      const data = await response.json();
      if (data.status === 'success') {
        setMessage(`Success: ${data.message}`);
      } else {
        setMessage(`Error: ${data.message}`);
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>comprimir Máquina Virtual</h1>
      <button onClick={handleExport} disabled={loading}>
        {loading ? 'Exportando...' : 'Exportar VM'}
      </button>
      <p>{message}</p>
    </div>
  );
};

export default Comprimir;
