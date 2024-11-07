// App.js

import React from 'react';
import './styles.css';

function App() {
  return (
    <div className="container1">
      <h1>Prompcorp</h1>
      <nav className="sidebar">
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="sup_search.html">Supplier search</a></li>
          <li><a href="sup_induction.html">Supplier/Agent Induction information</a></li>
          <li><a href="metrics.html">Metrics</a></li> 
        </ul>
      </nav>
      <div className="content">
        <p>This is a simple web interface created using React.js.</p>
      </div>
    </div>
  );
}

export default App;
