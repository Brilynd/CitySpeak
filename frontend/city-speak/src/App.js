import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import "./App.css"
import MyMap from './Map';


function App() {

  return (
    <div>
      <header>
        <h1>City-Speak</h1>
      </header>
      <Grid container style={{minHeight: "80vh"}}>
        <Grid item xs={6}>
          <MyMap />
        </Grid>
        <Grid item xs={6}>
          <h2>Current Location: Paris</h2>
        </Grid>
      </Grid>
      
    </div>
  );
}

export default App;
