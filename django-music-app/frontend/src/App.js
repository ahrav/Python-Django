import React, { Suspense } from 'react';
import { BrowserRouter } from 'react-router-dom';
import Home from './containers/Home/Home'




function App() {

  return (
    <div>
      <Suspense fallback="Loading..">
        <BrowserRouter>
          <Home />
        </BrowserRouter>
      </Suspense>
    </div>
  );
}

export default App;
