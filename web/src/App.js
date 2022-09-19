// import logo from './logo.svg';
import './App.css';
import * as React from 'react';
import TextField from './components/Form';
import theme from './theme';
import { ThemeProvider } from '@mui/material/styles';

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        
        <header className="App-header">
          <h1>Disordered Protein Prediction Aggregator</h1>
        </header>
        <TextField></TextField>
      </ThemeProvider>
    
    </div>
  );
}

export default App;
