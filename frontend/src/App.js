import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [fileId, setFileId] = useState('');
  const [spm, setSpm] = useState('');
  const [length, setLength] = useState(3);
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [references, setReferences] = useState([]);
  const [models, setModels] = useState([]);
  const [selectedModel, setSelectedModel] = useState('deepseek');
  const [backendUrl, setBackendUrl] = useState('https://spm-frontend-xzbb.onrender.com');

  useEffect(() => {
    fetch(`${backendUrl}/models`)
      .then(res => res.json())
      .then(data => setModels(data));
  }, [backendUrl]);

  const uploadFile = async () => {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await fetch(`${backendUrl}/upload`, {
      method: 'POST',
      body: formData
    });
    
    const data = await response.json();
    setFileId(data.file_id);
    setSpm('');
    setAnswer('');
  };

  const generateSPM = async () => {
    const formData = new FormData();
    formData.append('file_id', fileId);
    formData.append('length', length);
    formData.append('model_name', selectedModel);
    
    const response = await fetch(`${backendUrl}/generate-spm`, {
      method: 'POST',
      body: formData
    });
    
    const data = await response.json();
    setSpm(data.spm);
  };

  const askQuestion = async () => {
    const formData = new FormData();
    formData.append('file_id', fileId);
    formData.append('question', question);
    
    const response = await fetch(`${backendUrl}/chat`, {
      method: 'POST',
      body: formData
    });
    
    const data = await response.json();
    setAnswer(data.response);
    setReferences(data.references);
  };

  return (
    <div className="container">
      <h1>SPM Generator</h1>
      
      <div className="section">
        <h2>Upload PDF</h2>
        <input type="file" onChange={e => setFile(e.target.files[0])} />
        <button onClick={uploadFile}>Upload PDF</button>
      </div>
      
      {fileId && (
        <div className="section">
          <h2>Generate Summary</h2>
          
          <div className="form-group">
            <label>Model:</label>
            <select value={selectedModel} onChange={e => setSelectedModel(e.target.value)}>
              {models.map(model => (
                <option key={model} value={model}>{model}</option>
              ))}
            </select>
          </div>
          
          <div className="form-group">
            <label>Summary Length:</label>
            <select value={length} onChange={e => setLength(e.target.value)}>
              {[1,2,3,4,5].map(num => (
                <option key={num} value={num}>{num} pages</option>
              ))}
            </select>
          </div>
          
          <button onClick={generateSPM}>Generate SPM</button>
          
          {spm && (
            <div className="output">
              <h3>Summary for Policymakers</h3>
              <pre>{spm}</pre>
            </div>
          )}
        </div>
      )}
      
      {fileId && (
        <div className="section">
          <h2>Chat with Document</h2>
          <input 
            type="text" 
            value={question} 
            onChange={e => setQuestion(e.target.value)}
            placeholder="Ask about the document"
          />
          <button onClick={askQuestion}>Ask Question</button>
          
          {answer && (
            <div className="output">
              <h3>Answer:</h3>
              <p>{answer}</p>
              
              {references.length > 0 && (
                <div className="references">
                  <h4>References:</h4>
                  <ul>
                    {references.map((ref, index) => (
                      <li key={index}>
                        Page {ref.page}: {ref.excerpt}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
