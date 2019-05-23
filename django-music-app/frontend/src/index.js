import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import App from './App'
import { StoreProvider } from './Store'

ReactDOM.render(
    <StoreProvider>
        <App path='/'/>
    </StoreProvider>, 
document.getElementById('root'));

