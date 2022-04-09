import React, { useState, useEffect } from 'react';
import MyMap from './Map';

function App() {
  const dimensions = {
    width: 600,
    height: 300,
    margin: { top: 30, right: 30, bottom: 30, left: 60 }
  };

  const data = [{}]

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <p>The current time is {0}.</p>
        <MyMap data={data} dimensions={dimensions}/>
      </header>
    </div>
  );
}

export default App;
