import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import ChoiceContextProvider from './context/ChoiceContext.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ChoiceContextProvider>
    <App />
    </ChoiceContextProvider>
  </React.StrictMode>,
)
